import os
import signal
from flask import Flask
from app import generator

from utils import setting_statsd, StatsdMiddleware

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

setting_statsd()
app.wsgi_app = StatsdMiddleware(app.wsgi_app, "flask-monitoring")

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=555) # port 5000 is the default