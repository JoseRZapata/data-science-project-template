# 🔑 Configurar tokens para GitHub Actions

Esta plantilla ahora usa **`GITHUB_TOKEN` por defecto** en la mayoría de workflows.

`GITHUB_TOKEN` se crea automáticamente en cada ejecución de GitHub Actions, así que normalmente **no** necesitas crear un PAT manual.

## 1) Recomendación por defecto: `GITHUB_TOKEN`

### Qué configurar en el repositorio

1. Ir a **Settings → Actions → General → Workflow permissions**.
2. Seleccionar **Read and write permissions**.
3. Activar **Allow GitHub Actions to create and approve pull requests** (requerido para workflows de automatización de PRs).

En los workflows, usar:

```yaml
with:
  github-token: ${{ secrets.GITHUB_TOKEN }}
```

o:

```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Además, definir permisos explícitos en cada workflow/job cuando aplique, por ejemplo:

```yaml
permissions:
  contents: write
  pull-requests: write
  issues: write
```

## 2) ¿Cuándo sí necesitas un PAT?

Usa PAT (o token de GitHub App) solo en casos avanzados, por ejemplo:

- Cuando necesitas que PRs/commits creados por automatización disparen otros workflows y las restricciones de `GITHUB_TOKEN` lo impiden.
- Cuando necesitas acceso a **otro repositorio** (operaciones cross-repo).
- Cuando una acción requiere scopes específicos no cubiertos por los permisos actuales de `GITHUB_TOKEN`.

Si hace falta, crea un secret de repositorio llamado `PAT`.

## 3) Fallback temporal de migración (opcional)

Mientras migras repositorios existentes, puedes usar temporalmente:

```yaml
${{ secrets.PAT || github.token }}
```

Así mantienes compatibilidad con repos viejos mientras eliminas dependencia de PAT.

## 4) CODECOV_TOKEN

`CODECOV_TOKEN` sigue siendo necesario para workflows de subida de cobertura a Codecov (según tu configuración).

- <https://docs.codecov.com/docs/quick-start>
- <https://docs.codecov.com/docs/adding-the-codecov-token#github-actions>

---

## Referencias

- <https://docs.github.com/en/actions/security-guides/automatic-token-authentication>
- <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#permissions>
- <https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow>
- <https://github.com/peter-evans/create-pull-request?tab=readme-ov-file#workflow-permissions>
- <https://github.blog/changelog/2023-02-02-github-actions-updating-the-default-github_token-permissions-to-read-only/>