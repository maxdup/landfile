from flask import Flask
from flask_restplus import Api
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, \
    auth_token_required
from flask_mail import Mail
from flask_cors import CORS

db = MongoEngine()

from landfile.models import User, Role  # NOQA: E402

from landfile.bp_site import landfile_site   # NOQA: E402
#from landfile.bp_api import landfile_api   # NOQA: E402


def create_app(config):
    app = Flask(__name__, static_folder='static')

    app.config.from_object(config)
    app.url_map.strict_slashes = False

    app.register_blueprint(landfile_site)
    # app.register_blueprint(landfile_api)

    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    mail = Mail(app)
    db.init_app(app)

    CORS(app)
    return app
