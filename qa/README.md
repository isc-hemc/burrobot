# Questions and Answers API (Burrobot)

`Questions and Answers API` is the [Burrobot](https://github.com/Davestring/burrobot) service itself. This API is a Flask application with a pretrained model using `transformers` and `BERT`.

## Contents

- [Dependencies](#dependencies)
- [Content](#content)
- [Appendices](#appendices)
- [Authors](#Authors)

## Dependencies

![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)
![Flask 1.1.2](https://img.shields.io/badge/Flask-1.1.2-black.svg)
![Flask RESTful 3.10.0](https://img.shields.io/badge/Flask-RESTful-0.3.8-green.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.7.1-red.svg)
![Transformers 4.1.1](https://img.shields.io/badge/Transformers-4.1.1-yellow.svg)

## Content

### Installing Dependencies

This project uses [pipenv](https://pipenv-fork.readthedocs.io/en/latest/) to create a virtual environment and manage the project dependencies.

> Use the following command to install the project dependencies and create the virtual environment.
```bash
pipenv install
```

> Use the following command to install the development dependencies.
```bash
pipenv install --dev
```

> Use the following command to check the path of the virtual environment.
```bash
pipenv --venv
```

### Local Development

Flask cames with a development server that can be easily run with the following:

```bash
pipenv run python manage.py
```

This server only must be used in development environments.

### Production Deployment

The applications comes with a [uWSGI](./run.ini) implementation, this configuration will
help us to deploy a production server. To run the Web Server Gateway Interface run:

```bash
pipenv run uwsgi run.ini
```

## Appendices

### CMS API

This API makes a request to the [CMS](https://github.com/Davestring/burrobot/tree/main/cms) service to retrieve the updated information that the QA model will use so make sure to deploy that service first before making any HTTP request to this API.

### Burrobot Request

To use the service, make a POST request to the following endpoint:

> /burrobot - endpoint payload,
```json
{
    "context_id": 1,
    "question": "how was your day?"
}
```

If everything goes well, you should see a similar response:

> Response.
```json
{
    "message": "Burrobot says:",
    "data": "Good!"
}
```

### uWSGI

Make sure you have installed on your machine the uWSGI server for production deploys as well as the python uwsgi library:

> For MacOS:
```bash
brew install uwsgi
```

## Authors

***David Martinez** - [Davestring](https://github.com/Davestring)

***José Ricardo López García** - [JoseRicardoL](https://github.com/JoseRicardoL)