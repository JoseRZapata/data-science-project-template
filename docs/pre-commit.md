# Pre-commit configuration

this project uses [pre-commit](https://pre-commit.com/) to run checks on every commit.

Configuration file: [.pre-commit-config.yaml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.pre-commit-config.yaml)

## pre-commit/pre-commit-hooks

This repository contains some out-of-the-box hooks provided by the [pre-commit project](https://github.com/pre-commit/pre-commit-hooks).

- `trailing-whitespace`: This hook trims trailing whitespace.
- `end-of-file-fixer`: This hook ensures that a file is either empty, or ends with one newline.
- `check-yaml`: This hook checks yaml files for parseable syntax.
- `check-case-conflict`: This hook checks for files with names that would conflict on a case-insensitive filesystem like MacOS HFS+ or Windows FAT.
- `debug-statements`: This hook checks for Python debug statements.
- `detect-private-key`: This hook checks for the addition of private keys.
- `check-merge-conflict`: This hook checks for files that contain merge conflict strings.
- `check-ast`: This hook checks Python source files for syntactically valid ast.
- `check-added-large-files`: This hook prevents adding large files. The max size is configurable.

## astral-sh/ruff-pre-commit

This repository contains hooks for the Ruff programming language.

- [`ruff`](https://docs.astral.sh/ruff/): This hook runs the Ruff linter with the `--fix` option to automatically fix issues and a custom configuration file.
- [`ruff-format`](https://docs.astral.sh/ruff/): This hook runs the Ruff formatter.

## pre-commit/mirrors-mypy

This repository contains a mirror of mypy for pre-commit.

- [`mypy`](http://mypy-lang.org/): This hook runs mypy, a static type checker for Python, with a custom configuration file.

## PyCQA/bandit

This repository contains Bandit, a tool designed to find common security issues in Python code.

- [`bandit`](https://github.com/PyCQA/bandit): This hook runs Bandit with a custom configuration file.

## Yelp/detect-secrets

This repository contains a tool to detect secrets in the code base. [yelp detect-secrets](https://github.com/Yelp/detect-secrets)

- `detect-secrets`: This hook runs detect-secrets, a tool to detect secrets in the code base.
- `detect-secrets-jupyter`: This hook runs detect-secrets specifically for Jupyter notebooks.
