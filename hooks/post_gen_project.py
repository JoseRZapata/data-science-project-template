#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


mkdocs = "y"
codecov = "y"

mkdocs = '{% if cookiecutter.mkdocs != "y" %}n{% endif %}'
codecov = '{% if cookiecutter.codecov != "y" %}n{% endif %}'

if __name__ == "__main__":
    if mkdocs != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")
        remove_file(".github/workflows/docs.yml")

    if codecov != "y":
        remove_file("codecov.yml")
