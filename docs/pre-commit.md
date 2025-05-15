# Pre-commit configuration

this project uses [pre-commit](https://pre-commit.com/) to run checks on every commit.

Configuration file: [.pre-commit-config.yaml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.pre-commit-config.yaml)

> If you initialize you project using `make install` pre-commit is already installed and configured.
> If not, you can install pre-commit running in terminal `uv run pre-commit install` in the root of the project.

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

- [`ruff`](https://docs.astral.sh/ruff/): This hook runs the Ruff linter with the `--fix` option to automatically fix issues in scripts and notebooks and a custom configuration file.
- [`ruff-format`](https://docs.astral.sh/ruff/): This hook runs the Ruff formatter.

## pre-commit/mirrors-mypy

This repository contains a mirror of mypy for pre-commit.

- [`mypy`](http://mypy-lang.org/): This hook runs mypy, a static type checker for Python, with a custom configuration file.

## commitizen-tools/commitizen

This repository contains hooks for commitizen.

- [`commitizen`](https://commitizen-tools.github.io/commitizen/): This hook checks that commit messages follow the conventional commit format.
