# 🔑 Configurar Tokens

Algunas de las GitHub Actions requieren claves de token que se establezcan como secretos en el repositorio de GitHub. Los siguientes tokens son requeridos:

## GitHub Action secrets.PAT

Este es el token de acceso personal para el repositorio de GitHub y se usa para:

- Subir la documentación de MKDocs a la rama `gh-pages`.
- Subir la actualización automática de pre-commit a la rama `main`.

Cómo configurar el secrets.PAT:

- Crear en github un [Personal Access Token (PAT)](https://github.com/settings/tokens?type=beta), para el repositorio específico. [Cómo](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)
- Darle acceso de lectura/escritura a "Contents", "Pull Requests" y "Workflows" en la sección "Repository Permissions".
- Agregar el PAT a los secretos del repositorio. Ir a la configuración del repositorio > Secrets and variables > Actions. Luego en Repository secrets agregar un nuevo secreto de repositorio y nombrarlo `PAT` y pegar el token.
- Debes permitir explícitamente a GitHub Actions crear pull requests. Esta configuración se encuentra en la configuración del repositorio bajo Actions > General > Workflow permissions. Seleccionar `Read repository contents and packages permissions`

## CODECOV_TOKEN

Este es el token para codecov. Se usa para subir el reporte de cobertura a codecov. Puedes obtenerlo desde codecov.io. No es requerido para desarrollo local.
<https://docs.codecov.com/docs/quick-start>

Debes agregar este secreto al repositorio de github. Cómo agregar codecov al repositorio de github: <https://docs.codecov.com/docs/adding-the-codecov-token#github-actions>

---

## Referencias

- <https://github.com/peter-evans/create-pull-request?tab=readme-ov-file#workflow-permissions>
- <https://github.com/peter-evans/create-pull-request/issues/2443>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token>
