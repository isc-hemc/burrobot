# NLP

Module dedicated to Natural Language Processing tasks.

## Contents

- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Run](#run)
- [Appendices](#Appendices)
- [Authors](#Authors)

---

## Dependencies

![Python +3.7](https://img.shields.io/badge/python-+3.7-blue.svg)

## Configuration

To run this system it's necessary an **environment file** (**.env**). In this directory run the following commands:

``` bash
touch .env
```

``` bash
vi .env
```

Then, here is a list of the variables needed for the correct execution of this program.

### Mongo

| Variable          | Value       | Description                          |
| ----------------- | ----------- | ------------------------------------ |
| MONGO_HOST        | 127.0.0.1   | IP where mongo server is running     |
| MONGO_PORT        | 27017       | Port where mongo server is listening |
| MONGO_DB          | db          | Database name                        |
| MONGO_DB_USER     | user        | Owner of the _MONGO_DB_ database     |
| MONGO_DB_PASSWORD | xEhc67+$gh  | _MONGO_DB_USER_ password             |

### MySQL

| Variable          | Value       | Description                          |
| ----------------- | ----------- | ------------------------------------ |
| MYSQL_HOST        | 127.0.0.1   | IP where mysql server is running     |
| MYSQL_PORT        | 27018       | Port where mysql server is listening |
| MYSQL_DB          | db          | Database name                        |
| MYSQL_DB_USER     | user        | Owner of the _MYSQL_DB_ database     |
| MYSQL_DB_PASSWORD | xEhc67+$gi  | _MYSQL_DB_USER_ password             |

## Run

This script comes with a command line arguments that can be passed to improve the execution, here is a list with a description of them:

- -p, --preprocess: Pre-process the information stored in the MongoDB server. Default value is 0 (False), if want to perform the action the value must be 1 (True).
- -t, --topics: If the SQL database has been populated with different types of pre-processed data this value should be 1 (default), otherwise 0.
- -c, --collection: MongoDB collection to retrieve the data.
- -g, --graph: Plot the most common topics retrieved from the LDA.analysis.
- -h, --help: Help - Show this message.
- --topic_column: MySQL database column to analyse, the available options are: raw_msg, with_stopwords_no_lemmas_msg, with_stopwords_with_lemmas_msg, no_stopwords_no_lemmas_msg, no_stopwords_with_lemmas_msg.
- --num_topics: Number of topics to retrieve from the LDA analysis.
- --load_topics: Load topics from a file named `topics.txt` in the resources directory. If exists this label should be 1, otherwise 0.

For more information about the command line arguments, run:

```bash
pipenv run python main.py --help
```

### Workflow

The script comes with different functionalities and may be run multiple times, the correct functionality is based on that the conversations stored in the `MongoDB` be *pre-processed* and stored in the `MYSQLDB`, to do that, run:

```bash
pipenv run python main.py --preprocess=1
```

or 

```bash
pipenv run python main.py -p 1
```

This process may take a while. Once it's finish we can stract the topics of all the conversations given the `--topic_column` value, the default its *no_stopwords_with_lemmas_msg* (run --help for more information) and then plot those topics and visualize the result:

```bash
pipenv run python main.py --topics=1 --graph=1 --num-topics=50 --topic_column=raw_msg
```

or 

```bash
pipenv run python main.py -t 1 -g 1 --num-topics=50 --topic_column=raw_msg
```

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

### Appendix B - Configure and run pre-commit

Git hook scripts are useful for identifying simple issues before submission to code review. This module has a *pre-commit-config.yml* file that helps us with this task, so, in order to install the git hooks, open a terminal in this module and type the following commands:

> Install the git hook scripts

```bash
pipenv install --dev
pipenv run pre-commit install
```

> Run against all files

```bash
pipenv run pre-commit run --all-files
```

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)

***José Ricardo López García** - [JoseRicardoL](https://github.com/JoseRicardoL)
