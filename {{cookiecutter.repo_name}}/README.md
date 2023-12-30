# {{cookiecutter.project_name}}

## Features and Tools

Features              | Description
 ---                  | ---
[Poetry]              | Manage packages and virtual enviroment
[Hydra]               | Manage configuration files
[Ruff]                | Code quality (Linting, formatting)
[Mypy]                | Static type checking
[Pre-commit]          | Automate code reviewing and formatting
[Pytest]              | Test code
[Cookiecutter]        | Create project from template
[Data structure]      | Data structure convention for data science projects
[Pull Request template] | Template for pull requests
[Notebook template]     | Template for notebooks


## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make env 
```

## Install dependencies
To install all dependencies for this project, run:
```bash
poetry install
```

To install a new package, run:
```bash
poetry add <package-name>
```