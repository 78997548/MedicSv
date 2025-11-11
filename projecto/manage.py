#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks.

    This file is used by Django's manage commands. To make the script more
    robust when executed from a directory other than the project root, we
    ensure the project parent directory is on sys.path so Python can import
    the `citasMedicas` package regardless of the current working directory.
    """
    # Add project root (MedicSv) to sys.path so `citasMedicas` can be imported
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent
    sys.path.insert(0, str(project_root))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citasMedicas.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Provide a slightly more helpful hint to the user
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment? Try: `Entorno\\Scripts\\Activate.ps1` "
            "or install Django with `pip install django`.") from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
