# GitHub Action:Pre-commit auto-update

This GitHub Action file configures a workflow named "Pre-commit auto-update". This workflow is responsible for automatically updating the pre-commit hooks in your repository.

[pre-commit_autoupdate.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/pre-commit_autoupdate.yml)

## Workflow Details

- `on`: This workflow is triggered in two situations:

  - `schedule`: It runs automatically every Monday at 7:00 UTC (according to the cron schedule `"0 7 * * 1"`).
  - `workflow_dispatch`: This allows the workflow to be manually run from the GitHub user interface.
- `jobs`: Defines a job named "pre-commit-update".

## Job "pre-commit-update" Details

`runs-on`: This job runs on the latest version of Ubuntu.

`steps`: Defines the steps to be followed in this job.

`Checkout`: This step uses the actions/checkout@v3 action to get a copy of the repository.

`Update pre-commit hooks`: This step uses the `brokenpip3/action-pre-commit-update` action to update the pre-commit hooks. This action requires a GitHub token to function, which is passed through `github-token: ${{ secrets.PAT }}`. [PAT] is a secret stored in the repository settings that contains a personal access token with repository scope.

In summary, this workflow takes care of keeping the pre-commit hooks in the repository up-to-date, running automatically every Monday and also allowing manual execution whenever necessary.

[PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token
