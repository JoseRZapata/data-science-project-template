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

    text_msg = """
    Install Make and run the following commands to set git and enviroment:
    🎉 Init git track: make init_git
    🎉 Init Enviroment: make init_env
    """
    subprocess.run(["echo", text_msg], check=False)  # nosec
