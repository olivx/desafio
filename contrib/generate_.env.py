from django.utils.crypto import get_random_string

""" create .env file"""
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print('create a initial .env file ')
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print('')
print('')
print('')
print('')
print('')

_keys = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
_CONF_FILE = '''
SECRET_KEY={}
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, .localhost
API_TOKEN=essa_não_é_uma_chave_valida
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DB_NAME=travisci
#DB_HOST=127.0.0.1
#DB_PORT=5432
#DB_USER=postgres
#DB_PASSWORD=
#EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
#DEFAULT_FROM_EMAIL=smtp.teste.com
#EMAIL_HOST=teste@email.com
#EMAIL_PORT=587
#EMAIL_USE_TLS=True
#EMAIL_HOST_USER=teste@email.com
#EMAIL_HOST_PASSWORD=you_password
#INTERNAL_IPS=127.0.0.1
'''.format(get_random_string(50, _keys))

with open('.env', 'w') as conf:
    conf.write(_CONF_FILE)

print("***********************************************************")
print('conf file was created with  ')
print("***********************************************************")
print(_CONF_FILE)
print("---------------------------------------------------")
