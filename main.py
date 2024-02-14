import logging
from pathlib import Path
from functools import wraps

from asgiref.wsgi import WsgiToAsgi
from flask import Flask, send_from_directory
from flask import render_template
from flask import make_response
from flask_cors import CORS

from app.settings import STATIC_DIR
from app.settings import SECRETS
from app.settings import ALLOWED_HOSTS
from app.settings import DEBUG

logger = logging.getLogger('client')

def set_cors_headers(route_function):
    @wraps(route_function)
    def decorated_function(*args, **kwargs):
        response = route_function(*args, **kwargs)
        response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
        response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
        response.headers['Cross-Origin-Resource-Policy'] = 'cross-origin'
        return response
    return decorated_function


flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = SECRETS

if not DEBUG and "INSECURE" in SECRETS:
    raise RuntimeError(
        "When 'DEBUG' is se to True, you must provide a "
        "secure key."
    )

CORS(flask_app, resources={r"/*": {"origins": ALLOWED_HOSTS}})
asgi_flask_app = WsgiToAsgi(flask_app)

@flask_app.route("/")
@set_cors_headers
def serve_home():
    template = "home.html"
    response = make_response(render_template(str(template)))
    return response

@flask_app.route("/<path:name>")
@set_cors_headers
def serve_section(name):
    template = Path('processed') / f"{name}.html"
    response = make_response(render_template(str(template)))
    return response

@flask_app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == "__main__":
    flask_app.run()
