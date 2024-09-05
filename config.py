from json import loads
from os import getenv

USERS = loads(getenv('USERS', '[]'))
MESSAGE_FILENAME = getenv('MESSAGE_FILENAME', 'message.json')
