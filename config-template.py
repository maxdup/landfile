# Landfile configuration
UPLOAD_FOLDER = None

# Flask configuration
DEBUG = True
TEST = False
ENV = 'development'

# WTForm configuration
WTF_CSRF_ENABLED = False

# Mongoengine configuration
MONGODB_DB = 'landfile'
MONGODB_SETTINGS = {
    'db': MONGODB_DB,
    'connect': False,
    'tz_aware': True
}

# Flask-security configuration
# https://pythonhosted.org/Flask-Security/configuration.html

SECRET_KEY = 'super secret'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = 'something_super_secret'
SECURITY_CONFIRM_SALT = 'confirm-salt'
SECURITY_HASHING_SCHEME = ['hex_md5']
SECURITY_DEPRECATED_HASHING_SCHEME = []

SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = True
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True

SECURITY_POST_LOGIN_VIEW = '/'
SECURITY_LOGOUT_URL = '/logout'
SECURITY_LOGIN_URL = '/login'
SECURITY_RESET_URL = '/reset'
SECURITY_CHANGE_URL = '/change'
SECURITY_REGISTER_URL = '/register'
SECURITY_CONFIRM_URL = '/confirm'

SECURITY_REGISTER_USER_TEMPLATE = 'register_user.html'
SECURITY_SEND_CONFIRMATION_TEMPLATE = 'send_confirmation.html'
SECURITY_LOGIN_USER_TEMPLATE = 'login_user.html'
SECURITY_CHANGE_PASSWORD_TEMPLATE = 'change_password.html'
SECURITY_RESET_PASSWORD_TEMPLATE = 'reset_password.html'
SECURITY_FORGOT_PASSWORD_TEMPLATE = 'forgot_password.html'

SECURITY_MSG_EMAIL_CONFIRMED = (
    'Thank you. Your email has been confirmed.', 'success')
SECURITY_MSG_CONFIRMATION_REQUIRED = (
    'Email requires confirmation.', 'error')
SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = (
    'Invalid confirmation token.', 'error')

# Flask-mail configuration
# https://pythonhosted.org/Flask-Mail/#configuring-flask-mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'example@gmail.com'
MAIL_PASSWORD = '--email password--'
MAIL_DEFAULT_SENDER = 'example@gmail.com'
SECURITY_EMAIL_SENDER = 'example@gmail.com'
