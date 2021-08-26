#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login.settings")

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
    except:

        print("Django is probably not installed (or installed properly), visit the bottom of README.md for tutorial on how to install Django")

        # Remove the above try/except to view full error message in terminal
