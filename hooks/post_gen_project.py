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


mkdocs = "{% if cookiecutter.mkdocs %}y{% endif %}"
codecov = "{% if cookiecutter.codecov%}y{% endif %}"

if mkdocs != "y":
    remove_dir("docs")
    remove_file("mkdocs.yml")
    remove_file(".github/workflows/docs.yml")
if codecov != "y":
    remove_file("codecov.yml")


if not os.path.exists(".cruft.json"):
    text_msg = """
    Install \033[1;32m Make \033[0m and run next steps to set git and environment:

    🎉 Init git in local: \033[1;32m make init_git \033[0m
    🎉 Init Environment: \033[1;32m make init_env \033[0m
    """
    subprocess.run(["echo", "-e", text_msg], check=False)  # nosec
