import os
from pathlib import Path

from dotenv import load_dotenv


# Loads variables from .env file
load_dotenv()


ROOT_DIR = Path(__name__).resolve().parent
STATIC_DIR = ROOT_DIR / 'static'
TEMPLATES_DIR = ROOT_DIR / 'templates'
ARTICLES_DIR = STATIC_DIR / 'articles'
IMAGES_DIR = STATIC_DIR / 'images'
ARTICLE_TEMPLATE_DIR = TEMPLATES_DIR / '.articles.html.templates'
JS_TEMPLATE = STATIC_DIR / 'js/.js.template'
JAVASCRIPT_PROCESSED_DIR = STATIC_DIR / 'js' / 'processed'
ARTICLES_PROCESSED_DIR = STATIC_DIR / 'articles_processed'
TEMPLATES_PROCESSED_DIR = TEMPLATES_DIR / 'processed'
CONTEXT_PATH_DIR = STATIC_DIR / 'context'

SECRETS = os.environ.get(
    "SECRETS",
    default="INSECURE-X3azliUf7INg018n-oBUFl94530UhYuahdvJmwxYKwE"
)
APP_NAME = os.environ.get("APP_NAME", default="app")
APP_DIR = os.environ.get("APP_DIR", default=".")
APP_PORT = int(os.environ.get("APP_PORT", default="5000"))
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS", default="http://0.0.0.0:5000, https://0.0.0.0:5000"
)
DEBUG = bool(os.environ.get("DEBUG", default=True))

HOST = ALLOWED_HOSTS.split(', ')[0].split('//')[1].split(':')[0]
