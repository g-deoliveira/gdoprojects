from flask import Flask
from config import Config

import boto3

app = Flask(__name__)
app.config.from_object(Config)
app.config["DEBUG"] = True

boto3_client = boto3.client(
    'lambda',
    region_name=app.config['AWS_REGION'],
    aws_access_key_id=app.config['AWS_ACCESS_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY']
)

# this import has to be here
from app import routes

