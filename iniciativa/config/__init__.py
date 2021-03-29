import os

localDL = 'sqlite:///../../.database/dl.db'
localApp = 'sqlite:///../../.database/app.db'

def getCryptedEnvars(key, defaultvalue):
    env = os.environ.get('ENV', 'local')

    ## TODO ask to secretmanager for envar with key
    return defaultvalue

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=getCryptedEnvars('app_uri', localApp)
    SQLALCHEMY_BINDS={
            'datalake': getCryptedEnvars('datalake_uri', localDL)
            }
