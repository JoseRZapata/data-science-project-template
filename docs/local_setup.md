# 🛠️ Local Dev environment setup

I develop data science python projects in Linux OS or MAC OS. (For Windows OS I recommend [WSL] and run commands as Linux OS).

I setup my local development environment using the following steps:

## 💻 Computer setup to develop with Python

1. Install [Git]
      - Linux: `sudo apt-get install git`
      - MAC: `brew install git`
2. Install [Make]
      - Linux: `sudo apt-get install make`
      - MAC: `brew install make`
3. Install locally [UV] to Manage python versions, dependencies and virtual environments.
      - Linux:

        ```bash title="Install uv in Linux or MACOS"
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

        - Check the installation version executing in terminal: `uv version`

4. Install [Python] using [UV], at this time I am using Python 3.11  
      - `uv python install 3.11` # Install Python 3.11 in computer

5. In the folder of the project, set the Python version and create a virtual environment.
   1. If the project has `uv.lock` file
      - `uv sync` # Create virtual Environment and install dependencies.
      - `source .venv/bin/activate` # Activate Environment
   2.
      - `uv venv --python 3.11` # Create a Python 3.11 virtual environment
      - `source .venv/bin/activate` # Activate the Python 3.11 virtual environment
      - **Check the installation version** executing in terminal: `python --version`

**Note:** To deactivate the virtual enviroment in terminal type: `deactivate`

## 🐍 General Python tools

General Tools that I use to develop Python projects, The most important is [UV] to manage python versions, virtual environments, manage dependencies for the projects and to have tools in isolated environments, because applications runs in its own virtual environment to avoid dependencies conflicts and they are available everywhere.

[UV Highligths](https://github.com/astral-sh/uv?tab=readme-ov-file#highlights)

1. [Cruft] allows you to maintain all the necessary boilerplate for packaging and building projects separate from the code you intentionally write. Fully compatible with existing Cookiecutter templates.
      - `uv tool install cruft`
2. (optional) [Pre-commit] to local check the security of the dependencies of the project.
      - `uv tool install pip-audit`
3. (optional) [Pip-audit] to local check the security of the dependencies of the project.
      - `uv tool install pip-audit`
4. (optional) [Actionlint] to check the syntax of the GitHub Actions configuration files of the project.
      - `uv tool install actionlint`

**Note:** [UV] replace tool like [Pyenv], [Poetry] and other ones to manage the python versions, environments and dependencies.

## 📁 Start a new data science project

1. Start a new project using the [Cruft] with the [Data Science Project Template].

    ```shell title="create project"
    cruft create https://github.com/JoseRZapata/data-science-project-template
    ```

2. Answer the questions to create the project.
3. Run `make init_env` to init [Git] Or You can do the same running this commands:

    ```shell title="init environment"
        git init -b main
        git add .
        git commit -m "🎉 Begin a project, Initial commit"
    ```

4. Run `make install` to install the dependencies of the project. Or You can do the same running this commands:

    ```shell title="install dependencies"
        uv sync --all-groups
    ```

5. 🎉 Congrats Start coding your project.

6. If you want to push this repository to GitHub, first create a new repository in GitHub and then run the following commands to push your local repository to GitHub.

    ```shell title="push to GitHub"
        git remote add origin <your-repo-url>
        git branch -M main
        git push -u origin main
    ```

---
[Actionlint]: https://github.com/Mateusz-Grzelinski/actionlint-py
[Cruft]: https://cruft.github.io/cruft/
[Data Science Project Template]: https://github.com/JoseRZapata/data-science-project-template
[Git]: https://git-scm.com/
[Make]: https://www.gnu.org/software/make/manual/make.html
[Pip-audit]: https://github.com/pypa/pip-audit
[Poetry]: https://python-poetry.org/docs/
[Pre-commit]: https://pre-commit.com/
[Pyenv]: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
[Python]: https://www.python.org/downloads/
[UV]: https://docs.astral.sh/uv/
[WSL]: https://docs.microsoft.com/en-us/windows/wsl/install
