# GitHub Action: Automerge

This GitHub Action workflow automates the merging of pull requests labeled with `automerge`. It supports scheduled runs and manual execution, ensuring streamlined integration of changes that meet predefined criteria.

[automerge.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/automerge.yml)

---

## Workflow Details

### Triggers (`on`)

- **`schedule`**:
    - Automatically runs daily at 08:00 UTC (according to the cron schedule: `0 8 * * *`).
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
