import os

class Config(object):

    # to use CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # to run the lambda
    AWS_ACCESS_ID = os.environ.get('AWS_ACCESS_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.environ.get('AWS_REGION')
