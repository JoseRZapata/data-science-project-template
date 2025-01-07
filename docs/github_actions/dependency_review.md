# GitHub Action: Dependency Review

This GitHub Action workflow is designed to automatically review changes to your project dependencies during pull requests. It uses GitHub's `dependency-review-action` to analyze the dependency graph and flag potential security issues or unwanted changes in dependencies.

[dependency-review.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/dependency-review.yml)

---

## Workflow Details

### Triggers (`on`)

- **`pull_request`**: The workflow is triggered whenever a pull request is created or updated, ensuring dependency reviews are performed as part of the code review process.

### Permissions

- **`contents: read`**: Grants the workflow read-only access to the repository's contents, which is sufficient for performing the dependency review.

---

## Job Details

### **dependency-review**

**`runs-on`**: `ubuntu-latest`

**Steps**:

1. **Checkout repository**:
   - Uses `actions/checkout@v4` to fetch the pull request's code for analysis.
2. **Dependency Review**:
   - Uses `actions/dependency-review-action@v4` to analyze changes to dependencies. This action checks for:
     - Newly added dependencies.
     - Updates to existing dependencies.
     - Security vulnerabilities in any affected dependencies.

---

In summary, the "Dependency Review" workflow enhances your project’s security by automatically evaluating dependency changes in pull requests, helping you catch potential issues early in the development cycle.
