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
