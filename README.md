# Data science project template

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pages-build-deployment](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/pages/pages-build-deployment)
[![CI](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JoseRZapata/data-science-project-template/graph/badge.svg?token=7LCPX574UF)](https://codecov.io/gh/JoseRZapata/data-science-project-template)

---

A modern template for data science projects with all the necessary tools for experiment, development, testing, and deployment. From notebooks to production.

✨📚✨ Documentation: <https://joserzapata.github.io/data-science-project-template/>

Source Code: <https://github.com/JoseRZapata/data-science-project-template>

---

## Features

<!-- features-begin -->

- Dependency management with [UV]
- Virtual environment management with [UV]
- Linting with [pre-commit] and [Ruff]
- Continuous integration with [GitHub Actions]
- Documentation with [mkdocs] and [mkdocstrings] using the [mkdocs-material](https://github.com/squidfunk/mkdocs-material)theme
- Automated dependency updates with [Dependabot]
- Code formatting with [Ruff]
- Import sorting with [Ruff] using isort rule.
- Testing with [pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]
- Static type-checking with [mypy]
- Security audit with [Ruff] using bandit rule.
- Manage project labels with [GitHub Labeler]

---
Table of Contents
<!-- markdownlint-disable MD007 -->
- [Data science project template](#data-science-project-template)
  - [Features](#features)
  - [📁 Creating a New Project](#-creating-a-new-project)
    - [👍 Recommendations](#-recommendations)
    - [🍪🥇 Via Cruft - (**recommended**)](#-via-cruft---recommended)
    - [🍪 Via Cookiecutter](#-via-cookiecutter)
  - [🔗  Linking an Existing Project](#--linking-an-existing-project)
  - [🗃️ Project structure](#️-project-structure)
  - [✨ Features and Tools](#-features-and-tools)
    - [🚀 Project Standardization and Automation](#-project-standardization-and-automation)
      - [🔨 Developer Workflow Automation](#-developer-workflow-automation)
      - [🌱 Conditionally Rendered Python Package or Project Boilerplate](#-conditionally-rendered-python-package-or-project-boilerplate)
    - [🔧 Maintainability](#-maintainability)
      - [🏷️  Type Checking and Data Validation](#️--type-checking-and-data-validation)
      - [✅ 🧪 Testing/Coverage](#--testingcoverage)
      - [🚨 Linting](#-linting)
        - [🔍 Code quality](#-code-quality)
        - [🎨 Code formatting](#-code-formatting)
      - [👷 CI/CD](#-cicd)
        - [Automatic Dependency updates](#automatic-dependency-updates)
        - [Dependency Review in PR](#dependency-review-in-pr)
        - [Pre-commit automatic updates](#pre-commit-automatic-updates)
  - [🔒 Security](#-security)
    - [🔏 Static Application Security Testing (SAST)](#-static-application-security-testing-sast)
  - [⌨️ Accessibility](#️-accessibility)
    - [🔨 Automation tool (Makefile)](#-automation-tool-makefile)
    - [📝 Project Documentation](#-project-documentation)
    - [🗃️ Templates](#️-templates)
    - [Good practices](#good-practices)
  - [References](#references)
<!-- markdownlint-enable MD007 -->
## 📁 Creating a New Project

### 👍 Recommendations

It is highly recommended to use managers for the python versions, dependencies and virtual environments.

This project uses [UV], a extremely fast tool to replace [pip](https://pip.pypa.io/en/stable/), pip-tools, [Pipx], [Poetry], [Pyenv], twine, [virtualenv](https://virtualenv.pypa.io/en/latest/), and more.

🌟 Check how to setup your environment: <https://joserzapata.github.io/data-science-project-template/local_setup/>

### 🍪🥇 Via [Cruft] - (**recommended**)

```bash title="install cruft"
# Install cruft in a isolated environment using uv

uv tool install cruft 

# Or Install with pip

pip install --user cruft # Install `cruft` on your path for easy access
```

```shell title="create project"
cruft create https://github.com/JoseRZapata/data-science-project-template
```

then inside the project folder, init git and uv environment using [Make]:

```shell title="install project"
make init_git
make install_env
source .venv/bin/activate
```

### 🍪 Via [Cookiecutter]

```shell title="install cookiecutter"

uv tool install cookiecutter # Install cruft in a isolated environment

# Or Install with pip

pip install --user cookiecutter # Install `cookiecutter` on your path for easy access
```

```shell title="create project"
cookiecutter gh:JoseRZapata/data-science-project-template
```

Note: **_Cookiecutter_** uses `gh:` as short-hand for `https://github.com/`

## 🔗  Linking an Existing Project

If the project was originally installed via [Cookiecutter], you must first use [Cruft] to link the project with the original template:

```shell
cruft link https://github.com/JoseRZapata/data-science-project-template
```

Then/else:

```shell
cruft update
```

## 🗃️ Project structure

Folder structure for data science projects  [why?](https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71)

- [Data structure](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
- [Pipelines based on Feature/Training/Inference Pipelines](https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines)

```bash
.
├── .code_quality
│   ├── mypy.ini                        # mypy configuration
│   └── ruff.toml                       # ruff configuration
├── .github                             # github configuration
│   ├── actions
│   │   └── python-poetry-env
│   │       └── action.yml              # github action to setup python environment
│   ├── dependabot.md                   # github action to update dependencies
│   ├── pull_request_template.md        # template for pull requests
│   └── workflows                       # github actions workflows
│       ├── ci.yml                      # run continuous integration (tests, pre-commit, etc.)
│       ├── dependency_review.yml       # review dependencies
│       ├── docs.yml                    # build documentation (mkdocs)
│       └── pre-commit_autoupdate.yml   # update pre-commit hooks
├── .vscode                             # vscode configuration
|   ├── extensions.json                 # list of recommended extensions
|   ├── launch.json                     # vscode launch configuration
|   └── settings.json                   # vscode settings
├── conf                                # folder configuration files
│   └── config.yaml                     # main configuration file
├── data
│   ├── 01_raw                          # raw immutable data
│   ├── 02_intermediate                 # typed data
│   ├── 03_primary                      # domain model data
│   ├── 04_feature                      # model features
│   ├── 05_model_input                  # often called 'master tables'
│   ├── 06_models                       # serialized models
│   ├── 07_model_output                 # data generated by model runs
│   ├── 08_reporting                    # reports, results, etc
│   └── README.md                       # description of the data structure
├── docs                                # documentation for your project
│   ├── index.md                        # documentation homepage
├── models                              # store final models
├── notebooks
│   ├── 1-data                          # data extraction and cleaning
│   ├── 2-exploration                   # exploratory data analysis (EDA)
│   ├── 3-analysis                      # Statistical analysis, hypothesis testing.
│   ├── 4-feat_eng                      # feature engineering (creation, selection, and transformation.)
│   ├── 5-models                        # model training, evaluation and hyperparameter tuning.
│   ├── 6-interpretation                # model interpretation
│   ├── 7-deploy                        # model packaging, deployment strategies.
│   ├── 8-reports                       # story telling, summaries and analysis conclusions.
│   ├── notebook_template.ipynb         # template for notebooks
│   └── README.md                       # information about the notebooks
├── src                                 # source code for use in this project
│   ├── README.md                       # description of src structure
│   ├── tmp_mock.py                     # example python file
│   ├── data                            # data extraction, validation, processing, transformation
│   ├── model                           # model training, evaluation, validation, export
│   ├── inference                       # model prediction, serving, monitoring
│   └── pipelines                       # orchestration of pipelines
│       ├── feature_pipeline            # transforms raw data into features and labels
│       ├── training_pipeline           # transforms features and labels into a model
│       └── inference_pipeline          # takes features and a trained model for predictions
├── tests                               # test code for your project
│   ├── test_mock.py                    # example test file
│   ├── data                            # tests for data module
│   ├── model                           # tests for model module
│   ├── inference                       # tests for inference module
│   └── pipelines                       # tests for pipelines module
├── .editorconfig                       # editor configuration
├── .gitignore                          # files to ignore in git
├── .pre-commit-config.yaml             # configuration for pre-commit hooks
├── codecov.yml                         # configuration for codecov
├── Makefile                            # useful commands to setup environment, run tests, etc.
├── mkdocs.yml                          # configuration for mkdocs documentation
├── pyproject.toml                      # dependencies and configuration project file
├── uv.lock                             # locked dependencies
└── README.md                           # description of your project    
```

## ✨ Features and Tools

### 🚀 Project Standardization and Automation

#### 🔨 Developer Workflow Automation

- Python packaging, dependency management and environment management
  with [UV] - [`why use a management, (uv is a replacement for poetry)`](https://codecut.ai/poetry-a-better-way-to-manage-python-dependencies/)
- Project workflow orchestration
  with [Make] as an [interface shim](https://en.wikipedia.org/wiki/Shim_(computing))
    - Self-documenting [Makefile](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/Makefile); just type
      `make` on the command line to display auto-generated documentation on available
      targets:
- Automated Cookiecutter template synchronization with [Cruft] - [`why?`](https://careers.wolt.com/en/blog/tech/project-template-for-modern-python-packages)
- Code quality tooling automation and management with [pre-commit]
- Continuous integration and deployment with [GitHub Actions]
- Project configuration files  with [Hydra] - [`why?`](https://codecut.ai/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)

#### 🌱 Conditionally Rendered Python Package or Project Boilerplate

- _Optional:_ [Jupyter] support

### 🔧 Maintainability

#### 🏷️  Type Checking and Data Validation

- Static type-checking with [Mypy]

#### ✅ 🧪 Testing/Coverage

- Testing with [Pytest]
- Code coverage with [Coverage.py]
- Coverage reporting with [Codecov]

#### 🚨 Linting

##### 🔍 Code quality

- [Ruff] An extremely fast (10x-100x faster) Python linter and code formatter, written in Rust.
    - Replacement for ~~[Pylint]~~, ~~[Flake8]~~ (including major plugins) and more linters under a single, common interface
- [ShellCheck](https://github.com/koalaman/shellcheck)
- Unsanitary commits:
    - Secrets with [`detect-secrets`](https://github.com/Yelp/detect-secrets)
    - Large files with [`check-added-large-files`](https://github.com/pre-commit/pre-commit-hooks#check-added-large-files)
    - Files that contain merge conflict strings.[check-merge-conflict](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#check-merge-conflict)

##### 🎨 Code formatting

- [Ruff] An extremely fast (10x-100x faster) Python linter and code formatter, written in Rust.
    - Replacement for ~~[Black]~~, ~~[isort]~~, ~~[pyupgrade]~~ and more formatters under a single, common interface

- General file formatting:
    - [`end-of-file-fixer`](https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer)
    - [`pretty-format-json`](https://github.com/pre-commit/pre-commit-hooks#pretty-format-json)
    - (trim) [`trailing-whitespace`](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)
    - [`check-yaml`](https://github.com/pre-commit/pre-commit-hooks#check-yaml)

#### 👷 CI/CD

##### Automatic Dependency updates

- Dependency updates with [Dependabot], Automated [Dependabot] PR merging with the [Dependabot Auto Merge GitHub Action](https://github.com/ahmadnassri/action-dependabot-auto-merge)

- This is a replacement for [pip-audit](https://github.com/pypa/pip-audit) , _In your local environment, If you want to check for vulnerabilities in your dependencies you can use [pip-audit]_.

##### Dependency Review in PR

- Dependency Review  with [dependency-review-action], This action scans your pull requests for dependency changes, and will raise an error if any vulnerabilities or invalid licenses are being introduced.

##### Pre-commit automatic updates

- Automatic updates with [GitHub Actions] workflow `.github/workflows/pre-commit_autoupdate.yml`

## 🔒 Security

### 🔏 Static Application Security Testing (SAST)

- Code vulnerabilities with [Bandit] using [Ruff]

## ⌨️ Accessibility

### 🔨 Automation tool (Makefile)

Makefile to automate the setup of your environment, the installation of dependencies, the execution of tests, etc.
in terminal type `make` to see the available commands

```bash
Target                Description
-------------------   ----------------------------------------------------
check                 Run code quality tools with pre-commit hooks.
docs_test             Test if documentation can be built without warnings or errors
docs_view             Build and serve the documentation
init_env              Install dependencies with uv and activate env
init_git              Initialize git repository
install_data_libs     Install pandas, scikit-learn, Jupyter, seaborn
pre-commit_update     Update pre-commit hooks
test                  Test the code with pytest and coverage
```

### 📝 Project Documentation

- Documentation building
  with [MkDocs] - [Tutorial](https://realpython.com/python-project-documentation-with-mkdocs/)
    - Powered by [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
    - Rich automatic documentation from type annotations and docstrings (NumPy, Google, etc.)
    with [mkdocstrings]

### 🗃️ Templates

- [Pull Request template]
- [Notebook template]

### Good practices

- <https://www.conventionalcommits.org/>
- <https://keepachangelog.com/>

---

## References

- <https://drivendata.github.io/cookiecutter-data-science/>
- <https://github.com/crmne/cookiecutter-modern-datascience>
- <https://github.com/fpgmaas/cookiecutter-poetry>
- <https://github.com/khuyentran1401/data-science-template>
- <https://github.com/woltapp/wolt-python-package-cookiecutter>
- <https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html>
- <https://github.com/TeoZosa/cookiecutter-cruft-poetry-tox-pre-commit-ci-cd>
- <https://github.com/cjolowicz/cookiecutter-hypermodern-python>
- <https://github.com/gotofritz/cookiecutter-gotofritz-poetry>
- <https://github.com/kedro-org/kedro-starters>

---

[Bandit]: https://github.com/PyCQA/bandit
[Black]: https://github.com/psf/black
[Codecov]: https://codecov.io/
[Cookiecutter]:https://cookiecutter.readthedocs.io/en/stable/
[Coverage.py]: https://coverage.readthedocs.io/
[Cruft]: https://cruft.github.io/cruft/
[Dependabot]: https://github.com/dependabot/dependabot-core
[dependency-review-action]: https://github.com/actions/dependency-review-action
[Flake8]:https://github.com/PyCQA/flake8
[GitHub Actions]: https://github.com/features/actions
[Github Labeler]: https://github.com/marketplace/actions/github-labeler
[hydra]: https://hydra.cc/
[isort]: https://github.com/PyCQA/isort
[Jupyter]: https://jupyter.org/
[Make]: https://www.gnu.org/software/make/manual/make.html
[mkdocs]: https://www.mkdocs.org/
[mkdocstrings]: https://mkdocstrings.github.io/
[Mypy]: http://mypy-lang.org/
[Notebook template]: https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[Pipx]:https://pipx.pypa.io/stable/
[Poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[Pull Request template]: https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/pull_request_template.md
[Pyenv]:https://github.com/pyenv/pyenv
[Pylint]:https://github.com/PyCQA/pylint
[Pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[Ruff]: https://docs.astral.sh/ruff/
[UV]: https://docs.astral.sh/uv/
