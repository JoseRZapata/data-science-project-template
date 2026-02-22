
# GitHub Action: Pruebas CI/CD

Este flujo de trabajo de GitHub Action está diseñado para optimizar y automatizar los procesos de CI/CD de tu proyecto. El flujo de trabajo se activa en pull requests y pushes a la rama `main`. Realiza varias tareas clave incluyendo linting, verificaciones de pre-commit, validación de actualización del proyecto y ejecución de pruebas con reportes de cobertura.

[ci.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/ci.yml)

---

## Detalles del Flujo de Trabajo

### Disparadores (`on`)

- **`pull_request`**: El flujo de trabajo se ejecuta cuando se abre o actualiza un pull request.
- **`push`**: El flujo de trabajo se activa para pushes a la rama `main`.

### Resumen de Jobs

El flujo de trabajo define cuatro jobs:

1. **`actionlint`**: Valida la sintaxis y estructura de los archivos de flujo de trabajo de GitHub Action.
2. **`lint-cruft`**: Asegura que no existan archivos `.rej`, verificando que las actualizaciones del proyecto se aplicaron correctamente.
3. **`pre-commit`**: Ejecuta los hooks de pre-commit para aplicar estándares de código y formateo en todos los archivos.
4. **`test`**: Ejecuta pruebas unitarias con reportes de cobertura y sube los resultados a Codecov.

---

## Detalles de los Jobs

### **1. actionlint**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

- **Checkout**: Usa `actions/checkout@v4` para obtener el repositorio.
- **Descargar actionlint**: Obtiene `actionlint` usando un script bash.
- **Verificar archivos de flujo de trabajo**: Ejecuta `actionlint` para validar los archivos de flujo de trabajo.

---

### **2. lint-cruft**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

- **Checkout**: Usa `actions/checkout@v4` para obtener el repositorio.
- **Verificar archivos `.rej`**: Falla el job si se encuentran archivos `.rej`, indicando una actualización no exitosa de la estructura del proyecto.

---

### **3. pre-commit**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

- **Checkout**: Usa `actions/checkout@v4` para obtener el repositorio.
- **Instalar `uv`**: Configura la herramienta `uv` usando `astral-sh/setup-uv@v6`.
- **Ejecutar hooks de pre-commit**: Ejecuta todos los hooks de pre-commit en todo el repositorio, mostrando cualquier fallo con diffs coloreados.

---

### **4. test**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

- **Checkout**: Usa `actions/checkout@v4` para obtener el repositorio.
- **Instalar `uv`**: Configura la herramienta `uv` usando `astral-sh/setup-uv@v6`.
- **Configurar Python**: Configura Python según el archivo `.python-version` usando `actions/setup-python@v5`.
- **Instalar el proyecto**: Instala el proyecto con todos los extras y dependencias de desarrollo usando `uv sync`.
- **Ejecutar pruebas con cobertura**: Ejecuta pruebas con `pytest` y genera un reporte de cobertura en formato XML.
- **Subir reporte de cobertura**: Sube el reporte de cobertura a Codecov usando `codecov/codecov-action@v5`. Requiere un secreto `CODECOV_TOKEN` almacenado en la configuración del repositorio.

---

En resumen, este flujo de trabajo automatiza el linting, la validación de actualización del proyecto, las verificaciones de pre-commit, las pruebas y los reportes de cobertura para un pipeline de CI/CD robusto.
