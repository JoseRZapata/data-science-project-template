# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.3.0] - 2026-02-22

### Added 🚀

- Added Spanish translation for all documentation using `mkdocs-static-i18n`.
- Added `README.es.md` with translated content.
- Added `mkdocs-static-i18n` plugin to `mkdocs.yml` to support multi-language documentation.
- Added `mkdocs-static-i18n` to the `docs` dependencies in `pyproject.toml`.
- Added `CHANGELOG.md` to the cookiecutter template (`{{cookiecutter.repo_name}}/CHANGELOG.md`).

### Changed 💥

- Updated `.github/workflows/docs.yml` to trigger on changes to `mkdocs.yml`.

## [Released]

## [1.2.0] - 2025-11-29

### Added 🚀

- New workflow for automatic template dependency updates with corresponding script

### Changed 💥

- Updated actions/github-script from 7 to 8
- Updated actions/setup-python from 5 to 6
- Updated actions/checkout from 5 to 6
- Updated astral-sh/setup-uv from 6 to 7
- Updated pytest-cov from 6.3.0 to 7.0.0
- Multiple updates to mkdocs-material package
- Updated multiple Python packages dependencies
- Updated documentation and pre-commit hooks

## [1.1.4] - 2025-09-09

### Added 🚀

Update README.md removing hydra information and fix make file information to install environment with uv

## [1.1.3] - 2025-03-19

Update Codecov configurations

### Changed 💥

Codecov github action configuration has been updated to use the new version of the action.

### Added 🚀

Update docs to config local repository with github

## [1.1.2] - 2025-03-19

add new commands to makefile

### Changed 💥

`Makefile` and `{{cookiecutter.repo_name}}/Makefile`

### Added 🚀

- `make test_coverage`: ## Test coverage report coverage.xml
- `make switch_main`: ## Switch to main branch and pull
- `clean_branchs`: ## Clean local branches already merged on the remote

## [1.1.0] - 2025-02-26

Changed pipeline folder structure in src to match MLOps description by Google

### Added 🚀

- google mlops link reference

### Changed 💥

- File restructuring:

{{cookiecutter.repo_name}}/src/pipelines: change folder structure
conf/: change folder names

## [1.1.1] - 2025-03-02

Changed lib folder structure in src to match MLOps description by Google

### Changed 💥

- File restructuring:

{{cookiecutter.repo_name}}/src/libs: change folder structure
conf/: change folder names

## [1.1.0] - 2025-02-26

Changed pipeline folder structure in src to match MLOps description by Google

### Added 🚀

- google mlops link reference

### Changed 💥

- File restructuring:

{{cookiecutter.repo_name}}/src/pipelines: change folder structure
conf/: change folder names

## [1.0.1] - 2025-02-14

The Main change in this to configure vscode settings for run RUFF native server and updates dependencies and pre-commit hooks.

### Changed 💥

- `pyproject.toml` and `uv.lock` upgrade dependencies
- `.pre-commit-config.yaml` hooks update

### Fixed 🐞

- `.vscode/settings.json` to configure vscode settings for run RUFF native server

## [1.0.0] - 2025-01-07

The Main change in this Pull Request is the migration from poetry to uv to manage the dependencies and the environment of the project.

### Added 🚀

- [UV](https://docs.astral.sh/uv/) has been added to the project to manage the dependencies and the environment of the project.
- Add python 3.12 to the testing matrix.

### Changed 💥

- `pyproject.toml` has been change to uses [UV](https://docs.astral.sh/uv/) and the standards in PEP, so is not compatible with **poetry anymore**.
- `Makefile` has been updated to use `uv` instead of `poetry` in the scripts.
- update the CI to use `uv` instead of `poetry` in:
    git- `ci.yaml` workflow
    - `docs.yaml`workflow
- Add `uv.lock` to the project dependencies instead of `poetry.lock`.
- Update the documentation to use `uv` instead of `poetry` in:
    - `docs/setup_tokens.md`
    - `docs/pre-commit.md`
    - `docs/local_setup.md`
- Update the `README.md` to use `uv` instead of `poetry`.

### Removed 🔥

- `poetry.lock` has been removed from the project.

### Fixed 🐞

- Fix ci.yaml to use `uv`, pre-commit steps and the tests.
