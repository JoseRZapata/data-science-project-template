# Configuración de Pre-commit

Este proyecto usa [pre-commit](https://pre-commit.com/) para ejecutar verificaciones en cada commit.

Archivo de configuración: [.pre-commit-config.yaml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.pre-commit-config.yaml)

> Si inicializas tu proyecto usando `make install` pre-commit ya está instalado y configurado.
> Si no, puedes instalar pre-commit ejecutando en terminal `uv run pre-commit install` en la raíz del proyecto.

## pre-commit/pre-commit-hooks

Este repositorio contiene algunos hooks listos para usar proporcionados por el [proyecto pre-commit](https://github.com/pre-commit/pre-commit-hooks).

- `trailing-whitespace`: Este hook elimina los espacios en blanco al final de las líneas.
- `end-of-file-fixer`: Este hook asegura que un archivo esté vacío o termine con una nueva línea.
- `check-yaml`: Este hook verifica que los archivos yaml tengan una sintaxis válida.
- `check-case-conflict`: Este hook verifica archivos con nombres que entrarían en conflicto en un sistema de archivos insensible a mayúsculas como MacOS HFS+ o Windows FAT.
- `debug-statements`: Este hook verifica declaraciones de depuración en Python.
- `detect-private-key`: Este hook verifica la adición de claves privadas.
- `check-merge-conflict`: Este hook verifica archivos que contienen cadenas de conflicto de merge.
- `check-ast`: Este hook verifica que los archivos fuente de Python tengan un ast sintácticamente válido.
- `check-added-large-files`: Este hook previene agregar archivos grandes. El tamaño máximo es configurable.

## astral-sh/ruff-pre-commit

Este repositorio contiene hooks para el lenguaje de programación Ruff.

- [`ruff`](https://docs.astral.sh/ruff/): Este hook ejecuta el linter Ruff con la opción `--fix` para corregir automáticamente problemas en scripts y notebooks y un archivo de configuración personalizado.
- [`ruff-format`](https://docs.astral.sh/ruff/): Este hook ejecuta el formateador Ruff.

## pre-commit/mirrors-mypy

Este repositorio contiene un mirror de mypy para pre-commit.

- [`mypy`](http://mypy-lang.org/): Este hook ejecuta mypy, un verificador estático de tipos para Python, con un archivo de configuración personalizado.

## commitizen-tools/commitizen

Este repositorio contiene hooks para commitizen.

- [`commitizen`](https://commitizen-tools.github.io/commitizen/): Este hook verifica que los mensajes de commit sigan el formato de commits convencionales.
