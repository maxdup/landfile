from flask import current_app as app, Blueprint, render_template, session, request
from flask_security import roles_accepted, login_required
from wtforms import Field, StringField, validators
from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm as BaseForm
from werkzeug.utils import secure_filename
import os


landfile_site = Blueprint('landfile_site', __name__)


class DumpForm(BaseForm):
    sender = StringField('From (optional)', validators=[validators.optional()],
                         description='Anything like your name, email or phone number')
    message = StringField('Message (optional)', validators=[validators.optional()],
                          description='A short message or caption')
    dumped_file = FileField('File', validators=[FileRequired()])


@landfile_site.route('/', methods=['GET'])
def home():
    return render_template('/index.html')


@landfile_site.route('/dump', methods=['GET', 'POST'])
def dump():
    form = DumpForm()
    if request.method == 'POST' and form.validate():
        f = form.dumped_file.data
        filename = secure_filename(f.filename)
        print(dir(app))
        dumps_folder = app.config['UPLOAD_FOLDER'] or \
            os.path.join(app.static_folder, 'files')
        f.save(os.path.join(dumps_folder, filename))
        return render_template('/dumped.html')

    dump_form = DumpForm()
    return render_template('/dump.html', dump_form=dump_form)
