# 🔑 Setup Tokens

Some of the github actions require token keys to be set as secrets in the github repository. The following tokens are required:

## Github Action secrets.PAT

This is the personal access token for the github repository and It is used to:

- Push the MKDocs documentation to the `gh-pages` branch.
- Push the pre-commit autoupdate to the `main` branch.

How to configure the secrets.PAT:

- Create in github a [Personal Access Token (PAT)](https://github.com/settings/tokens?type=beta),for the specific repository. [How](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
- Give it read/write access to "Contents", "Pull Requests" and "Workflows" under the "Repository Permissions" section.
- Add de PAT to the repository secrets. Go to the repository settings > Secrets and variables > Actions. THen in Repository secrets add a new repository secret and Name it `PAT` and paste the token.
- You must explicitly allow GitHub Actions to create pull requests. This setting can be found in a repository's settings under Actions > General > Workflow permissions. select `Read repository contents and packages permissions`

## CODECOV_TOKEN

This is the token for codecov. It is used to upload the coverage report to codecov. You can get it from codecov.io. It is not required for local development.
<https://docs.codecov.com/docs/quick-start>

You have to add this secret to the github repository. How to add codecov to the github repository: <https://docs.codecov.com/docs/adding-the-codecov-token#github-actions>

---

## References

- <https://github.com/peter-evans/create-pull-request?tab=readme-ov-file#workflow-permissions>
- <https://github.com/peter-evans/create-pull-request/issues/2443>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token>
