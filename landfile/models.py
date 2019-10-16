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
    last_login_at = db.DateTimeField()
    current_login_at = db.DateTimeField()
    last_login_ip = db.StringField(max_length=45)
    current_login_ip = db.StringField(max_length=45)
    login_count = db.IntField()

    roles = db.ListField(db.ReferenceField(Role), default=[])


class Dump(db.Document):
    filename = db.StringField()
    message = db.StringField()
    uploader = db.ReferenceField(User)
    uploader_ip = db.StringField()
    upload_time = db.DateTimeField()
