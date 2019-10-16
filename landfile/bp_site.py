from flask import Blueprint, render_template, session
from flask_security import roles_accepted, login_required
from wtforms import BooleanField, Field, HiddenField, PasswordField, \
    StringField, SubmitField, ValidationError, validators
from flask_wtf import FlaskForm as BaseForm


landfile_site = Blueprint('landfile_site', __name__)


class DumpForm(BaseForm):
    message = StringField(u'Message', validators=[
        validators.optional()])
    sender = StringField(u'From', validators=[
        validators.optional()])


@landfile_site.route('/', methods=['GET'])
def home():
    return render_template('/index.html')


@landfile_site.route('/dump', methods=['GET'])
def dump():
    print('dump')
    dump_form = DumpForm()
    return render_template('/dump.html', dump_form=dump_form)
