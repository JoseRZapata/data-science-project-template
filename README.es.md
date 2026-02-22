# Plantilla de proyecto de ciencia de datos

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/charliermarsh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![pages-build-deployment](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/pages/pages-build-deployment/badge.svg?branch=gh-pages)](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/pages/pages-build-deployment)
[![CI](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/ci.yml/badge.svg)](https://github.com/JoseRZapata/data-science-project-template/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JoseRZapata/data-science-project-template/graph/badge.svg?token=7LCPX574UF)](https://codecov.io/gh/JoseRZapata/data-science-project-template)

---

Una plantilla moderna para proyectos de ciencia de datos con todas las herramientas necesarias para experimentación, desarrollo, pruebas y despliegue. Desde notebooks hasta producción.

✨📚✨ Documentación: <https://joserzapata.github.io/data-science-project-template/>

Código Fuente: <https://github.com/JoseRZapata/data-science-project-template>

---

## Características

<!-- features-begin -->

- Gestión de dependencias con [UV]
- Gestión de entornos virtuales con [UV]
- Linting con [pre-commit] y [Ruff]
- Integración continua con [GitHub Actions]
- Documentación con [mkdocs] y [mkdocstrings] usando el tema [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
- Actualizaciones automáticas de dependencias con [Dependabot]
- Formateo de código con [Ruff]
- Ordenamiento de imports con [Ruff] usando la regla isort.
- Pruebas con [pytest]
- Cobertura de código con [Coverage.py]
- Reportes de cobertura con [Codecov]
- Verificación estática de tipos con [mypy]
- Auditoría de seguridad con [Ruff] usando la regla bandit.
- Gestión de etiquetas del proyecto con [GitHub Labeler]

---
Tabla de Contenidos
<!-- markdownlint-disable MD007 -->
- [Plantilla de proyecto de ciencia de datos](#plantilla-de-proyecto-de-ciencia-de-datos)
  - [Características](#características)
  - [📁 Crear un Nuevo Proyecto](#-crear-un-nuevo-proyecto)
    - [👍 Recomendaciones](#-recomendaciones)
    - [🍪🥇 Vía Cruft - (**recomendado**)](#-vía-cruft---recomendado)
    - [🍪 Vía Cookiecutter](#-vía-cookiecutter)
  - [🔗  Vincular un Proyecto Existente](#--vincular-un-proyecto-existente)
  - [🗃️ Estructura del proyecto](#️-estructura-del-proyecto)
  - [✨ Características y Herramientas](#-características-y-herramientas)
    - [🚀 Estandarización y Automatización del Proyecto](#-estandarización-y-automatización-del-proyecto)
      - [🔨 Automatización del Flujo de Trabajo del Desarrollador](#-automatización-del-flujo-de-trabajo-del-desarrollador)
      - [🌱 Paquete Python o Plantilla de Proyecto Renderizado Condicionalmente](#-paquete-python-o-plantilla-de-proyecto-renderizado-condicionalmente)
    - [🔧 Mantenibilidad](#-mantenibilidad)
      - [🏷️  Verificación de Tipos y Validación de Datos](#️--verificación-de-tipos-y-validación-de-datos)
      - [✅ 🧪 Pruebas/Cobertura](#--pruebascobertura)
      - [🚨 Linting](#-linting)
        - [🔍 Calidad de código](#-calidad-de-código)
        - [🎨 Formateo de código](#-formateo-de-código)
      - [👷 CI/CD](#-cicd)
        - [Actualizaciones automáticas de dependencias](#actualizaciones-automáticas-de-dependencias)
        - [Revisión de dependencias en PR](#revisión-de-dependencias-en-pr)
        - [Actualizaciones automáticas de Pre-commit](#actualizaciones-automáticas-de-pre-commit)
  - [🔒 Seguridad](#-seguridad)
    - [🔏 Pruebas Estáticas de Seguridad de Aplicaciones (SAST)](#-pruebas-estáticas-de-seguridad-de-aplicaciones-sast)
  - [⌨️ Accesibilidad](#️-accesibilidad)
    - [🔨 Herramienta de automatización (Makefile)](#-herramienta-de-automatización-makefile)
    - [📝 Documentación del Proyecto](#-documentación-del-proyecto)
    - [🗃️ Plantillas](#️-plantillas)
    - [Buenas prácticas](#buenas-prácticas)
  - [Referencias](#referencias)
<!-- markdownlint-enable MD007 -->
## 📁 Crear un Nuevo Proyecto

### 👍 Recomendaciones

Se recomienda encarecidamente usar gestores para las versiones de Python, dependencias y entornos virtuales.

Este proyecto usa [UV], una herramienta extremadamente rápida para reemplazar [pip](https://pip.pypa.io/en/stable/), pip-tools, [Pipx], [Poetry], [Pyenv], twine, [virtualenv](https://virtualenv.pypa.io/en/latest/), y más.

🌟 Revisa cómo configurar tu entorno: <https://joserzapata.github.io/data-science-project-template/local_setup/>

### 🍪🥇 Vía [Cruft] - (**recomendado**)

```bash title="instalar cruft"
# Instalar cruft en un entorno aislado usando uv

uv tool install cruft

# O instalar con pip

pip install --user cruft # Instalar `cruft` en tu PATH para fácil acceso
```

```shell title="crear proyecto"
cruft create https://github.com/JoseRZapata/data-science-project-template
```

luego dentro de la carpeta del proyecto, inicializar git y el entorno uv usando [Make]:

```shell title="instalar proyecto"
make init_git
make install_env
source .venv/bin/activate
```

### 🍪 Vía [Cookiecutter]

```shell title="instalar cookiecutter"

uv tool install cookiecutter # Instalar cookiecutter en un entorno aislado

# O instalar con pip

pip install --user cookiecutter # Instalar `cookiecutter` en tu PATH para fácil acceso
```

```shell title="crear proyecto"
cookiecutter gh:JoseRZapata/data-science-project-template
```

Nota: **_Cookiecutter_** usa `gh:` como abreviatura de `https://github.com/`

## 🔗  Vincular un Proyecto Existente

Si el proyecto fue instalado originalmente vía [Cookiecutter], primero debes usar [Cruft] para vincular el proyecto con la plantilla original:

```shell
cruft link https://github.com/JoseRZapata/data-science-project-template
```

Luego:

```shell
cruft update
```

## 🗃️ Estructura del proyecto

Estructura de carpetas para proyectos de ciencia de datos  [¿por qué?](https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71)

- [Estructura de datos](https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention)
- [Pipelines basados en Feature/Training/Inference Pipelines](https://www.hopsworks.ai/post/mlops-to-ml-systems-with-fti-pipelines)

```bash
.
├── .code_quality
│   ├── mypy.ini                        # configuración de mypy
│   └── ruff.toml                       # configuración de ruff
├── .github                             # configuración de github
│   ├── actions
│   │   └── python-poetry-env
│   │       └── action.yml              # github action para configurar entorno python
│   ├── dependabot.md                   # github action para actualizar dependencias
│   ├── pull_request_template.md        # plantilla para pull requests
│   └── workflows                       # flujos de trabajo de github actions
│       ├── ci.yml                      # ejecutar integración continua (pruebas, pre-commit, etc.)
│       ├── dependency_review.yml       # revisión de dependencias
│       ├── docs.yml                    # construir documentación (mkdocs)
│       └── pre-commit_autoupdate.yml   # actualizar hooks de pre-commit
├── .vscode                             # configuración de vscode
|   ├── extensions.json                 # lista de extensiones recomendadas
|   ├── launch.json                     # configuración de ejecución de vscode
|   └── settings.json                   # configuración de vscode
├── conf                                # carpeta de archivos de configuración
│   └── config.yaml                     # archivo principal de configuración
├── data
│   ├── 01_raw                          # datos crudos inmutables
│   ├── 02_intermediate                 # datos tipados
│   ├── 03_primary                      # datos del modelo de dominio
│   ├── 04_feature                      # características del modelo
│   ├── 05_model_input                  # frecuentemente llamados 'master tables'
│   ├── 06_models                       # modelos serializados
│   ├── 07_model_output                 # datos generados por ejecuciones del modelo
│   ├── 08_reporting                    # reportes, resultados, etc
│   └── README.md                       # descripción de la estructura de datos
├── docs                                # documentación de tu proyecto
│   ├── index.md                        # página principal de documentación
├── models                              # almacenar modelos finales
├── notebooks
│   ├── 1-data                          # extracción y limpieza de datos
│   ├── 2-exploration                   # análisis exploratorio de datos (EDA)
│   ├── 3-analysis                      # Análisis estadístico, pruebas de hipótesis.
│   ├── 4-feat_eng                      # ingeniería de características (creación, selección y transformación.)
│   ├── 5-models                        # entrenamiento de modelos, evaluación y ajuste de hiperparámetros.
│   ├── 6-interpretation                # interpretación de modelos
│   ├── 7-deploy                        # empaquetado de modelos, estrategias de despliegue.
│   ├── 8-reports                       # narrativa, resúmenes y conclusiones de análisis.
│   ├── notebook_template.ipynb         # plantilla para notebooks
│   └── README.md                       # información sobre los notebooks
├── src                                 # código fuente para uso en este proyecto
│   ├── README.md                       # descripción de la estructura de src
│   ├── tmp_mock.py                     # archivo python de ejemplo
│   ├── data                            # extracción, validación, procesamiento, transformación de datos
│   ├── model                           # entrenamiento, evaluación, validación, exportación de modelos
│   ├── inference                       # predicción, servicio, monitoreo de modelos
│   └── pipelines                       # orquestación de pipelines
│       ├── feature_pipeline            # transforma datos crudos en características y etiquetas
│       ├── training_pipeline           # transforma características y etiquetas en un modelo
│       └── inference_pipeline          # toma características y un modelo entrenado para predicciones
├── tests                               # código de pruebas para tu proyecto
│   ├── test_mock.py                    # archivo de prueba de ejemplo
│   ├── data                            # pruebas para el módulo data
│   ├── model                           # pruebas para el módulo model
│   ├── inference                       # pruebas para el módulo inference
│   └── pipelines                       # pruebas para el módulo pipelines
├── .editorconfig                       # configuración del editor
├── .gitignore                          # archivos a ignorar en git
├── .pre-commit-config.yaml             # configuración para hooks de pre-commit
├── codecov.yml                         # configuración para codecov
├── Makefile                            # comandos útiles para configurar entorno, ejecutar pruebas, etc.
├── mkdocs.yml                          # configuración para documentación mkdocs
├── pyproject.toml                      # archivo de dependencias y configuración del proyecto
├── uv.lock                             # dependencias bloqueadas
└── README.md                           # descripción de tu proyecto
```

## ✨ Características y Herramientas

### 🚀 Estandarización y Automatización del Proyecto

#### 🔨 Automatización del Flujo de Trabajo del Desarrollador

- Empaquetado de Python, gestión de dependencias y gestión de entornos
  con [UV] - [`¿por qué usar un gestor? (uv es un reemplazo de poetry)`](https://codecut.ai/poetry-a-better-way-to-manage-python-dependencies/)
- Orquestación del flujo de trabajo del proyecto
  con [Make] como [interfaz shim](https://en.wikipedia.org/wiki/Shim_(computing))
    - [Makefile](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/Makefile) autodocumentado; simplemente escribe
      `make` en la línea de comandos para mostrar documentación autogenerada sobre los
      objetivos disponibles:
- Sincronización automatizada de plantillas Cookiecutter con [Cruft] - [`¿por qué?`](https://careers.wolt.com/en/blog/tech/project-template-for-modern-python-packages)
- Automatización y gestión de herramientas de calidad de código con [pre-commit]
- Integración y despliegue continuos con [GitHub Actions]
- Archivos de configuración del proyecto con [Hydra] - [`¿por qué?`](https://codecut.ai/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)

#### 🌱 Paquete Python o Plantilla de Proyecto Renderizado Condicionalmente

- _Opcional:_ Soporte para [Jupyter]

### 🔧 Mantenibilidad

#### 🏷️  Verificación de Tipos y Validación de Datos

- Verificación estática de tipos con [Mypy]

#### ✅ 🧪 Pruebas/Cobertura

- Pruebas con [Pytest]
- Cobertura de código con [Coverage.py]
- Reportes de cobertura con [Codecov]

#### 🚨 Linting

##### 🔍 Calidad de código

- [Ruff] Un linter y formateador de Python extremadamente rápido (10x-100x más rápido), escrito en Rust.
    - Reemplazo de ~~[Pylint]~~, ~~[Flake8]~~ (incluyendo plugins principales) y más linters bajo una interfaz única y común
- [ShellCheck](https://github.com/koalaman/shellcheck)
- Commits no seguros:
    - Secretos con [`detect-secrets`](https://github.com/Yelp/detect-secrets)
    - Archivos grandes con [`check-added-large-files`](https://github.com/pre-commit/pre-commit-hooks#check-added-large-files)
    - Archivos que contienen cadenas de conflicto de merge. [check-merge-conflict](https://github.com/pre-commit/pre-commit-hooks?tab=readme-ov-file#check-merge-conflict)

##### 🎨 Formateo de código

- [Ruff] Un linter y formateador de Python extremadamente rápido (10x-100x más rápido), escrito en Rust.
    - Reemplazo de ~~[Black]~~, ~~[isort]~~, ~~[pyupgrade]~~ y más formateadores bajo una interfaz única y común

- Formateo general de archivos:
    - [`end-of-file-fixer`](https://github.com/pre-commit/pre-commit-hooks#end-of-file-fixer)
    - [`pretty-format-json`](https://github.com/pre-commit/pre-commit-hooks#pretty-format-json)
    - (trim) [`trailing-whitespace`](https://github.com/pre-commit/pre-commit-hooks#trailing-whitespace)
    - [`check-yaml`](https://github.com/pre-commit/pre-commit-hooks#check-yaml)

#### 👷 CI/CD

##### Actualizaciones automáticas de dependencias

- Actualizaciones de dependencias con [Dependabot], merge automatizado de PRs de [Dependabot] con el [Dependabot Auto Merge GitHub Action](https://github.com/ahmadnassri/action-dependabot-auto-merge)

- Esto es un reemplazo de [pip-audit](https://github.com/pypa/pip-audit), _En tu entorno local, si quieres verificar vulnerabilidades en tus dependencias puedes usar [pip-audit]_.

##### Revisión de dependencias en PR

- Revisión de dependencias con [dependency-review-action], esta acción escanea tus pull requests por cambios de dependencias, y generará un error si se están introduciendo vulnerabilidades o licencias inválidas.

##### Actualizaciones automáticas de Pre-commit

- Actualizaciones automáticas con flujo de trabajo de [GitHub Actions] `.github/workflows/pre-commit_autoupdate.yml`

## 🔒 Seguridad

### 🔏 Pruebas Estáticas de Seguridad de Aplicaciones (SAST)

- Vulnerabilidades de código con [Bandit] usando [Ruff]

## ⌨️ Accesibilidad

### 🔨 Herramienta de automatización (Makefile)

Makefile para automatizar la configuración de tu entorno, la instalación de dependencias, la ejecución de pruebas, etc.
en la terminal escribe `make` para ver los comandos disponibles

```bash
Target                Descripción
-------------------   ----------------------------------------------------
check                 Ejecutar herramientas de calidad de código con hooks de pre-commit.
docs_test             Probar si la documentación se puede construir sin advertencias o errores
docs_view             Construir y servir la documentación
init_env              Instalar dependencias con uv y activar entorno
init_git              Inicializar repositorio git
install_data_libs     Instalar pandas, scikit-learn, Jupyter, seaborn
pre-commit_update     Actualizar hooks de pre-commit
test                  Probar el código con pytest y cobertura
```

### 📝 Documentación del Proyecto

- Construcción de documentación
  con [MkDocs] - [Tutorial](https://realpython.com/python-project-documentation-with-mkdocs/)
    - Potenciado por [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
    - Documentación automática rica a partir de anotaciones de tipo y docstrings (NumPy, Google, etc.)
    con [mkdocstrings]

### 🗃️ Plantillas

- [Plantilla de Pull Request]
- [Plantilla de Notebook]

### Buenas prácticas

- <https://www.conventionalcommits.org/>
- <https://keepachangelog.com/>

---

## Referencias

- <https://drivendata.github.io/cookiecutter-data-science/>
- <https://github.com/crmne/cookiecutter-modern-datascience>
- <https://github.com/fpgmaas/cookiecutter-poetry>
- <https://github.com/khuyentran1401/data-science-template>
- <https://github.com/woltapp/wolt-python-package-cookiecutter>
- <https://khuyentran1401.github.io/reproducible-data-science/structure_project/introduction.html>
- <https://github.com/TeoZosa/cookiecutter-cruft-poetry-tox-pre-commit-ci-cd>
- <https://github.com/cjolowicz/cookiecutter-hypermodern-python>
- <https://github.com/gotofritz/cookiecutter-gotofritz-poetry>
- <https://github.com/kedro-org/kedro-starters>

---

[Bandit]: https://github.com/PyCQA/bandit
[Black]: https://github.com/psf/black
[Codecov]: https://codecov.io/
[Cookiecutter]:https://cookiecutter.readthedocs.io/en/stable/
[Coverage.py]: https://coverage.readthedocs.io/
[Cruft]: https://cruft.github.io/cruft/
[Dependabot]: https://github.com/dependabot/dependabot-core
[dependency-review-action]: https://github.com/actions/dependency-review-action
[Flake8]:https://github.com/PyCQA/flake8
[GitHub Actions]: https://github.com/features/actions
[GitHub Labeler]: https://github.com/marketplace/actions/github-labeler
[hydra]: https://hydra.cc/
[isort]: https://github.com/PyCQA/isort
[Jupyter]: https://jupyter.org/
[Make]: https://www.gnu.org/software/make/manual/make.html
[mkdocs]: https://www.mkdocs.org/
[mkdocstrings]: https://mkdocstrings.github.io/
[Mypy]: http://mypy-lang.org/
[Plantilla de Notebook]: https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/notebooks/notebook_template.ipynb
[Pipx]:https://pipx.pypa.io/stable/
[Poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[Plantilla de Pull Request]: https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/pull_request_template.md
[Pyenv]:https://github.com/pyenv/pyenv
[Pylint]:https://github.com/PyCQA/pylint
[Pytest]: https://docs.pytest.org/en/latest/
[pyupgrade]: https://github.com/asottile/pyupgrade
[Ruff]: https://docs.astral.sh/ruff/
[UV]: https://docs.astral.sh/uv/
