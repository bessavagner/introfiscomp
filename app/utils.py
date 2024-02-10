import re
import unicodedata
from pathlib import Path

from .settings import ARTICLE_TEMPLATE_DIR, JS_TEMPLATE

def extract_title_from_templates(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'{% block title %}(.*?)\{% endblock %}', content, re.DOTALL)
        if match:
            return match.group(1).strip()
        else:
            return None


def normalize_string(input_string):
    # Remove accents
    normalized_string = unicodedata.normalize('NFKD', input_string).encode('ASCII', 'ignore').decode('utf-8')
    # Remove special characters
    normalized_string = re.sub(r'[^\w\s-]', '', normalized_string)
    # Convert to lowercase
    normalized_string = normalized_string.lower()
    # Replace spaces with dashes
    normalized_string = re.sub(r'\s+', '-', normalized_string)
    return normalized_string


def write_article_template(title, js, path):
    template = ''
    with open(ARTICLE_TEMPLATE_DIR, 'r', encoding='utf-8') as html:
        template = html.read()
    with open(path, 'w', encoding='utf-8') as html:
        html.write(template.format(title=title, javascript=js))

def write_article_js(url, path, subfolder=False):
    template = ''
    with open(JS_TEMPLATE, 'r', encoding='utf-8') as js:
        template = js.read()
    with open(path, 'w', encoding='utf-8') as js:
        if subfolder:
            template = template.replace("../modules/apps.js", "../../modules/apps.js")
        js.write(template.format(url=url))
