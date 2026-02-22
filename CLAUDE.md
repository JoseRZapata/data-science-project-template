# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Cookiecutter template repository** that generates new data science projects. It is NOT a data science project itself — it's a meta-project. The actual template lives in `{{cookiecutter.repo_name}}/`, and the root-level configs manage this template repo.

Template variables are defined in `cookiecutter.json` and rendered as `{{ cookiecutter.var_name }}`. The post-generation hook (`hooks/post_gen_project.py`) conditionally removes files based on boolean options (mkdocs, codecov).

## Two-Level Structure

There are **two levels** of configuration — don't confuse them:

1. **Root level** — manages this template repository (testing, docs, CI for the template itself)
2. **`{{cookiecutter.repo_name}}/`** — the template that gets generated into new projects

Both levels have their own `pyproject.toml`, `Makefile`, `.pre-commit-config.yaml`, and `.github/workflows/`.

## Common Commands

### Template Repository (root level)
```bash
make install_env          # Install deps with uv + pre-commit
make test                 # Run template validation tests (pytest-cookies)
make test_coverage        # Generate coverage.xml
make check                # Run all pre-commit hooks
make lint                 # Run ruff linter only
make docs                 # Serve mkdocs documentation locally
make docs_test            # Test docs build
```

### Running a single test
```bash
uv run pytest tests/test_create_template.py -v
uv run pytest tests/test_create_template.py::test_run_cookiecutter_result -v
```

### Updating template dependencies to latest PyPI versions
```bash
python scripts/update_template_deps.py "{{cookiecutter.repo_name}}/pyproject.toml"
```

## Testing

Tests use **pytest-cookies** to validate template generation. They are in `tests/` and verify:
- Template bakes without errors
- Generated filenames don't contain unrendered `{{ cookiecutter.* }}` variables
- Conditional file removal works (no mkdocs, no codecov)
- Python version strings appear correctly in generated `.python-version` and `pyproject.toml`

```bash
uv run pytest tests/ -v --cov
```

## Code Quality

Config files live in `.code_quality/` (both root and template):
- **Ruff** (`.code_quality/ruff.toml`): line-length=100, target Python 3.10, includes notebooks. Rules: B, C90, E, F, W, PL, I, S, UP, RUF, SIM, TRY
- **mypy** (`.code_quality/mypy.ini`): strict mode — `disallow_untyped_defs`, `disallow_untyped_calls`, `check_untyped_defs` all enabled

Pre-commit hooks enforce: YAML validation, merge conflict check, large file check, ruff lint+format, mypy, and **commitizen** (conventional commits required).

## Generated Project Architecture

Generated projects follow the **Feature/Training/Inference (FTI) pipeline** pattern:

```
src/
├── data/                    # Data extraction, validation, processing
├── model/                   # Training, evaluation, validation, export
├── inference/               # Prediction, serving, monitoring
└── pipelines/
    ├── feature_pipeline/    # Raw data → Features & Labels
    ├── training_pipeline/   # Features & Labels → Model
    └── inference_pipeline/  # Features & Model → Predictions
```

Data follows an **8-stage convention** (from Kedro): `01_raw` → `02_intermediate` → `03_primary` → `04_feature` → `05_model_input` → `06_models` → `07_model_output` → `08_reporting`

Notebooks are numbered to match: `1-data/`, `2-exploration/`, ..., `8-reports/`

## Dependencies & Tooling

- **UV** for package management (`uv sync`, `uv add`, `uv run`)
- **Python 3.10+** (tested on 3.10, 3.11, 3.12, 3.13)
- **Conventional commits** enforced via commitizen (`feat:`, `fix:`, `docs:`, etc.)
- **Hydra** for project configuration management (`conf/config.yaml`)

## Template Conditional Rendering

The template `pyproject.toml` uses Jinja2 comments for conditionals:
```toml
#{% if cookiecutter.mkdocs %}
docs = [...]
#{% endif %}
```

Files in `_copy_without_render` (listed in `cookiecutter.json`) are copied as-is without Jinja2 processing — this includes `.code_quality/`, `.vscode/`, `src/`, `tests/`, `data/`, and `.pre-commit-config.yaml`.

## CI/CD Workflows

Root-level (`.github/workflows/`):
- `ci.yml` — runs pre-commit + pytest on PRs and pushes to main
- `docs.yml` — deploys mkdocs to GitHub Pages on merge
- `pre-commit_autoupdate.yml` — weekly auto-update of hooks
- `update_template_deps.yml` — auto-update template dependencies
- `dependency-review.yml`, `automerge.yml`, `labels.yml`, `pr-labeler.yml`
