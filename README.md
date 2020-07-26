# Open Graph online parser

## Description 

This is the test task app that described in the [test_task_description.txt](test_task_description.txt) file (in Russian)
The general purpose of this app is generate a JSON by url.
A JSON will contain a [Open Graph metadata](https://ogp.me/) extracted from an url.

## Installation on nix

open terminal and run the following commands:

```shell script
git clone git clone https://github.com/dremdem/og_online_parser.git
cd og_online_parser
pipenv install
python manage.py migrate
```

## Usage

open terminal and run the following commands:

```shell script
python manage.py runserver
```

* open http://127.0.0.1:8000/

## Extensibility

I decided not develop the parser myself. 
I'm going to use existing solutions.
This task will be like interface/wrapper for any solution, 
that parse Open Graph metadata.

First of all I've found the following repos: 

* https://github.com/jvanasco/metadata_parser

## Django's Applications

### api

### ui

## Models

### OGInterface

Describes Open Graph library for the parsing Open Graph markup

Attributes:

* name
* description
* link to GitHub
* model name where parser class will be stored
* parser class name

### UrlHistory

Stores the last N parsed urls.
Amount of N could be specified in the settings.

Attributes:

* url

### Routes

#### Get JSON

Return prettified JSON-string by url

* route: /parse
* method: POST
* payload: {url: <url>, parser_id: <parser_id>}

#### List last L urls

Return the last L parsed urls.
If the L is not defined then return the last N urls.   

* route: /last, /last/<L>
* method: GET

## Tech stack 

* Python 3.8: https://www.python.org/
* Django DRF: https://www.django-rest-framework.org/
* VueJS: https://vuejs.org/
* Axios: https://github.com/axios/axios
* Sqllite: https://www.sqlite.org/

## Frontend

The SPA(Single Page Application) by VueJS with two options: 

* Get a JSON by an url 
* Get a last L urls

### Elements

Parsing block:

* url 
* combobox with parsers
* JSON text area
* Parse button
* Clear button

Last url block:

* list of last urls
* quantity of last urls
* Get List button

## Tests

I'm going to use pytest-django implementation
* https://pytest-django.readthedocs.io/en/latest/
* https://aalvarez.me/posts/testing-django-and-drf-with-pytest/
* https://medium.com/@poorva.mahajan2990/django-drf-file-upload-and-pytest-a31923e9e9d1


