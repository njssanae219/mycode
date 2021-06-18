#!/usr/bin/env python3

from flask import Flask
from celerytask import celery1

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqps://xicbpsnc:Sr32LS7_SAxgHvjpRBJDamQDX4n2M2nE@fish.rmq.cloudamqp.com/xicbpsnc'
app.config['CELERY_BACKEND'] = 'amqps://xicbpsnc:Sr32LS7_SAxgHvjpRBJDamQDX4n2M2nE@fish.rmq.cloudamqp.com/xicbpsnc'

celery = celery1(app)

@app.route('/process/<name>')
def process(name):
    return name

@celery.task(name='celeryconfig.reverse')
def reverse(string):
    return string[::-1]

if __name__== "__main__":
    app.run(host="0.0.0.0", port=2224)
