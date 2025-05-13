from flask import Flask, render_template
from .config import Config
from .models import db, Package
from flask_migrate import Migrate
from .routes.index import index_bp

app = Flask(__name__)               #initialize flask instace
app.config.from_object(Config)      #load the config class

db.init_app(app)                # bind SQLAlchemy object to the Flask app
migrate = Migrate(app, db)      # link SQLAlchemy, flask, and flask_migrate instance

app.register_blueprint(index_bp)    #bind the blueprit to flask app
