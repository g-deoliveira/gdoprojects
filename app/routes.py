from flask import render_template, redirect, url_for
import json

from app import app
from app.forms import UrlForm

from app import boto3_client

from config import Config

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/newsworthy', methods=['GET', 'POST'])
def newsworthy():
    form = UrlForm()
    if form.validate_on_submit():
        url = form.url.data

        payload = {'url':url}

        result = boto3_client.invoke(
            FunctionName='is-website-newsworthy',
            InvocationType='RequestResponse',
            Payload=json.dumps(payload)
        )
        response = result['Payload'].read()

        prediction, times = parse_response(response)
    else:
        prediction = None
        times = None

        #return redirect(url_for('index'))
    return render_template('url.html', title='NewsWorthy', form=form, prediction=prediction, times=times)

def parse_response(response):

    # convert bytearray to dictionary
    response = json.loads(response)

    prediction = response.get('prediction')

    times = response.get('times', {})

    return prediction, times