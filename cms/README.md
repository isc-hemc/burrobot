# Burrobot CMS

`Burrobot CMS` is a simple app developed in Python using the Django REST Framework. This API is focused on updating and manage the context content to serve updated responses to the users through the Facebook API.

## Contents

- [Dependencies](#dependencies)
- [Content](#content)
- [Appendices](#appendices)

## Dependencies

![Docker 20.10.2](https://img.shields.io/badge/Docker-20.10.2-blue.svg)
![Python 3.8](https://img.shields.io/badge/Python-3.8-yellow.svg)
![Django 2.2.0](https://img.shields.io/badge/Django-2.2.0-black.svg)
![Django REST Framework 3.10.0](https://img.shields.io/badge/DjangoRestFramework-3.10.0-green.svg)
![SQLite 3.0](https://img.shields.io/badge/SQLite-3.0-white.svg)

## Content
### Installing Dependencies

This project uses [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) to create a virtual environment and manage the project dependencies.

> Use the following command to install the project dependencies and create the virtual environment.
```bash
pipenv install
```

> Use the following command to install de development dependencies.
```bash
pipenv install --dev
```

> Use the following command to check the path of the virtual environment.
```bash
pipenv --venv
```

### Executing Migrations

In the [.vscode](./.vscode) folder there is a [launch](./.vscode/launch.json) file so in the VSCode Debugger we can easily execute the `API: Make Migrations` and the `API: Migrate` tasks in that order. To execute the migrations manually you can use the following commands:

```bash
pipenv run python manage.py makemigrations
```

```bash
pipenv run python manage.py migrate
```
## Appendices
### Pre Commit

The [pre-commit](https://pre-commit.com/) configuration can be found in `.pre-commit-config.yaml` file. When cloning this repository you should execute the following command in order to set up the git hook scripts:

```bash
pipenv run pre-commit install
```

Now, `pre-commit` will run automatically on `git commit`.
### Git Flow

This project uses [git-flow](http://danielkummer.github.io/git-flow-cheatsheet/) guideline to perform high-level repository operations. Once you clone this repository make shure to execute the following command to start using `git-flow` and continue using the project guideline.

```bash
git flow init
```

For this project from the `main` branch we will take the production build and from the `develop` branch the staging environment.

#### Feature

For developing a new _feature_ we need to run the following command:

```bash
git flow feature start my-feature
```

Once all the changes are done we should squash all out commits and merge with the `develop`branch:

```bash
git flow feature finish my-feature
```

#### Release

For release a new version of the application we should run the following command:

```bash
git flow release start vX.X.X
```

The `vX.X.X` will be the version tag of the release, we use [semver](https://semver.org/lang/es/) guideline when creating a new release version. Once the release it ready to be deployed we can run the following command:

```bash
git flow release finish vX.X.X
```

This will merge the release branch into `develop` and `main`, but not only that, it will also create a `tag` that we will push to our repository using the command:

```bash
git push --tags
```

This will help us to keep out project stable and healthy.

### Django Utils

#### Creating a Project

This project uses [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) to manage the project dependencies and environment, after installing the Django dependency (`pipenv install Django~=2.2.0`), we can easily create a Django project executing the following command:

```bash
pipenv run django-admin startproject app .
```

#### Creating an Application

As we are creating all our applications inside the [app](./app) folder we can create a new app using the following commands:

```bash
cd app
pipenv run python ./../manage.py startapp myapp
```

#### Creating a Superuser

After launching the project we can easily create a superuser executing the following command:

```bash
pipenv run python manage.py createsuperuser
```

After that, enter the email and password of the superuser in the command line.
