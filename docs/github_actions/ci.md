
# GitHub Action: CI/CD Tests

This GitHub Action workflow is designed to streamline and automate the CI/CD processes for your project. The workflow is triggered on pull requests and pushes to the `main` branch. It performs several key tasks including linting, pre-commit checks, project update validation, and running tests with coverage reporting.

[ci-cd-tests.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/ci-cd-tests.yml)

---

## Workflow Details

### Triggers (`on`)

- **`pull_request`**: The workflow runs when a pull request is opened or updated.
- **`push`**: The workflow is triggered for pushes to the `main` branch.

### Jobs Overview

The workflow defines four jobs:

1. **`actionlint`**: Validates the syntax and structure of GitHub Action workflow files.
2. **`lint-cruft`**: Ensures no `.rej` files are present, verifying that project updates were applied correctly.
3. **`pre-commit`**: Executes pre-commit hooks to enforce code standards and formatting in all files.
4. **`test`**: Runs unit tests with coverage reporting and uploads the results to Codecov.

---

## Job Details

### **1. actionlint**

**`runs-on`**: `ubuntu-latest`

**Steps**:

- **Checkout**: Uses `actions/checkout@v4` to fetch the repository.
- **Download actionlint**: Fetches `actionlint`  using a bash script.
- **Check workflow files**: Runs `actionlint` to validate the workflow files.

---

### **2. lint-cruft**

**`runs-on`**: `ubuntu-latest`

**Steps**:

- **Checkout**: Uses `actions/checkout@v4` to fetch the repository.
- **Check for `.rej` files**: Fails the job if `.rej` files are found, indicating an unsuccessful project structure update.

---

### **3. pre-commit**

**`runs-on`**: `ubuntu-latest`

**Steps**:

- **Checkout**: Uses `actions/checkout@v4` to fetch the repository.
- **Install `uv`**: Sets up the `uv` tool using `astral-sh/setup-uv@v5`.
- **Run pre-commit hooks**: Executes all pre-commit hooks across the repository, displaying any failures with colorized diffs.

---

### **4. test**

**`runs-on`**: `ubuntu-latest`

**Steps**:

- **Checkout**: Uses `actions/checkout@v4` to fetch the repository.
- **Install `uv`**: Sets up the `uv` tool using `astral-sh/setup-uv@v5`.
- **Set up Python**: Configures Python according to the `.python-version` file using `actions/setup-python@v5`.
- **Install the project**: Installs the project with all extras and development dependencies using `uv sync`.
- **Run tests with coverage**: Executes tests with `pytest` and generates a coverage report in XML format.
- **Upload coverage report**: Uploads the coverage report to Codecov using `codecov/codecov-action@v4`. Requires a `CODECOV_TOKEN` secret stored in the repository settings.

---

In summary, this workflow automates linting, project update validation, pre-commit checks, testing, and coverage reporting for a robust CI/CD pipeline.
