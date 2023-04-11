# Todo

Todo is a web application developed in Python using [Django](https://www.djangoproject.com/) and [Bootstrap](https://getbootstrap.com/docs/), designed to keep track of tasks.

## Features

- The website has a fully functioning authentication system connected to the SQLite database. The sign up and login pages have been implemented using Django forms. Upon registration username and password are validated.
- Todo objects are implemented using a model. Todos of all users are kept in the database and access to them is restricted to the user and the admin only. Todos can be created, updated, and deleted. Database entries will be automatically updated when the user changes the state of their todos.
- Front end desing of the website has been done using bootstrap framework and is kept minimalistic.

## Local Installation

To run the application you will need to install the dependencies outlined in [requirements.txt](requirements.txt). For convenience, you can use Python's `venv` package to install dependencies in a virtual environment. You can find the instructions on creating and activating a virtual environment in the official [documentation](https://docs.python.org/3.10/library/venv.html). After setting up and activating your environment, you can install the dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

You can then run the application by executing the following command in your terminal:

```bash
manage.py runserver
```


## License

This repository is licensed under the terms of [MIT License](LICENSE).
