# 🛠️ Configuración del entorno de desarrollo local

Desarrollo proyectos de ciencia de datos en Python en Linux OS o MAC OS. (Para Windows OS recomiendo [WSL] y ejecutar los comandos como en Linux OS).

Configuro mi entorno de desarrollo local siguiendo los siguientes pasos:

## 💻 Configuración del computador para desarrollar con Python

1. Instalar [Git]
      - Linux: `sudo apt-get install git`
      - MAC: `brew install git`
2. Instalar [Make]
      - Linux: `sudo apt-get install make`
      - MAC: `brew install make`
3. Instalar localmente [UV] para gestionar versiones de Python, dependencias y entornos virtuales.
      - Linux:

        ```bash title="Instalar uv en Linux o MACOS"
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

        - Verificar la versión de instalación ejecutando en terminal: `uv version`

4. Instalar [Python] usando [UV], actualmente estoy usando Python 3.11
      - `uv python install 3.11` # Instalar Python 3.11 en el computador

5. En la carpeta del proyecto, establecer la versión de Python y crear un entorno virtual.
   1. Si el proyecto tiene archivo `uv.lock`
      - `uv sync` # Crear Entorno Virtual e instalar dependencias.
      - `source .venv/bin/activate` # Activar Entorno
   2.
      - `uv venv --python 3.11` # Crear un entorno virtual de Python 3.11
      - `source .venv/bin/activate` # Activar el entorno virtual de Python 3.11
      - **Verificar la versión de instalación** ejecutando en terminal: `python --version`

**Nota:** Para desactivar el entorno virtual en terminal escribe: `deactivate`

## 🐍 Herramientas generales de Python

Herramientas generales que uso para desarrollar proyectos en Python. La más importante es [UV] para gestionar versiones de Python, entornos virtuales, gestionar dependencias para los proyectos y tener herramientas en entornos aislados, porque las aplicaciones se ejecutan en su propio entorno virtual para evitar conflictos de dependencias y están disponibles en todas partes.

[UV Highligths](https://github.com/astral-sh/uv?tab=readme-ov-file#highlights)

1. [Cruft] te permite mantener todo el código repetitivo necesario para empaquetar y construir proyectos separado del código que escribes intencionalmente. Totalmente compatible con plantillas existentes de Cookiecutter.
      - `uv tool install cruft`
2. (opcional) [Pip-audit] para verificar localmente la seguridad de las dependencias del proyecto.
      - `uv tool install pip-audit`
3. (opcional) [Actionlint] para verificar la sintaxis de los archivos de configuración de GitHub Actions del proyecto.
      - `uv tool install actionlint`

**Nota:** [UV] reemplaza herramientas como [Pyenv], [Poetry] y otras para gestionar las versiones de Python, entornos y dependencias.

## 📁 Iniciar un nuevo proyecto de ciencia de datos

1. Iniciar un nuevo proyecto usando [Cruft] con la [Data Science Project Template].

    ```shell title="crear proyecto"
    cruft create https://github.com/JoseRZapata/data-science-project-template
    ```

2. Responder las preguntas para crear el proyecto.
3. Ejecutar `make init_git` para inicializar [Git] o puedes hacer lo mismo ejecutando estos comandos:

    ```shell title="inicializar entorno"
        git init -b main
        git add .
        git commit -m "🎉 Begin a project, Initial commit"
    ```

4. Ejecutar `make install_env` para instalar las dependencias del proyecto. O puedes hacer lo mismo ejecutando estos comandos:

    ```shell title="instalar dependencias"
        uv sync --all-groups
        uv run pre-commit install
    ```

5. 🎉 ¡Felicidades! Comienza a programar tu proyecto.

6. Si quieres subir este repositorio a GitHub, primero crea un nuevo repositorio en GitHub y luego ejecuta los siguientes comandos para subir tu repositorio local a GitHub.

    ```shell title="subir a GitHub"
        git remote add origin <tu-url-del-repo>
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
[Pyenv]: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation
[Python]: https://www.python.org/downloads/
[UV]: https://docs.astral.sh/uv/
[WSL]: https://docs.microsoft.com/en-us/windows/wsl/install
