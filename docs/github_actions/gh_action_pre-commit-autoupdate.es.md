# GitHub Action: Actualización automática de Pre-commit

Este archivo de GitHub Action configura un flujo de trabajo llamado "Pre-commit auto-update". Este flujo de trabajo es responsable de actualizar automáticamente los hooks de pre-commit en tu repositorio.

[pre-commit_autoupdate.yml](https://github.com/JoseRZapata/data-science-project-template/blob/main/{{cookiecutter.repo_name}}/.github/workflows/pre-commit_autoupdate.yml)

## Detalles del Flujo de Trabajo

- `on`: Este flujo de trabajo se activa en dos situaciones:

    - `schedule`: Se ejecuta automáticamente cada lunes a las 7:00 UTC (según el cron schedule `"0 7 * * 1"`).
    - `workflow_dispatch`: Permite ejecutar manualmente el flujo de trabajo desde la interfaz de usuario de GitHub.
- `jobs`: Define un job llamado "pre-commit-update".

## Detalles del Job "pre-commit-update"

`runs-on`: Este job se ejecuta en la última versión de Ubuntu.

`steps`: Define los pasos a seguir en este job.

`Checkout`: Este paso usa la acción actions/checkout@v3 para obtener una copia del repositorio.

`Actualizar hooks de pre-commit`: Este paso usa la acción `brokenpip3/action-pre-commit-update` para actualizar los hooks de pre-commit. Esta acción requiere un token de GitHub para funcionar, que se pasa mediante `github-token: ${{ secrets.PAT }}`. [PAT] es un secreto almacenado en la configuración del repositorio que contiene un token de acceso personal con alcance de repositorio.

En resumen, este flujo de trabajo se encarga de mantener actualizados los hooks de pre-commit en el repositorio, ejecutándose automáticamente cada lunes y permitiendo también la ejecución manual cuando sea necesario.

[PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token
