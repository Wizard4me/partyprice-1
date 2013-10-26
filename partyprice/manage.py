#!/usr/bin/env python
#66666d
import os
import sys

#3
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "partyprice.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
