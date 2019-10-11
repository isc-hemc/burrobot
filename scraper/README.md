# Facebook Messenger Scraper

This module implements a **Facebook Messenger Scraper** to download messages from a user profile or even a page thanks to [Facebook Graph API](https://developers.facebook.com/docs/graph-api/).

## Contents

- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Appendices](#Appendices)
- [Authors](#Authors)

---

## Dependencies

![Python +3.7](https://img.shields.io/badge/python-+3.7-blue.svg)

---

## Configuration

To run this system it's necessary an **environment file** (**.env**). In this directory run the following commands:

``` bash
touch .env
```

``` bash
vi .env
```

Then, here is a list of the variables needed for the correct execution of this program.

### Graph API

| Variable               | Value                  | Description                                 |
|------------------------|------------------------|---------------------------------------------|
| ACCESS_TOKEN           | ax23sF&4z$r4%g         | Access token for your Graph API application |

## Appendices

### Appendix A - Debugging with VSCode

To have all the development environment automated create a settings.json, tasks.json and launch.json files inside a .vscode folder with the following configuration:

> settings.json - this file will enable the development dependencies for clean coding, also will reference the *environment* of the project created automatically by *pipenv* and will establish the editor rulers:

```json
{
  "python.pythonPath": "$(pipenv -venv)/bin/python",
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length",
    "79"
  ],
  "[python]": {
    "editor.formatOnPaste": false
  },
  "python.linting.pydocstyleEnabled": true,
  "python.linting.pep8Enabled": true,
  "python.linting.mypyEnabled": true,
  "python.linting.pep8Path": "pycodestyle",
  "python.linting.banditEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Path": "pyflakes",
  "editor.rulers": [
    80,
    120
  ]
}
```

> tasks.json - this file will be in charge of loading the *environment* file:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Set_DOTENV",
      "type": "shell",
      "command": "PIPENV_DOTENV_LOCATION=$PWD"
    }
  ]
}
```

> launch.json - this file will run the project in the editor for correct debugging:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Scraper: Run",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/main.py",
      "preLaunchTask": "Set_DOTENV",
    }
  ]
}
```

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)

***José Ricardo López García** - [JoseRicardoL](https://github.com/JoseRicardoL)
