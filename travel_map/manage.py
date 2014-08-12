#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    import settings  
    from django.core.management import execute_manager

    execute_manager(settings)