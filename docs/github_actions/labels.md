# GitHub Action: Label Synchronization

This GitHub Action workflow automates the synchronization of GitHub labels based on a YAML configuration file. It runs on changes to the label configuration or its workflow file and ensures consistency in label management across the repository.

[github-labeler.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/github-labeler.yml)

---

## Workflow Details

### Triggers (`on`)

- **`push`**:
    - Triggered when changes are pushed to the `main` branch.
    - Monitored paths:
        - `.github/labels.yml`: The YAML file containing label definitions.
        - `.github/workflows/labels.yml`: The workflow configuration for label synchronization.
- **`pull_request`**:
    - Triggered when pull requests modify the `.github/labels.yml` or `.github/workflows/labels.yml` files.

---

## Job Details

### **labeler**

**`runs-on`**: `ubuntu-latest`

**Steps**:

1. **Checkout repository**:
   - Uses `actions/checkout@v4` to fetch the repository content.

2. **Run Labeler**:
   - Uses `crazy-max/ghaction-github-labeler@v5` to synchronize labels based on the `.github/labels.yml` file.
   - **Inputs**:
     - `github-token`: A personal access token (PAT) stored in the repository's secrets for authentication.
     - `yaml-file`: Specifies the path to the label configuration file (`.github/labels.yml`).
     - `dry-run`: Simulates the label synchronization process when the workflow is triggered by a pull request (`true` for pull requests, `false` otherwise).
     - `exclude`: Excludes specific labels from synchronization. Here, labels matching `help*` or `*issue` are excluded.

---

In summary, this workflow ensures that GitHub labels in your repository remain consistent with the definitions in `.github/labels.yml`. It supports both live updates for pushes and simulation mode for pull requests, providing a robust solution for label management.
