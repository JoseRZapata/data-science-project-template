# Data science project template

Template for a data science projects with software development tools

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


## How to use this project

Install Cookiecutter:
```bash
pip install cookiecutter
```

Create a project based on the template:
```bash
cookiecutter https://github.com/JoseRZapata/data-science-project-template
```

## References

- https://drivendata.github.io/cookiecutter-data-science/
- https://github.com/crmne/cookiecutter-modern-datascience
- https://github.com/khuyentran1401/data-science-template
- https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html
- https://github.com/kedro-org/kedro-starters

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[click]: https://click.palletsprojects.com/
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
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[Notebook template]: {{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[NumPy]:https://numpy.org/
[OmegaConf]: https://omegaconf.readthedocs.io/en/latest/
[Pandas]:https://pandas.pydata.org/
[pandera]:(https://pandera.readthedocs.io/en/stable/)
[pipenv]: https://pipenv.pypa.io/en/latest/
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
[tox]: https://tox.readthedocs.io/
[typeguard]: https://github.com/agronholm/typeguard
[xdoctest]: https://github.com/Erotemic/xdoctest