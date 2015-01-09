#!/usr/bin/python
import os, sys
import logging

PROJECT_DIR = '/var/www/FlaskApp/FlaskApp/'

activate_this = os.path.join(PROJECT_DIR, 'venv', 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = '657483920owiejhrfgbvnc;'
