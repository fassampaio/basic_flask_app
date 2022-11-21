
import sys
import logging

logging.basicLogging(stream=sys.stderr)

sys.path.insert(0, '/var/www/basic_flask_app/')

from app import app as application
