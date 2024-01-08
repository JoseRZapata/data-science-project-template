# {{cookiecutter.project_name}}

## Features and Tools

Features                                     | Package  | Why?
 ---                                         | ---      | ---
Dependencies and env                         | [Poetry] | [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
Project configuration file                   | [Hydra]  |  [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
Lint - Format, sort imports <br>  (Code Quality)  | [Ruff] |
Static type checking                         | [Mypy] | 
Code quality & security each commit          | [pre-commit] | 
Test code                                    | [Pytest] | 
Project Template                             | [Cruft] or [Cookiecutter] | 
Folder structure for data science projects   | [Data structure] | [article](https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71)
Template for pull requests                   | [Pull Request template] | 
Template for notebooks                       | [Notebook template] | 

## Set up the environment

1. Set up the environment:

    ```bash
    make init_env
    ```

1. Install libraries for data science and machine learning:

    ```bash
    make install_all_libs
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

[bandit]: https://github.com/PyCQA/bandit
[codecov]: https://codecov.io/
[Cookiecutter]:https://cookiecutter.readthedocs.io/stable/
[coverage.py]: https://coverage.readthedocs.io/
[Data structure]: {{cookiecutter.repo_name}}/data/README.md
[deepcheck]:https://deepcheck.io/
[dependabot]: https://github.com/dependabot/dependabot-core
[depy]:https://fpgmaas.github.io/deptry/
[DVC]:https://dvc.org/
[flake8]: https://flake8.pycqa.org/en/latest/
[furo]: https://pradyunsg.me/furo/
[github actions]: https://github.com/features/actions
[github labeler]: https://github.com/marketplace/actions/github-labeler
[hydra]: https://hydra.cc/
[Jupyter]:https://jupyter.org/
[just]:https://just.systems/man/en/
[Makefile]: https://www.gnu.org/software/make/manual/make.html
[MlFlow]:https://www.mlflow.org/
[Mypy]: http://mypy-lang.org/
[nox]: https://nox.thea.codes/
[Notebook template]: {{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[NumPy]:https://numpy.org/
[OmegaConf]: https://omegaconf.readthedocs.io/en/latest/
[Pandas]:https://pandas.pydata.org/
[pandera]:(https://pandera.readthedocs.io/en/stable/)
[Poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[Pull Request template]: {{cookiecutter.repo_name}}/pull_request_template.md
[pypi]: https://pypi.org/
[Pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[Ruff]: https://docs.astral.sh/ruff/
[safety]: https://github.com/pyupio/safety
[scikit-learn]:https://scikit-learn.org/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[testpypi]: https://test.pypi.org/
