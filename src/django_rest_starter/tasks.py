# Due the usage of Windows, without pty support, we need to use subprocess.run instead of invoke
# More info in the issue:  https://github.com/pyinvoke/invoke/issues/561
import subprocess

def start():
    """Run the Django development server."""
    subprocess.run(["poetry", "run", "python", "src/manage.py", "runserver"], check=True)

def migrate():
    """Apply database migrations."""
    subprocess.run(["poetry", "run", "python", "src/manage.py", "migrate"], check=True)

def test():
    """Run Django tests."""
    subprocess.run(["poetry", "run", "python", "src/manage.py", "test"], check=True)
