import os
from flask import Flask
from dotenv import load_dotenv

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
print(APP_ROOT)
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


def config(key, default_value=None):
    if os.getenv(key):
        return os.getenv(key)
    return default_value
