# 🔑 Setup tokens for GitHub Actions

This template now uses **`GITHUB_TOKEN` by default** for most workflows.

`GITHUB_TOKEN` is automatically created by GitHub Actions on each run, so you usually **do not** need to create a custom PAT secret.

## 1) Recommended default: `GITHUB_TOKEN`

### What to configure in the repository

1. Go to **Settings → Actions → General → Workflow permissions**.
2. Select **Read and write permissions**.
3. Enable **Allow GitHub Actions to create and approve pull requests** (required for PR automation workflows).

In workflows, use:

```yaml
with:
  github-token: ${{ secrets.GITHUB_TOKEN }}
```

or:

```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Also set explicit permissions in each workflow/job when needed, for example:

```yaml
permissions:
  contents: write
  pull-requests: write
  issues: write
```

## 2) When is a PAT still needed?

Use a PAT (or GitHub App token) only for advanced cases, such as:

- You need automation-created PRs/commits to trigger additional workflows in a way that `GITHUB_TOKEN` restrictions prevent.
- You need to access **another repository** (cross-repo operations).
- An action feature explicitly requires scopes not available with your current `GITHUB_TOKEN` permissions.

If needed, create a repository secret named `PAT`.

## 3) Transitional fallback (optional)

If you are migrating existing repositories, you can temporarily use:

```yaml
${{ secrets.PAT || github.token }}
```

This keeps old repos working while you remove PAT dependencies.

## 4) CODECOV_TOKEN

`CODECOV_TOKEN` is still required for Codecov upload workflows (depending on your Codecov setup).

- <https://docs.codecov.com/docs/quick-start>
- <https://docs.codecov.com/docs/adding-the-codecov-token#github-actions>

---

## References

- <https://docs.github.com/en/actions/security-guides/automatic-token-authentication>
- <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions>
- <https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow>
- <https://github.com/peter-evans/create-pull-request?tab=readme-ov-file#workflow-permissions>
- <https://github.blog/changelog/2023-02-02-github-actions-updating-the-default-github_token-permissions-to-read-only/>