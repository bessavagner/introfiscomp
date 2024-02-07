from pathlib import Path

ROOT_DIR = Path(__name__).resolve().parent
STATIC_DIR = ROOT_DIR / 'static'
TEMPLATES_DIR = ROOT_DIR / 'templates'
ARTICLE_TEMPLATE = TEMPLATES_DIR / '.articles.html.templates'
JS_TEMPLATE = STATIC_DIR / 'js/.js.template'
