# Configuración de VSCode

Las siguientes son algunas configuraciones comunes que pueden ser configuradas en Visual Studio Code para mejorar la experiencia de desarrollo en Python.

[https://github.com/JoseRZapata/data-science-project-template/.vscode/settings.json](https://github.com/JoseRZapata/data-science-project-template/blob/main/.vscode/settings.json)

```json
{
  "[python]": {

    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit",
    },
    "editor.formatOnSave": true,
        "editor.rulers": [
      100
    ]
  },
  "files.exclude": {
    "**/__pycache__": true
  },
  "python.languageServer": "Pylance",
  "editor.formatOnPaste": true,
  "notebook.lineNumbers": "on",
  "editor.inlineSuggest.enabled": true,
  "editor.formatOnType": true,
  "git.autofetch": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "python.terminal.activateEnvInCurrentTerminal": true,
}
```

- `[python]`: Esta sección aplica configuraciones específicamente para archivos Python.

- `"editor.codeActionsOnSave"`: Especifica acciones a realizar cuando se guarda un archivo Python.
- `"source.fixAll.ruff"`: "explicit": La función de auto-corrección de Ruff está en modo explícito, lo que significa que solo corregirá problemas cuando se le indique explícitamente.
- `"source.organizeImports.ruff": "explicit"`: La función de organización de imports de Ruff está en modo explícito, lo que significa que solo organizará imports cuando se le indique explícitamente.
- `"editor.formatOnSave": true`: Esta configuración habilita el formateo automático de código cuando se guarda un archivo Python.
- `"editor.rulers": [100]`: Esta configuración agrega una regla vertical en el carácter 100 del editor para archivos Python como guía de longitud de línea.
- `"files.exclude": {"**/__pycache__": true}`: Esta configuración oculta todos los directorios __pycache__ en el explorador de archivos.

- `"python.languageServer": "Pylance"`: Esta configuración especifica Pylance como el servidor de lenguaje para Python. Un servidor de lenguaje proporciona características como autocompletado y resaltado de sintaxis.

- `"editor.formatOnPaste": true`: Esta configuración habilita el formateo automático de código cuando pegas código en el editor.

- `"notebook.lineNumbers": "on"`: Esta configuración habilita los números de línea en Jupyter notebooks.

- `"editor.inlineSuggest.enabled": true`: Esta configuración habilita las sugerencias en línea, que muestran completados sugeridos mientras escribes.

- `"editor.formatOnType": true`: Esta configuración habilita el formateo automático de código mientras escribes.

- `"git.autofetch": true`: Esta configuración habilita la obtención automática de datos de Git.

- `"editor.defaultFormatter": "charliermarsh.ruff"`: Esta configuración especifica Ruff como el formateador predeterminado para código en el editor.

- `"python.terminal.activateEnvInCurrentTerminal": true`: Esta configuración habilita la activación automática del entorno Python en la terminal actual.

- `"python.defaultInterpreterPath": "${workspaceFolder}/.venv"`: Esta configuración especifica la ruta predeterminada del intérprete de Python al entorno virtual creado en el proyecto.
