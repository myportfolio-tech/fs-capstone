# Udacity Full Stack Capstone Project

## Staffer App
The staffer API provides backend services for an employees & projects application. 

The API is live on heroku at [`Staffer App`](https://staffer-udacity.herokuapp.com/)

We are implementing a Jinja templated front end (not part of this project) located at  [`Jinja Frontend`](http://udacity-staffer.herokuapp.com/)

The [`Staffer App`](https://staffer-udacity.herokuapp.com/)

1. Performas CRUD operations on employee and project records
2. Handles user authentication through auth0 tokens
3. Implements access to routes through RBAC (see
[`Permissions and Testing`](./staffer/Auth.md) )

&nbsp;

----

## Setting up the Project

The project runs a Flask server on a [Pipenv](https://docs.pipenv.org/) virtual environment.

A postgresql database and SqlAlchemy handle the data.

&nbsp;

### Before you start:
1. Install [postgresql](https://www.postgresql.org/download/) if needed
2. Install pipenv 

```console
pip install pipenv
```

3. Start your virtual environment with 

```console
pipenv shell
```
4. Install dependencies
```console
pipenv install
```

&nbsp;


### Database Setup
With Postgres running, create the database, create tables, and insert innitial data.
```bash
psql postgres < starting_psql_tester.psql
```
&nbsp;


### Running the flask server

The app will run locally on port 5000.


```bash
python wsgi.py
```

Check the app is running [`locally`](http://localhost:5000).

&nbsp;

### Migrations



## Heroku

