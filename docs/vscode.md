# VSCode configuration settings

The following are some common settings that can be configured in Visual Studio Code to improve the Python development experience.

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

- `[python]`: This section applies settings specifically for Python files.

- `"editor.codeActionsOnSave"`: Specifies actions to be performed when a Python file is saved.
- `"source.fixAll.ruff"`: "explicit": The Ruff auto-fix feature is set to explicit mode, meaning it will only fix issues when explicitly told to do so.
- `"source.organizeImports.ruff": "explicit"`: The Ruff import organization feature is set to explicit mode, meaning it will only organize imports when explicitly told to do so.
- `"editor.formatOnSave": true`: This setting enables automatic code formatting when a Python file is saved.
- `"editor.rulers": [100]`: This setting adds a vertical ruler at the 100th character in the editor for Python files to guide line length.
- `"files.exclude": {"**/__pycache__": true}`: This setting hides all __pycache__ directories in the file explorer.

- `"python.languageServer": "Pylance"`: This setting specifies Pylance as the language server for Python. A language server provides features like auto-completion and syntax highlighting.

- `"editor.formatOnPaste": true`: This setting enables automatic code formatting when you paste code into the editor.

- `"notebook.lineNumbers": "on"`: This setting enables line numbers in Jupyter notebooks.

- `"editor.inlineSuggest.enabled": true`: This setting enables inline suggestions, which show suggested completions as you type.

- `"editor.formatOnType": true`: This setting enables automatic code formatting as you type.

- `"git.autofetch": true`: This setting enables automatic fetching of Git data.

- `"editor.defaultFormatter": "charliermarsh.ruff"`: This setting specifies Ruff as the default formatter for code in the editor.

- `"python.terminal.activateEnvInCurrentTerminal": true`: This setting enables automatic activation of the Python environment in the current terminal.

- `"python.defaultInterpreterPath": "${workspaceFolder}/.venv"`: This setting specifies the default Python interpreter path to be the virtual environment created in the project.
