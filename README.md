# Data science project template

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Template for a data science projects with software development tools

---

Table of Contents

<!-- toc -->

- [Data science project template](#data-science-project-template)
  - [:tada: Creating a New Project](#tada-creating-a-new-project)
  - [:link: Linking an Existing Project](#link-linking-an-existing-project)
  - [:sparkles: Features](#sparkles-features)
    - [:rocket: Project Standardization and Automation](#rocket-project-standardization-and-automation)
      - [:hammer: Developer Workflow Automation](#hammer-developer-workflow-automation)
      - [:seedling: Conditionally Rendered Python Package or Project Boilerplate](#seedling-conditionally-rendered-python-package-or-project-boilerplate)
    - [:wrench: Maintainability](#wrench-maintainability)
      - [:label: Type Checking and Data Validation](#label-type-checking-and-data-validation)
      - [:white\_check\_mark: Testing/Coverage](#white_check_mark-testingcoverage)
      - [:rotating\_light: Linting](#rotating_light-linting)
      - [:construction\_worker: CI/CD](#construction_worker-cicd)
  - [:chart\_with\_downwards\_trend: Observability](#chart_with_downwards_trend-observability)
      - [:loud\_sound: Logging](#loud_sound-logging)
      - [:goal\_net: Error Tracking](#goal_net-error-tracking)
  - [:lock: Security](#lock-security)
      - [:lock\_with\_ink\_pen: Static Application Security Testing (SAST)](#lock_with_ink_pen-static-application-security-testing-sast)
  - [:clipboard: Accessibility](#clipboard-accessibility)
      - [:memo: Project Documentation](#memo-project-documentation)
      - [:ballot\_box\_with\_check: Design Documentation and Production Deployment Checklists](#ballot_box_with_check-design-documentation-and-production-deployment-checklists)
      - [:card\_file\_box: Architecture Documentation](#card_file_box-architecture-documentation)
  - [:sparkles: Features and Tools](#sparkles-features-and-tools)
  - [Recommendations](#recommendations)
  - [:tada: Create a new project](#tada-create-a-new-project)
    - [Using Cruft](#using-cruft)
    - [Using Cookiecutter](#using-cookiecutter)
  - [:card\_file\_box: Project structure](#card_file_box-project-structure)
  - [References](#references)

<!-- tocstop -->

## :tada: Creating a New Project

Via [`cruft`](https://cruft.github.io/cruft/) (recommended):

```shell script
pip install --user cruft # Install `cruft` on your path for easy access
cruft create https://github.com/JoseRZapata/data-science-project-template
```

Via [`cookiecutter`](https://github.com/audreyr/cookiecutter):

```shell script
pip install --user cookiecutter # Install `cookiecutter` on your path for easy access
cookiecutter gh:JoseRZapata/data-science-project-template
```

Note: **_Cookiecutter_** uses `gh:` as short-hand for `https://github.com/`

## :link: Linking an Existing Project

If the project was originally installed via
[`cookiecutter`](https://github.com/audreyr/cookiecutter), you must first use
[`cruft`](https://cruft.github.io/cruft/) to link the project with the original
template:

```shell script
cruft link https://github.com/JoseRZapata/data-science-project-template
```

Then/else:

```shell script
cruft update
```

## :sparkles: Features

### :rocket: Project Standardization and Automation

#### :hammer: Developer Workflow Automation

- Python packaging and dependency management
  with [Poetry](https://python-poetry.org/)
- Project workflow orchestration
  with [Make](https://www.gnu.org/software/make/)
  as an [interface shim](https://en.wikipedia.org/wiki/Shim_(computing))
  - Self-documenting [Makefile](./{{cookiecutter.project_slug}}/Makefile); just type
      `make` on the command line to display auto-generated documentation on available
      targets:

<video width="720" height="540"
src="https://user-images.githubusercontent.com/13070236/207501188-98af2617-14f1-4b02-8c14-bac86598e25b.mov"
type="video/mp4"
controls autoplay loop></video>

- Automated Cookiecutter template synchronization
  with [cruft](https://cruft.github.io/cruft/)
- Test automation
  with [Tox](https://tox.readthedocs.io/en/latest/)
- Code quality tooling automation and management
  with [pre-commit](https://pre-commit.com/)
- Continuous integration and deployment
  with [GitHub Actions](https://github.com/features/actions)

#### :seedling: Conditionally Rendered Python Package or Project Boilerplate

- [Optional] Command-line interface boilerplate
  with [Typer](https://typer.tiangolo.com/)
- Project-specific [Docker](https://www.docker.com/) image
  Dockerfile[^1] with production dependencies for a
  completely reproducible execution environment
- [Optional] [Jupyter](https://jupyter.org/) support[^1]


### :wrench: Maintainability

#### :label: Type Checking and Data Validation

- Static type-checking
  with [Mypy](http://mypy-lang.org)[^2]
- Run-time type-checking
  with [Typeguard](https://github.com/agronholm/typeguard)
  - See the
    [Typeguard user guide](https://typeguard.readthedocs.io/en/latest/userguide.html?highlight=@typechecked#using-the-decorator)
    for usage overview

> :fire: **Tip**
> Complementary to type-checking, function-specific input validation is another useful
> technique. This helps eliminate an _implicit knowledge violation_ from
> **_hidden argument requirements_**:
>
>  "**_Hidden argument requirements_** occur when a method signature implies a wider range of
>  valid inputs than the method actually accepts. For example, accepting an int while
>  only allowing numbers 1 to 10 is a hidden constraint." [1]
>
>  [1] C. Riccomini and D. Ryaboy, The Missing README: A Guide for the New Software
>  Engineer, Paperback. No Starch Press, 2021.

#### :white_check_mark: Testing/Coverage

- Testing
  with [`pytest`](https://docs.pytest.org/en/latest/)
- Doctests
  with [`xdoctest`](https://xdoctest.readthedocs.io)[^2]
- [Performance testing](https://en.wikipedia.org/wiki/Software_performance_testing)
  with [`pytest-benchmark`](https://pytest-benchmark.readthedocs.io/en/stable/index.html)
- [Property-based testing](https://hypothesis.works/articles/what-is-property-based-testing/)
  with [Hypothesis](https://github.com/HypothesisWorks/hypothesis)
- [Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)
  with [mutmut](https://github.com/boxed/mutmut)

> :information_source: **Info**
>  For a good overview of how property-based testing and mutation testing
>  work together to improve the value and quality of your tests, see
>  [this stackoverflow post](https://stackoverflow.com/a/38704078/6470891)
>  and the
>  [follow-up by the `mutmut` author](https://stackoverflow.com/a/61849772/6470891).

- Code coverage
  with [Coverage.py](https://coverage.readthedocs.io/)
- Coverage reporting
  with [Codecov](https://codecov.io/)

#### :rotating_light: Linting

- Code quality:
  - [Ruff](https://github.com/charliermarsh/ruff)
    - A blazing-fast (10x-100x faster) replacement for
        [Pylint](https://github.com/PyCQA/pylint),
        [Flake8](https://github.com/PyCQA/flake8) (including major plugins),
        and more under a single, common interface
  - [`hadolint`](https://github.com/hadolint/hadolint)
  - [Pylint](https://github.com/PyCQA/pylint)[^2][^3]
  - [ShellCheck](https://github.com/koalaman/shellcheck)
- Code formatting:
  - [Black](https://github.com/psf/black)[^2]
  - [isort](https://github.com/timothycrosley/isort)[^2][^3]
  - [`pyupgrade`](https://github.com/asottile/pyupgrade)[^2][^3]
  - [`shfmt`](https://github.com/mvdan/sh)
    - Configured by default to align with [Google's Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- General file formatting:
  - [`end-of-file-fixer`](https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer)
  - [`pretty-format-json`](https://github.com/pre-commit/pre-commit-hooks#pretty-format-json)
  - (trim) [`trailing-whitespace`](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)
- Unsanitary commits:
  - Secrets
    with [`detect-secrets`](https://github.com/Yelp/detect-secrets)
  - Debugger imports and py37+ `breakpoint()` calls
    with [`debug-statements`](https://github.com/pre-commit/pre-commit-hooks#debug-statements)
  - Large files
    with [`check-added-large-files`](https://github.com/pre-commit/pre-commit-hooks#check-added-large-files)
  - Invalid Python files
    with [`check-ast`](https://github.com/pre-commit/pre-commit-hooks#check-ast)

#### :construction_worker: CI/CD

- Dependency updates
  with [Dependabot](https://dependabot.com/)
  - Automated [Dependabot](https://dependabot.com/) PR merging
    with the [Dependabot Auto Merge GitHub Action](https://github.com/ahmadnassri/action-dependabot-auto-merge)[^4]

## :chart_with_downwards_trend: Observability

#### :loud_sound: Logging

- [Structured logging](https://stripe.com/blog/canonical-log-lines)
  with [`structlog-sentry-logger`](https://github.com/TeoZosa/structlog-sentry-logger)
  (via [`structlog`](https://www.structlog.org/en/stable/))
  - Granular control flow context logging (via call stack introspection):
    - Namespaced module-specific loggers
    - Function name logging
  - Environment-dependent standard output stream log formatting:
    - Production: JSON logs
    - Development: Colorized human-readable logs, with JSON logs saved
      locally for retrospective analysis
  - [Optional] Exception logging to Sentry with
    [`structlog-sentry`](https://github.com/kiwicom/structlog-sentry)

#### :goal_net: Error Tracking

- [Optional] Exception monitoring
  with [Sentry](https://sentry.io/welcome/)
  - see: the [cookiecutter's `.env` file]({{cookiecutter.project_slug}}/.env)
    for a detailed activation guide

## :lock: Security


#### :lock_with_ink_pen: Static Application Security Testing (SAST)

- Code vulnerabilities
  with [Bandit](https://github.com/PyCQA/bandit)[^2]
- Python package dependencies vulnerabilities
  with [Safety](https://github.com/pyupio/safety)

## :clipboard: Accessibility

#### :memo: Project Documentation

- Documentation building
  with [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
  - Rich automatic documentation from type annotations and docstrings (NumPy, Google,
    etc.)
    with [`sphinx-autoapi`](https://github.com/readthedocs/sphinx-autoapi)
  - Automated emoji shortcode conversion[^5]
- Docstring coverage
  with [`interrogate`](https://interrogate.readthedocs.io/)
- Automated README table of contents generation
  with [`markdown-toc`](https://github.com/Lucas-C/pre-commit-hooks-nodejs)
- Publishing to [Confluence](https://www.atlassian.com/software/confluence)
  with [Atlassian Confluence Builder for Sphinx](https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/)

#### :ballot_box_with_check: Design Documentation and Production Deployment Checklists

- Production service design documentation and deployment checklist templates
  with [Mercari's `production-readiness-checklist`](https://github.com/mercari/production-readiness-checklist)

#### :card_file_box: Architecture Documentation

- [Optional] Architecture knowledge management
  with [Log4brains](https://github.com/thomvaill/log4brains) to systematically
  facilitate and record the planning process and context for each of a software system's
  architectural changes that occur over time and their consequences.
  - See: [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
    for an overview on [Architecture Decision Records (ADR)](https://github.com/joelparkerhenderson/architecture_decision_record)

[^1]: Conditionally rendered based on the configurations specified in the project setup phase to avoid tooling bloat

[^2]: Jupyter notebook compatibility via [nbQA](https://github.com/nbQA-dev/nbQA)

[^3]: Via [`ruff`](https://github.com/charliermarsh/ruff)

[^4]: Requires definitions of one or more of the below repository secrets:
  AUTO_MERGE_DEPENDABOT_TOKEN
  DOCKERHUB_TOKEN
  DOCKERHUB_USERNAME
  PYPI_TOKEN
  TEST_PYPI_TOKEN

---

## :sparkles: Features and Tools

Features                                     | Package  | Why?
 ---                                         | ---      | ---
Dependencies and env                         | [Poetry] | [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
Project configuration file                   | [Hydra]  |  [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
Lint - Format, sort imports  (Code Quality)  | [Ruff] |
Static type checking                         | [Mypy] |
code security                                | [bandit] |
Code quality & security each commit          | [pre-commit] |
Test code                                    | [Pytest] |
Test coverage                                | [coverage.py] |
Documentation                                | [mkdocs] |
Project Template                             | [Cruft] or [Cookiecutter] |
Folder structure for data science projects   | [Data structure] | [article](https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71)
Template for pull requests                   | [Pull Request template] |
Template for notebooks                       | [Notebook template] |

## Recommendations

It is highly recommended to use a python version manager like [Pyenv] and this project is set to use [Poetry] to manage the dependencies and the environment.

1. [Install Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. [Install Poetry](https://python-poetry.org/docs/#installation)

Set poetry to create the virtual enviroment inside the project’s root directory (`.venv`), in terminal run the following command:

```bash
poetry config virtualenvs.in-project true
```

## :tada: Create a new project

This can be done using [Cruft] or [Cookiecutter], if you interested to keep your project updated with the latest changes in this template, use [Cruft].

### Using Cruft

- Install Cruft:

```bash
pip install cruft
```

- Create a project based on the template:

```bash
cruft create https://github.com/JoseRZapata/data-science-project-template
```

- Update the project with the latest changes in the template:

In the terminal, go to the root of the project where the `.cruft.json` file is located and run:

```bash
cruft update
```

### Using Cookiecutter

Install Cookiecutter:

```bash
pip install cookiecutter
```

Create a project based on the template:

```bash
cookiecutter gh:JoseRZapata/data-science-project-template
```

## :card_file_box: Project structure

```bash
.
├── codecov.yml                         # configuration for codecov
├── .code_quality
│   ├── bandit.yaml                     # bandit configuration
│   ├── mypy.ini                        # mypy configuration
│   └── ruff.toml                       # ruff configuration
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
├── .editorconfig                       # editor configuration
├── .github                             # github configuration
│   ├── actions
│   │   └── python-poetry-env
│   │       └── action.yml              # github action to setup python environment
│   ├── pull_request_template.md        # template for pull requests
│   └── workflows
│       ├── dependencies.yml            # github action to update dependencies
│       ├── pre-commit_autoupdate.yml   # github action update pre-commit hooks
│       └── test.yml
├── .gitignore                          # files to ignore in git
├── Makefile                            # useful commands to setup environment,
├── models                              # store final models
├── notebooks
│   ├── 1-data                          # notebooks for data extraction and cleaning
│   ├── 2-exploration                   # notebooks for data exploration
│   ├── 3-analysis                      # notebooks for data analysis
│   ├── 4-feat_eng                      # notebooks for feature engineering
│   ├── 5-models                        # notebooks for model training
│   ├── 6-evaluation                    # notebooks for model evaluation
│   ├── 7-deploy                        # notebooks for model deployment
│   ├── notebook_template.ipynb         # template for notebooks
│   └── README.md                       # information about the notebooks
├── .pre-commit-config.yaml             # configuration for pre-commit hooks
├── pyproject.toml                      # dependencies for poetry
├── README.md                           # description of your project
├── src                                 # source code for use in this project
├── tests                               # test code for your project
└── .vscode                             # vscode configuration
    ├── extensions.json                 # list of recommended extensions
    └── settings.json                   # vscode settings
```

## References

- <https://drivendata.github.io/cookiecutter-data-science/>
- <https://github.com/crmne/cookiecutter-modern-datascience>
- <https://github.com/khuyentran1401/data-science-template>
- <https://github.com/woltapp/wolt-python-package-cookiecutter>
- <https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html>
- <https://github.com/TeoZosa/cookiecutter-cruft-poetry-tox-pre-commit-ci-cd>
- <https://github.com/kedro-org/kedro-starters>

[bandit]: https://github.com/PyCQA/bandit
[codecov]: https://codecov.io/
[Cookiecutter]:https://cookiecutter.readthedocs.io/stable/
[coverage.py]: https://coverage.readthedocs.io/
[Cruft]: https://cruft.github.io/cruft/
[Data structure]: {{cookiecutter.repo_name}}/data/README.md
[deepcheck]:https://deepcheck.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[depy]:https://fpgmaas.github.io/deptry/
[DVC]:https://dvc.org/
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[hydra]: https://hydra.cc/
[Jupyter]:https://jupyter.org/
[just]:https://just.systems/man/en/
[Makefile]: https://www.gnu.org/software/make/manual/make.html
[mkdocs]: https://www.mkdocs.org/
[MlFlow]:https://www.mlflow.org/
[Mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[Notebook template]: {{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[NumPy]:https://numpy.org/
[OmegaConf]: https://omegaconf.readthedocs.io/en/latest/
[Pandas]:https://pandas.pydata.org/
[pandera]:(https://pandera.readthedocs.io/en/stable/)
[Poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[Pull Request template]: {{cookiecutter.repo_name}}/.github/pull_request_template.md
[Pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.org/
[Pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[Ruff]: https://docs.astral.sh/ruff/
[safety]: https://github.com/pyupio/safety
[scikit-learn]:https://scikit-learn.org/
[testpypi]: https://test.pypi.org/
[tox]: https://tox.readthedocs.io/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
