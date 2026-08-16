"""Update GitHub Actions versions inside the generated project's workflows.

Dependabot cannot target `{{cookiecutter.repo_name}}/.github/workflows` directly
because the `directory` option rejects paths containing glob-like characters
(the `{{ }}` in the cookiecutter folder name is interpreted as a glob brace
pattern). This script replicates Dependabot's github-actions update behaviour
for that folder only, using the GitHub Releases API to find the latest tag
for each `owner/repo` referenced via `uses:`.
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ACTION_TEMPLATE_DIR = "{{cookiecutter.repo_name}}/.github/workflows"

# Matches: uses: "owner/repo@v1.2.3"  or  uses: owner/repo@v1.2.3
# Ignores local/docker actions (./path, docker://) which don't have owner/repo@tag shape.
USES_PATTERN = re.compile(r'(uses:\s*"?)([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)@([A-Za-z0-9_.\-]+)("?)')


MAJOR_ONLY_RE = re.compile(r"^v?\d+$")


def _fetch_json(url: str) -> dict | list | None:
    """Fetch and parse a JSON response from a GitHub API URL."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        print(f"Invalid URL scheme: {parsed.scheme}", file=sys.stderr)
        return None
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)  # noqa: S310
    with urllib.request.urlopen(req, timeout=10) as response:  # noqa: S310
        result: dict | list = json.loads(response.read().decode())
        return result


def get_latest_tag(owner_repo: str, current_tag: str) -> str | None:
    """Fetch the latest tag for a GitHub owner/repo.

    If `current_tag` uses a "major-only" floating style (e.g. "v4"), prefer
    the latest matching major-only tag from the repo's tag list (mirrors how
    most Actions publish `v4`, `v5`, ... floating tags). Otherwise fall back
    to the latest GitHub release tag (full semver, e.g. "0.0.5").

    Args:
        owner_repo (str): "owner/repo" string.
        current_tag (str): The tag currently referenced in the workflow.

    Returns:
        Optional[str]: The latest tag name, or None if not found.

    Examples:
        >>> get_latest_tag("actions/checkout", "v4")
        'v4'
        >>> get_latest_tag("nonexistent-owner/nonexistent-repo-xyz", "v1")
        None

    """
    try:
        release_data = _fetch_json(f"https://api.github.com/repos/{owner_repo}/releases/latest")
        release_tag: str | None = (
            str(release_data["tag_name"])
            if isinstance(release_data, dict) and release_data.get("tag_name") is not None
            else None
        )

        if MAJOR_ONLY_RE.match(current_tag):
            tags_data = _fetch_json(f"https://api.github.com/repos/{owner_repo}/tags?per_page=100")
            if isinstance(tags_data, list):
                major_tags = [t["name"] for t in tags_data if isinstance(t, dict) and "name" in t]
                major_only = [t for t in major_tags if MAJOR_ONLY_RE.match(t)]
                if major_only:
                    best_major_only = str(max(major_only, key=lambda t: int(t.lstrip("v"))))
                    # If the repo stopped publishing floating major tags (its
                    # latest full release has a higher major than the best
                    # floating tag we found), fall back to the full release tag.
                    release_major = re.match(r"^v?(\d+)", release_tag) if release_tag else None
                    if release_major and int(release_major.group(1)) > int(
                        best_major_only.lstrip("v")
                    ):
                        return release_tag
                    return best_major_only
    except Exception as e:
        print(f"Error fetching latest tag for {owner_repo}: {e}", file=sys.stderr)
        return None
    else:
        return release_tag


def update_file(file_path: str | Path) -> bool:
    """Update `uses:` action references in a workflow file to their latest tag.

    Args:
        file_path (Union[str, Path]): Path to the workflow file to update.

    Returns:
        bool: True if the file was modified.

    """
    path = Path(file_path)
    content = path.read_text(encoding="utf-8")

    new_content = content
    modified = False

    for match in USES_PATTERN.finditer(content):
        full_match = match.group(0)
        prefix = match.group(1)
        owner_repo = match.group(2)
        current_tag = match.group(3)
        suffix = match.group(4)

        print(f"Checking {owner_repo} (current: {current_tag})...")
        latest_tag = get_latest_tag(owner_repo, current_tag)

        if latest_tag and latest_tag != current_tag:
            print(f"  -> Updating {owner_repo} to {latest_tag}")
            new_string = f"{prefix}{owner_repo}@{latest_tag}{suffix}"
            new_content = new_content.replace(full_match, new_string)
            modified = True
        else:
            print("  -> Up to date or failed to fetch.")

    if modified:
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {file_path}")
    else:
        print(f"No changes needed for {file_path}")

    return modified


def main(target_dir: str | Path = ACTION_TEMPLATE_DIR) -> None:
    """Update all workflow files (*.yml, *.yaml) in the given directory.

    Args:
        target_dir (Union[str, Path]): Directory containing workflow files.

    """
    directory = Path(target_dir)
    if not directory.is_dir():
        # allow running from scripts/ directory
        directory = Path("..") / target_dir
        if not directory.is_dir():
            print(f"Could not find directory {target_dir}")
            sys.exit(1)

    workflow_files = sorted({*directory.glob("*.yml"), *directory.glob("*.yaml")})
    if not workflow_files:
        print(f"No workflow files found in {directory}")
        sys.exit(1)

    any_modified = False
    for workflow_file in workflow_files:
        print(f"\n--- {workflow_file} ---")
        if update_file(workflow_file):
            any_modified = True

    if not any_modified:
        print("\nNo workflow files needed updates.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else ACTION_TEMPLATE_DIR
    main(target)
