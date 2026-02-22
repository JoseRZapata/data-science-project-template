# GitHub Action: Sincronización de Etiquetas

Este flujo de trabajo de GitHub Action automatiza la sincronización de etiquetas de GitHub basándose en un archivo de configuración YAML. Se ejecuta ante cambios en la configuración de etiquetas o en su archivo de flujo de trabajo y asegura consistencia en la gestión de etiquetas en todo el repositorio.

[github-labeler.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/github-labeler.yml)

---

## Detalles del Flujo de Trabajo

### Disparadores (`on`)

- **`push`**:
    - Se activa cuando se hacen pushes a la rama `main`.
    - Rutas monitoreadas:
        - `.github/labels.yml`: El archivo YAML que contiene las definiciones de etiquetas.
        - `.github/workflows/labels.yml`: La configuración del flujo de trabajo para sincronización de etiquetas.
- **`pull_request`**:
    - Se activa cuando los pull requests modifican los archivos `.github/labels.yml` o `.github/workflows/labels.yml`.

---

## Detalles del Job

### **labeler**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

1. **Checkout del repositorio**:
   - Usa `actions/checkout@v4` para obtener el contenido del repositorio.

2. **Ejecutar Labeler**:
   - Usa `crazy-max/ghaction-github-labeler@v5` para sincronizar etiquetas basándose en el archivo `.github/labels.yml`.
   - **Entradas**:
     - `github-token`: Un token de acceso personal (PAT) almacenado en los secretos del repositorio para autenticación.
     - `yaml-file`: Especifica la ruta al archivo de configuración de etiquetas (`.github/labels.yml`).
     - `dry-run`: Simula el proceso de sincronización de etiquetas cuando el flujo de trabajo se activa por un pull request (`true` para pull requests, `false` en caso contrario).
     - `exclude`: Excluye etiquetas específicas de la sincronización. Aquí, las etiquetas que coincidan con `help*` o `*issue` son excluidas.

---

En resumen, este flujo de trabajo asegura que las etiquetas de GitHub en tu repositorio se mantengan consistentes con las definiciones en `.github/labels.yml`. Soporta tanto actualizaciones en vivo para pushes como modo de simulación para pull requests, proporcionando una solución robusta para la gestión de etiquetas.
