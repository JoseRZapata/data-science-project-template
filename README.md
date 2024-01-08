# Data science project template

Template for a data science projects with software development tools

## Features and Tools

Features                                     | Package
 ---                                         | ---
Dependencies and env                         | [Poetry]
Project configuration file                   | [Hydra]
Lint - Format, sort imports <br>  (Code Quality)  | [Ruff]
Static type checking                         | [Mypy]
Code quality & security each commit          | [pre-commit]
Test code                                    | [Pytest]
Project Template                             | [Cruft] or [Cookiecutter]
Folder structure for data science projects   |  [Data structure]
Template for pull requests                   | [Pull Request template]
Template for notebooks                       | [Notebook template]

## Recommendations

It is highly recommended to use a python version manager like [Pyenv] and this project is set to use [Poetry] to manage the dependencies and the environment.

1. [Install Pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
2. [Install Poetry](https://python-poetry.org/docs/#installation)

Set poetry to create the virtual enviroment inside the project’s root directory (`.venv`), in terminal run the following command:

```bash
poetry config virtualenvs.in-project true
```

## How to use this project

This can be done using [Cruft] or [Cookiecutter], if you interested to keep your project updated with the latest changes in this template, use [Cruft].

### Using Cruft

* Install Cruft:

```bash
pip install cruft
```

* Create a project based on the template:

```bash
cruft create https://github.com/JoseRZapata/data-science-project-template
```

* Update the project with the latest changes in the template:

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

## References

* <https://drivendata.github.io/cookiecutter-data-science/>
* <https://github.com/crmne/cookiecutter-modern-datascience>
* <https://github.com/khuyentran1401/data-science-template>
* <https://github.com/woltapp/wolt-python-package-cookiecutter>
* <https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html>
* <https://github.com/kedro-org/kedro-starters>

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[click]: https://click.palletsprojects.com/
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
[MlFlow]:https://www.mlflow.org/
[Mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[Notebook template]: {{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[NumPy]:https://numpy.org/
[OmegaConf]: https://omegaconf.readthedocs.io/en/latest/
[Pandas]:https://pandas.pydata.org/
[pandera]:(https://pandera.readthedocs.io/en/stable/)
[Poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[Pull Request template]: {{cookiecutter.repo_name}}/.github/pull_request_template.md
[Pyenv]: https://github.com/pyenv/pyenv
[pypi]: https://pypi.org/
[Pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[Ruff]: https://docs.astral.sh/ruff/
[safety]: https://github.com/pyupio/safety
[scikit-learn]:https://scikit-learn.org/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
[tox]: https://tox.readthedocs.io/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest
