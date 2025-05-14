# Django REST Starter

This is a starter project for building a backend application using Django and Django REST Framework.

## Features

- **Django**: A high-level web framework for Python. (v. 5)
- **Django REST Framework**: Toolkit for building Web APIs in Django. (v.3)
- **autopep8**: Code formatter for Python. (v. 2)

## Prerequisites

1. Install [Python](https://www.python.org/downloads/) (3.8+ recommended)
2. Review if [pip](https://pip.pypa.io/) is installed: `python -m pip --version`, usually is installed with Python.
3. Install [pipx](https://pipx.pypa.io/) for global tool installation (recommended)

```sh
python -m pip install --user pipx
pipx ensurepath
# Restart your terminal
```

4. Install [Poetry](https://python-poetry.org/) and [Poe the Poet](https://poethepoet.natn.io/) for script automation.

```sh
pipx install poetry poethepoet
```

5. (optional) Configuring Poetry to use in-project virtualenvs, keeps your `.venv` inside the project directory.

```sh
poetry config virtualenvs.in-project true
```

## Getting Started

1. Clone the repository:

```sh
git clone https://github.com/jhordyess/django-rest-starter.git
```

2. Navigate to the project directory:

```sh
cd django-rest-starter
```

3. Install dependencies:

```sh
poetry install
```

4. Start the development server:

```sh
poe dev
```

5. Open your browser or API client and interact with the server running at <http://localhost:8000>.

## Project Structure

```txt
django-rest-starter/
├── .gitignore      # List of files and directories to be ignored by version control.
├── manage.py       # Django management script.
├── poetry.lock     # Poetry lock file for dependencies.
├── pyproject.toml  # Project configuration and dependencies.
├── README.md       # Project documentation.
├── api/            # Django app for API logic
├── app/            # Django project settings and URLs
├── tests/          # Directory for test cases
```

## Commands

### Start the development server

```sh
poe dev
```

### Run Django management commands

```sh
poe manage <command>

# Example: Create migrations
poe manage makemigrations
# Example: Apply migrations
poe manage migrate
# Example: Create a superuser
poe manage createsuperuser
```

### Format the code

```sh
poe format
```

## Contributing

Contributions are welcome! If you find any issues or want to enhance the project, feel free to submit a pull request.

---

Happy hacking!
