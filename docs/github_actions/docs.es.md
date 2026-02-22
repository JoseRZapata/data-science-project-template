# GitHub Action: Construcción y Despliegue de Documentación

Este flujo de trabajo de GitHub Action automatiza el proceso de construcción y despliegue de la documentación del proyecto usando `mkdocs`. Asegura que las actualizaciones de documentación se publiquen automáticamente cada vez que se fusionen pull requests que afecten archivos específicos o cuando se active manualmente.

[docs.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/docs.yml)

---

## Detalles del Flujo de Trabajo

### Disparadores (`on`)

- **`pull_request`**:
    - Se activa cuando un pull request que afecta archivos de documentación se cierra (fusiona) en la rama `main`.
    - Rutas monitoreadas:
        - Archivos en el directorio `docs/`.
        - `readme.md`.
- **`workflow_dispatch`**: Permite la activación manual del flujo de trabajo a través de la interfaz de usuario de GitHub.

---

## Detalles del Job

### **build-and-publish**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

1. **Checkout del repositorio**:
   - Usa `actions/checkout@v4` para obtener el contenido del repositorio, asegurando acceso a los archivos de documentación más recientes.

2. **Instalar `uv`**:
   - Configura la herramienta `uv` usando `astral-sh/setup-uv@v6`.

3. **Configurar Python**:
   - Configura Python según el archivo `.python-version` usando `actions/setup-python@v5`.

4. **Construir documentación**:
   - Ejecuta `mkdocs build --clean` mediante `uv` para generar el sitio de documentación estático. La opción `--clean` asegura que el directorio de salida se limpie antes de construir.

5. **Desplegar documentación**:
   - Usa `peaceiris/actions-gh-pages@v4` para publicar la documentación construida en GitHub Pages.
   - **Entradas**:
     - `github_token`: Un Token de Acceso Personal (PAT) almacenado como secreto del repositorio.
     - `publish_dir`: Especifica el directorio que contiene el sitio construido (`./site`).

---

En resumen, este flujo de trabajo optimiza el proceso de construcción y despliegue de documentación. Actualiza automáticamente GitHub Pages cada vez que se fusionan archivos relacionados con documentación en la rama principal, con la flexibilidad adicional de activación manual para actualizaciones bajo demanda.
