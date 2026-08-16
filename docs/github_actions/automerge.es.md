# GitHub Action: Automerge

Este flujo de trabajo de GitHub Action automatiza la fusión de pull requests etiquetados con `automerge`. Soporta ejecuciones programadas y ejecución manual, asegurando una integración ágil de cambios que cumplan con criterios predefinidos.

[automerge.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/automerge.yml)

---

## Detalles del Flujo de Trabajo

### Disparadores (`on`)

- **`schedule`**:
    - Se ejecuta automáticamente **cada hora los domingos** (UTC) para capturar los jobs escalonados de creación de PRs (`0 * * * 0`).
    - Se ejecuta diariamente a las 08:00 UTC de lunes a sábado (`0 8 * * 1-6`).
- **`workflow_dispatch`**:
    - Permite la ejecución manual del flujo de trabajo a través de la interfaz de GitHub Actions.

---

## Detalles del Job

### **automerge**

**`runs-on`**: `ubuntu-latest`

**Pasos**:

1. **Automerge**:
   - Usa la acción `pascalgn/automerge-action@v0.16.3` para fusionar pull requests que cumplan criterios específicos.
   - **Variables de Entorno**:
     - `GITHUB_TOKEN`: Un token de acceso personal (PAT) almacenado en los secretos del repositorio para autenticación.
     - `MERGE_METHOD`: Especifica el método de fusión. En este caso, se usa el método `squash`, que combina todos los commits en un solo commit al fusionar.
     - `MERGE_REQUIRED_APPROVALS`: Define el número de aprobaciones requeridas para la fusión. Aquí está configurado en `"0"`, lo que significa que no se requieren aprobaciones.
     - `MERGE_LABELS`: Especifica la etiqueta (`automerge`) que activa el proceso de automerge.

---

En resumen, este flujo de trabajo simplifica el proceso de fusión de pull requests al fusionar automáticamente aquellos etiquetados con `automerge` usando el método `squash`. Puede ejecutarse diariamente o manualmente, asegurando flexibilidad y eficiencia en el proceso de desarrollo.

---

## Configuración Requerida del Repositorio para Workflows de PR Automatizados

Para que el workflow de automerge (y otros PRs creados por bots como Dependabot, `update_template_deps`, `update_template_workflows`) ejecuten sus checks de CI **automáticamente sin aprobación manual**, debes configurar lo siguiente en el **repositorio de tu proyecto generado**:

1. Ve a **Settings → Actions → General**
2. En **"Fork pull request workflows from outside collaborators"**, selecciona:
   - **"Require approval for first-time contributors who are new to GitHub"** (recomendado), o
   - **"Read‑only"** (si confías en todos los colaboradores)

Sin esta configuración, los PRs creados por bots mostrarán **"X workflows awaiting approval"** y sus checks permanecerán bloqueados hasta que un mantenedor apruebe manualmente cada ejecución.

Esta configuración solo necesita hacerse una vez por repositorio generado.
