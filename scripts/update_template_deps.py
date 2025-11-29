import json
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse


def get_latest_version(package_name: str) -> str | None:
    """Fetch the latest version of a package from PyPI.

    Args:
        package_name (str): The name of the package.
    Returns:
        Optional[str]: The latest version as a string, or None if not found.

    Raises:
        Exception: If there is an error fetching data from PyPI.

    Examples:
        >>> get_latest_version("requests")
        '2.28.1'
        >>> get_latest_version("nonexistent-package-xyz")
        None

    """
    try:
        url = f"https://pypi.org/pypi/{package_name}/json"
        # S310: Validate URL scheme to prevent security issues
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            print(
                f"Invalid URL scheme for {package_name}: {parsed.scheme}",
                file=sys.stderr,
            )
            return None
        with urllib.request.urlopen(url, timeout=10) as response:  # noqa: S310
            data = json.loads(response.read().decode())
            version = data.get("info", {}).get("version")
            return str(version) if version is not None else None
    except Exception as e:
        print(f"Error fetching version for {package_name}: {e}", file=sys.stderr)
        return None


def update_file(file_path: str | Path) -> None:
    """Update the dependencies in the given file to their latest versions.
    Args:
        file_path (Union[str, Path]): Path to the file to update.
    """

    path = Path(file_path)
    content = path.read_text(encoding="utf-8")

    # Regex to match dependencies defined like "package>=1.2.3"
    # It handles the quote, package name, >=, and version.
    # We capture the full line to replace the version part.
    # This regex assumes the format found in the user's file: "package>=version",
    pattern = re.compile(r'(")([a-zA-Z0-9_\-\[\]]+)(>=)(\d+\.\d+\.\d+)(")')

    new_content = content
    modified = False

    for match in pattern.finditer(content):
        full_match = match.group(0)
        quote_start = match.group(1)
        package = match.group(2)
        operator = match.group(3)
        current_version = match.group(4)
        quote_end = match.group(5)

        # Clean package name for API call (remove extras like [pyproject])
        clean_package = package.split("[")[0]

        print(f"Checking {clean_package} (current: {current_version})...")
        latest_version = get_latest_version(clean_package)

        if latest_version and latest_version != current_version:
            print(f"  -> Updating {clean_package} to {latest_version}")
            new_string = f"{quote_start}{package}{operator}{latest_version}{quote_end}"
            new_content = new_content.replace(full_match, new_string)
            modified = True
        else:
            print("  -> Up to date or failed to fetch.")

    if modified:
        path.write_text(new_content, encoding="utf-8")
        print(f"Updated {file_path}")
    else:
        print(f"No changes needed for {file_path}")


if __name__ == "__main__":
    target_file = "{{cookiecutter.repo_name}}/pyproject.toml"
    if len(sys.argv) > 1:
        target_file = sys.argv[1]

    # Resolve path relative to the script location or current working directory
    # Assuming script is run from root of repo or scripts dir
    if Path(target_file).exists():
        update_file(target_file)
    elif Path("..") / target_file:
        # Try to find it if we are in scripts dir
        f = Path("..") / target_file
        if f.exists():
            update_file(f)
        else:
            print(f"Could not find {target_file}")
            sys.exit(1)
    else:
        print(f"Could not find {target_file}")
        sys.exit(1)
