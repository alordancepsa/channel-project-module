import os
from iniciativa.MLFrameWork import ModelType

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

    ML_MODELS=[
         {
            "NAME": "MODEL_SALES_PREDICT",
            "type": ModelType.LOCAL_MODEL,
            "URL": 'https//.....'
         },
         {

            "NAME": "MODEL_REMOTE_SALES_PREDICT",
            "type": ModelType.REMOTE_MODEL,
            "endpoint": 'https//.....',
            "headers": {"api-id": "asdasd", "api-key": "asasdasdasdñlakdsñlk"}
         },

        {
            "NAME": "MODEL_LOCAL_SALES_USING_TF_LIKE_MODELS",
            "type": ModelType.LOCAL_TF_MODEL,
            "SCHEMA_URL": 'https//.....',
            "WEIGTH_URL": 'https//.....'
        }
        # ...
    ]
