#!/usr/bin/env python
import os
import shutil
import subprocess  # nosec

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file from project directory.

    Args:
        filepath (str): File path relative to project directory.
    """
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    """Remove directory from project directory.

    Args:
        filepath (str): Directory path relative to project directory.
    """
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    mkdocs = "{% if cookiecutter.mkdocs %}y{% endif %}"
    codecov = "{% if cookiecutter.codecov%}y{% endif %}"

    if mkdocs != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")
        remove_file(".github/workflows/docs.yml")

    if codecov != "y":
        remove_file("codecov.yml")

    # check if repo is already initialized using `git status`
    # if not, initialize the repo and make initial commit
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )  # nosec
    except subprocess.CalledProcessError:
        # We are not in a git repo
        subprocess.run(["echo", "Initializing git"], check=False)  # nosec
        subprocess.run(["git", "init", "-b", "main"], check=False)  # nosec
        subprocess.run(["git", "add", "."], check=False)  # nosec
        subprocess.run(["git", "commit", "-m", "🎉 Initial commit"], check=False)  # nosec
        subprocess.run(["echo", "🎉 Project Already created!"], check=False)  # nosec
