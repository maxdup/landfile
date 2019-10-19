from flask_mail import Message
import uuid
from flask import current_app as app, Blueprint, render_template, session, request, send_from_directory, abort, after_this_request
from flask_security import roles_accepted, login_required
from wtforms import Field, StringField, validators
from flask_wtf.file import FileField, FileRequired
from flask_wtf import FlaskForm as BaseForm
from werkzeug.utils import secure_filename
import os

from landfile.models import *


landfile_site = Blueprint('landfile_site', __name__)


class DumpForm(BaseForm):
    uploader_string = StringField(
        'From (optional)',
        validators=[validators.optional()],
        description='Anything like your name, email or phone number')
    message = StringField(
        'Message (optional)',
        validators=[validators.optional()],
        description='A short message or caption')
    dumped_file = FileField(
        'File',
        validators=[FileRequired()])


@landfile_site.route('/', methods=['GET'])
def home():
    return render_template('/index.html')


@landfile_site.route('/dumps/<path:filename>')
@login_required
def dumps(filename):
    # serves dumps as static files, requires login
    try:
        folder = app.config['DUMPS_FOLDER'] or \
            os.path.join(app.instance_path, 'dumps')
        return send_from_directory(folder, filename)
    except Exception as e:
        abort(404)


@landfile_site.route('/dump', methods=['GET', 'POST'])
def dump():
    dump_form = DumpForm()
    if request.method == 'POST' and dump_form.validate():
        dump = save_db_dump(dump_form)
        if app.config['DUMP_NOTIFY_EMAIL']:
            @after_this_request
            def notify_email(response):
                msg_dump = os.path.join(
                    request.url_root, 'dumps', dump.filename)

                msg = Message("LandFile - New file dumped",
                              recipients=[app.config['DUMP_NOTIFY_EMAIL']])

                msg.html = '<p>New dump from:<br/>' +\
                           dump.uploader_string + '</p>' +\
                           '<p>They left this as a message:<br/>' +\
                           dump.message + '</p>' +\
                           '<p>See the file here:<br/><a href="' +\
                           msg_dump + '" >' + msg_dump + '</a></p>'

                mail = app.extensions.get('mail')
                mail.send(msg)
                return response
        return render_template('/dumped.html')

    return render_template('/dump.html', dump_form=dump_form)


def save_db_dump(form):
    f = form.dumped_file.data
    original_filename, extension = os.path.splitext(f.filename)

    # make sure dump directory exists
    dumps_folder = app.config['DUMPS_FOLDER'] or \
        os.path.join(app.instance_path, 'dumps')
    if not os.path.exists(dumps_folder):
        os.makedirs(dumps_folder)

    # create unused filename
    while True:
        filename = secure_filename(str(uuid.uuid4()) + extension)
        if not os.path.exists(os.path.join(dumps_folder, filename)):
            break
    f.save(os.path.join(dumps_folder, filename))

    # save dump in database
    dump = Dump()
    dump.filename = filename
    dump.original_filename = f.filename
    dump.message = form.message.data
    dump.uploader_string = form.uploader_string.data
    dump.uploader_ip = str(request.remote_addr)
    dump.save()

    return dump


def save_db_file(f):
    f = form.dumped_file.data
    filename = secure_filename(f.filename)
    files_folder = app.config['UPLOAD_FOLDER'] or \
        os.path.join(app.static_folder, 'files')
    if not os.path.exists(files_folder):
        os.makedirs(files_folder)
    f.save(os.path.join(files_folder, filename))

    file = File()
    file.filename = filename
    file.uploader = current_user.id
    file.save()

    return file
