import os

DEBUG = os.getenv('DEBUG') in ['True', 'true', '1', 'yes']
if DEBUG:
    SQLALCHEMY_ECHO = True

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

LOG_LEVEL = (os.getenv('LOG_LEVEL') or 'debug').lower()
REDIS_LOG_LEVEL = (os.getenv('REDIS_LOG_LEVEL') or LOG_LEVEL).lower()
SERVICE_NAME = os.getenv('SERVICE_NAME') or 'Pepper'

SECRET_KEY = os.getenv('SECRET_KEY')
NONCE_SECRET = os.getenv('NONCE_SECRET')
HASHIDS_SALT = os.getenv('HASHIDS_SALT')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
HACKATHON_NAME = os.getenv('HACKATHON_NAME')
MLH_APPLICATION_ID = os.getenv('MLH_APPLICATION_ID')
MLH_SECRET = os.getenv('MLH_SECRET')
BASE_URL = os.getenv('BASE_URL')
GENERAL_INFO_EMAIL = os.getenv('GENERAL_INFO_EMAIL')
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
MAILGUN_PUB_KEY = os.getenv('MAILGUN_PUB_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
REGISTRATION_OPEN = os.getenv('REGISTRATION_OPEN') in ['True', 'true', '1', 'yes']
REGISTRATION_CLOSED = os.getenv('REGISTRATION_CLOSED') in ['True', 'true', '1', 'yes']
LETS_ENCRYPT_PATH = os.getenv('LETS_ENCRYPT_PATH')
LETS_ENCRYPT_PATH_CHALLENGE = os.getenv('LETS_ENCRYPT_PATH_CHALLENGE')
CDN_URL = os.getenv('CDN_URL')
FALLBACK_LOCAL_REGISTER = os.getenv('FALLBACK_LOCAL_REGISTER')
CHECK_IN_SECRET = os.getenv('CHECK_IN_SECRET')
FIREBASE_KEY = os.getenv('FIREBASE_KEY')
RESUMES_LINK = os.getenv('RESUMES_LINK')
REDIS_URL = os.getenv('REDIS_URL')
RECOVER_SALT = os.getenv('RECOVER_SALT')
MAX_BATCH_EMAILS = int(os.getenv('MAX_BATCH_EMAILS', '500'))
SENT_ACCEPTANCES = os.getenv('SENT_ACCEPTANCES') in ['True', 'true', '1', 'yes']
KEEN_MAX_RETRIES = int(os.getenv('KEEN_MAX_RETRIES', '3'))
