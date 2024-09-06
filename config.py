from json import loads
from os import getenv

USERS = loads(getenv('USERS', '[]'))
