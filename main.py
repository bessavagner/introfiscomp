import logging
from pathlib import Path
from asgiref.wsgi import WsgiToAsgi
from flask import Flask, send_from_directory
from flask import render_template

from app.settings import TEMPLATES_DIR, STATIC_DIR

flask_app = Flask(__name__)
asgi_flask_app = WsgiToAsgi(flask_app)

logger = logging.getLogger('default')

@flask_app.route("/")
def serve_home():
    template = "home.html"
    return render_template(template)

@flask_app.route("/<path:name>")
def serve_section(name):
    template = f"{name}.html"
    return render_template(template)

@flask_app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == "__main__":
    flask_app.run()
