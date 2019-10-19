from flask_security import UserMixin, RoleMixin
from flask_security.core import _security
from datetime import datetime
from . import db
import re


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, nullable=False, unique=True)


class User(db.Document, UserMixin):
    url = db.StringField(max_length=75, nullable=False)
    email = db.EmailField(max_length=255, nullable=False, unique=True)
    password = db.StringField(max_length=255, nullable=False)

    # handled by flask-security
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    login_count = db.IntField()
    current_login_at = db.DateTimeField()
    current_login_ip = db.StringField(max_length=45)
    last_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=45)

    roles = db.ListField(db.ReferenceField(Role), default=[])


class File(db.Document):
    filename = db.StringField()
    uploader = db.ReferenceField(User)
    upload_time = db.DateTimeField(default=datetime.now())


class Dump(db.Document):
    filename = db.StringField()
    original_filename = db.StringField()
    message = db.StringField()
    upload_time = db.DateTimeField(default=datetime.now())
    uploader_ip = db.StringField()
    uploader_string = db.StringField()
