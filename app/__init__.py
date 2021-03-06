from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db) 

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

from app.models import tabela,formulario
from app.models.tabela import User
from app.controllers import webapp




