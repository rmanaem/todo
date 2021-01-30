# Todo Web Application

Todo is a web application developed in Python3 using Django framework, designed to keep track of tasks, goals, etc.

## Installation

If you do not have Python3 installed, you can download it [here](https://www.python.org/downloads/).

Create a virtual environment, you can use [virtualenv](https://pypi.org/project/virtualenv/) package.

Install the requirements:

```
pip install -r requirements.txt
```

Run the application:

```
manage.py runserver
```

## Features

- The website has a fully functioning authentication system connected to the SQLite database. The sign up and login pages have been implemented using Django forms. Upon registration username and password are validated.
- Todo objects are implemented using a model. Todos of all users are kept in the database and access to them is restricted to the user and the admin only. Todos can be created, updated, and deleted. Database entries will be automatically updated when the user changes the state of their todos.
- Front end desing of the website has been done using bootstrap framework and is kept minimalistic.

## Refrences

[Python](https://www.python.org/doc/)

[Virtualenv](https://virtualenv.pypa.io/)

[Django](https://docs.djangoproject.com/)

[Bootstrap](https://getbootstrap.com/docs/)

## License

This repository is licensed under the [MIT License](https://github.com/rmanaem/todo-app/blob/master/LICENSE).
