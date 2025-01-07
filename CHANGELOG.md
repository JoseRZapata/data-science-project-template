# Changelog

## [0.2.0] - 2024-01-07

The Main change in this Pull Request is the migration from poetry to uv to manage the dependencies and the environment of the project.

### 💥 Breaking Changes

- `pyproject.toml` has been change to uses [UV](https://docs.astral.sh/uv/) and the standards in PEP, so is not compatible with **poetry anymore**.
- `Makefile` has been updated to use `uv` instead of `poetry` in the scripts.

### 🚀 Features

- [UV](https://docs.astral.sh/uv/) has been added to the project to manage the dependencies and the environment of the project.

### 🔥 Removals and Deprecations

- `poetry.lock` has been removed from the project.

### 🐞 Fixes

- Fix ci.yaml to use `uv`, pre-commit steps and the tests.

### 🐎 Performance

- Project install dependencies faster using `uv` instead of `poetry`.

### 🚨 Testing

- add python 3.12 to the testing matrix.

### 👷 Continuous Integration

- update the CI to use `uv` instead of `poetry` in:
    - `ci.yaml` workflow
    - `docs.yaml`workflow

### 📚 Documentation

- Update the documentation to use `uv` instead of `poetry` in:
    - `docs/setup_tokens.md`
    - `docs/pre-commit.md`
    - `docs/local_setup.md`
- Update the `README.md` to use `uv` instead of `poetry`.

### 🔨 Refactoring

- Refactor the `Makefile` to use `uv` instead of `poetry` in the scripts.
- Refactor the `pyproject.toml` to use `uv` instead of `poetry`.
- Refactor github actions to use `uv` instead of `poetry` in the scripts.

### 💄 Style

- Format the code using `Ruff` in all files

### 📦 Dependencies

- Add `uv.lock` to the project dependencies.
