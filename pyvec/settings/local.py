"""
Set variables from config.py that you want to override for local machine.
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG

#DATABASE_ENGINE = 'mysql'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = ''      # Or path to database file if using sqlite3.
#DATABASE_USER = 'root' 


from os.path import dirname,join
LOGGING_CONFIG_FILE = join(dirname(__file__),"logging/development.ini")

from logging.config import fileConfig
fileConfig(LOGGING_CONFIG_FILE)
# ^ FIXME


