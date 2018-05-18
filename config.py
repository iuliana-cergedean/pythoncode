import os

class Configuration(object):
    DEBUG = True
    PORT = int(os.getenv('PORT','22222'))
    HOST = '129.157.179.180'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://' \
            + os.getenv('MYSQLCS_USER_NAME','Captain') + ':' \
            + os.getenv('MYSQLCS_USER_PASSWORD','welcome1') + '@' \
            + os.getenv('MYSQLCS_CONNECT_STRING', \
            '127.0.0.1:3306/deathstar')
