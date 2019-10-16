from flask import Blueprint, render_template, session
from flask_security import roles_accepted, login_required

landfile_site = Blueprint('landfile_site', __name__)


@landfile_site.route('/', methods=['GET'])
def home():
    return render_template('/index.html')
