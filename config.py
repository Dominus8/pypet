class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'

    # from sys import platform
    # if platform == "linux" or platform == "linux2":
    #    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'
    # elif platform == "darwin":
    #    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'
    # elif platform == "win32":
    #    SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'
    SECRET_KEY = 'secret 12345'
