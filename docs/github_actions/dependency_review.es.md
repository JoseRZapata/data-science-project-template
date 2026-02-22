# GitHub Action: Revisión de Dependencias

Este flujo de trabajo de GitHub Action está diseñado para revisar automáticamente los cambios en las dependencias de tu proyecto durante los pull requests. Usa la acción `dependency-review-action` de GitHub para analizar el grafo de dependencias y señalar posibles problemas de seguridad o cambios no deseados en las dependencias.

[dependency-review.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/dependency-review.yml)

---

## Detalles del Flujo de Trabajo

### Disparadores (`on`)

- **`pull_request`**: El flujo de trabajo se activa cada vez que se crea o actualiza un pull request, asegurando que las revisiones de dependencias se realicen como parte del proceso de revisión de código.

### Permisos

- **`contents: read`**: Otorga al flujo de trabajo acceso de solo lectura al contenido del repositorio, lo cual es suficiente para realizar la revisión de dependencias.

---

## Detalles del Job

### **dependency-review**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

1. **Checkout del repositorio**:
   - Usa `actions/checkout@v4` para obtener el código del pull request para análisis.
2. **Revisión de Dependencias**:
   - Usa `actions/dependency-review-action@v4` para analizar cambios en las dependencias. Esta acción verifica:
     - Dependencias recién agregadas.
     - Actualizaciones a dependencias existentes.
     - Vulnerabilidades de seguridad en cualquier dependencia afectada.

---

En resumen, el flujo de trabajo "Revisión de Dependencias" mejora la seguridad de tu proyecto al evaluar automáticamente los cambios de dependencias en los pull requests, ayudándote a detectar posibles problemas temprano en el ciclo de desarrollo.
