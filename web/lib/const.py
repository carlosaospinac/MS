import os


_ = os.getenv

DB_HOST = _('DB_HOST')
DB_USER = _('DB_USER')
DB_PASSWORD = _('DB_PASSWORD')
DB_NAME = _('DB_NAME')
REDIS_HOST = _('REDIS_HOST')
REDIS_PASSWORD = _('REDIS_PASSWORD')
REDIS_PREFIX = _('APP_NAME')
SECRET_KEY = _('SECRET_KEY', 'my_precious')
DEFAULT_ROUNDS = int(_('DEFAULT_ROUNDS', '15'))
ACCESS_TOKEN_KEY = _('ACCESS_TOKEN_KEY', '')
REFRESH_ACCESS_TOKEN_KEY = _('REFRESH_ACCESS_TOKEN_KEY', '')
TOKEN_EXPIRATION_SEC = int(_('TOKEN_EXPIRATION_SEC', '30'))
