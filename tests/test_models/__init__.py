#!/bin/usr/python3
""" creates a unique FileStorage instance for the application"""

from models.engine.file_storage import fileStorage

storage = fileStorage()
storage.reload()