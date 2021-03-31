import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow
from iniciativa.MLFrameWork.load_models import load_app_models

from ..config import Config


app = Flask(__name__)
CORS(app, intercept_exceptions=False,  resources={r"/*": {"origins": "*"}})

app.config.from_object(Config)
    
db = SQLAlchemy()
db.init_app(app)
api = Api(app)
swagger = Swagger(app)

ma = Marshmallow(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# LOADING_APP_MODELS
appModels = load_app_models(Config.ML_MODELS)








# manager.handle(__name__, ["db", "upgrade"])


# from sqlalchemy import create_engine

# cluster_arn = "arn:aws:rds:us-east-1:123456789012:cluster:my-aurora-serverless-cluster"
# secret_arn = "arn:aws:secretsmanager:us-east-1:123456789012:secret:MY_DB_CREDENTIALS"

# app = Flask(app_name)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+auroradataapi://:@/my_db_name'
# engine_options=dict(connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))
# db = flask_sqlalchemy.SQLAlchemy(app, engine_options=engine_options)
