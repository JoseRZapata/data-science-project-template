# GitHub Action: Automerge

This GitHub Action workflow automates the merging of pull requests labeled with `automerge`. It supports scheduled runs and manual execution, ensuring streamlined integration of changes that meet predefined criteria.

[automerge.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/automerge.yml)

---

## Workflow Details

### Triggers (`on`)

- **`schedule`**:
    - Automatically runs **every hour on Sundays** (UTC) to catch staggered PR-creating jobs (`0 * * * 0`).
    - Runs daily at 08:00 UTC Monday–Saturday (`0 8 * * 1-6`).
- **`workflow_dispatch`**:
    - Allows manual execution of the workflow via the GitHub Actions interface.

---

## Job Details

### **automerge**

**`runs-on`**: `ubuntu-latest`

**Steps**:

1. **Automerge**:
   - Uses the `pascalgn/automerge-action@v0.16.3` action to merge pull requests that meet specific criteria.
   - **Environment Variables**:
     - `GITHUB_TOKEN`: A personal access token (PAT) stored in the repository's secrets for authentication.
     - `MERGE_METHOD`: Specifies the merge method. In this case, the `squash` method is used, which combines all commits into a single commit when merging.
     - `MERGE_REQUIRED_APPROVALS`: Defines the required number of approvals for merging. Here, it is set to `"0"`, meaning no approvals are required.
     - `MERGE_LABELS`: Specifies the label (`automerge`) that triggers the automerge process.

---

In summary, this workflow simplifies the process of merging pull requests by automatically merging those labeled with `automerge` using the `squash` method. It can be executed daily or manually, ensuring flexibility and efficiency in the development process.

---

## Required Repository Setting for Automated PR Workflows

For the automerge workflow (and other bot-created PRs like Dependabot, `update_template_deps`, `update_template_workflows`) to run their CI checks **automatically without manual approval**, you must configure the following setting in your **generated project's repository**:

1. Go to **Settings → Actions → General**
2. Under **"Fork pull request workflows from outside collaborators"**, select:
   - **"Require approval for first-time contributors who are new to GitHub"** (recommended), or
   - **"Read‑only"** (if you trust all contributors)

Without this setting, PRs created by bots will show **"X workflows awaiting approval"** and their checks will remain blocked until a maintainer manually approves each run.

This setting only needs to be configured once per generated repository.
