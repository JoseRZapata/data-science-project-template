# My local Dev environment setup

I develop data science python projects in Linux OS or MAC OS. (For Windows OS I recommend [WSL] and run commands as Linux OS).

I setup my local development environment using the following steps:

## 💻 Computer setup to develop with Python

1. Install [Git]
      - Linux: `sudo apt-get install git`
      - MAC: `brew install git`
2. Install [Make]
      - Linux: `sudo apt-get install make`
      - MAC: `brew install make`
3. Install [Pyenv] and after install set up the terminal for [Pyenv] - [Link to set up](https://github.com/pyenv/pyenv?tab=readme-ov-file#set-up-your-shell-environment-for-pyenv)
      - Linux: `curl https://pyenv.run | bash`
      - MAC: `brew install pyenv`
4. Install [Python] using [Pyenv] , at this time I am using Python 3.10.13 is in security updates only.
      - `pyenv install 3.10.13` # Install Python 3.10.13 in computer
      - `pyenv global 3.10.13` # Set Python 3.10.13 as global version
5. Install locally [Pipx] to Install and Run Python Applications in Isolated Environments
      - Linux:

        ```bash title="Install pipx in Linux"
        pip install --user pipx
        python3 -m pipx ensurepath
        ```

      - MAC:

        ```bash title="Install pipx in Mac os"
        brew install pipx
        pipx ensurepath
        ```

## 🐍 General Python tools

General Tools that I use to develop Python projects, The most important is [Poetry] and all this tools are installed using [Pipx] to have this tools in isolated environments, because applications runs in its own virtual environment to avoid dependencies conflicts and they are available everywhere.

[When pipx is typically used?](https://python.land/virtual-environments/pipx#When_pipx_is_typically_used)

1. [Poetry] to manage the dependencies and the virtual environment of the project.
      - `pipx install poetry`
2. [Pip-audit] to local check the security of the dependencies of the project.
      - `pipx install pip-audit`
3. [Actionlint] to check the syntax of the GitHub Actions configuration files of the project.
      - `pipx install actionlint`
4. [Cruft] allows you to maintain all the necessary boilerplate for packaging and building projects separate from the code you intentionally write. Fully compatible with existing Cookiecutter templates.
      - `pipx install cruft`

## 📁 Start a new data science project

1. Start a new project using the [Cruft] with the [Data Science Project Template].

    ```shell title="create project"
    cruft create https://github.com/JoseRZapata/data-science-project-template
    ```

2. Answer the questions to create the project.
3. Run `make init_env` to init [Git] and [Poetry]. Or You can do the same running this commands:

    ```shell title="init environment"
        git init -b main
        poetry install
        poetry run pre-commit install
        git add .
        git commit -m "🎉 Begin a project, Initial commit"
        poetry shell
    ```

4. 🎉 Congrats Start coding your project.

---
[Actionlint]: https://github.com/Mateusz-Grzelinski/actionlint-py
[Cruft]: https://cruft.github.io/cruft/
[Data Science Project Template]: https://github.com/JoseRZapata/data-science-project-template
[Git]: https://git-scm.com/
[Make]: https://www.gnu.org/software/make/manual/make.html
[Pip-audit]: https://github.com/pypa/pip-audit
[Pipx]: https://pipx.pypa.io/stable/
[Poetry]: https://python-poetry.org/docs/
[Pyenv]: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
[Python]: https://www.python.org/downloads/
[WSL]: https://docs.microsoft.com/en-us/windows/wsl/install
