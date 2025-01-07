# GitHub Action: Documentation Build and Deployment

This GitHub Action workflow automates the process of building and deploying project documentation using `mkdocs`. It ensures that documentation updates are automatically published whenever pull requests affecting specific files are merged or when triggered manually.

[docs.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/docs.yml)

---

## Workflow Details

### Triggers (`on`)

- **`pull_request`**:
    - Triggered when a pull request affecting documentation files is closed (merged) into the `main` branch.
    - Monitored paths:
        - Files in the `docs/` directory.
        - `readme.md`.
- **`workflow_dispatch`**: Allows manual triggering of the workflow via the GitHub user interface.

---

## Job Details

### **build-and-publish**

**`runs-on`**: `ubuntu-latest`

**Steps**:

1. **Checkout repository**:
   - Uses `actions/checkout@v4` to fetch the repository contents, ensuring access to the latest documentation files.

2. **Install `uv`**:
   - Sets up the `uv` tool using `astral-sh/setup-uv@v5`.

3. **Set up Python**:
   - Configures Python according to the `.python-version` file using `actions/setup-python@v5`.

4. **Build documentation**:
   - Runs `mkdocs build --clean` via `uv` to generate the static documentation site. The `--clean` option ensures that the output directory is cleared before building.

5. **Deploy documentation**:
   - Uses `peaceiris/actions-gh-pages@v3` to publish the built documentation to GitHub Pages.
   - **Inputs**:
     - `github_token`: A Personal Access Token (PAT) stored as a repository secret.
     - `publish_dir`: Specifies the directory containing the built site (`./site`).

---

In summary, this workflow streamlines the process of building and deploying documentation. It automatically updates GitHub Pages whenever documentation-related files are merged into the main branch, with the added flexibility of manual triggering for on-demand updates.
