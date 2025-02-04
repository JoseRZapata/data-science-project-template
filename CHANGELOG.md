# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [Released]

## [1.0.0] - 2024-01-07

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
