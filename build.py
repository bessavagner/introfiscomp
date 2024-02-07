import json
from pathlib import Path
from app.articles.processors import DocumentProcessor
from app.utils import extract_title_from_templates
from app.settings import (
    STATIC_DIR,
    TEMPLATES_DIR,
    ARTICLE_TEMPLATE,
    JS_TEMPLATE
)

templates_path = TEMPLATES_DIR
context_path = STATIC_DIR / 'context'

def write_article_template(title, js, path):
    template = ''
    with open(ARTICLE_TEMPLATE, 'r', encoding='utf-8') as html:
        template = html.read()
    template.format(title=title, javascript=js)
    with open(path, 'w', encoding='utf-8') as html:
        html.write(template)

def write_article_js(url, path):
    template = ''
    with open(JS_TEMPLATE, 'r', encoding='utf-8') as js:
        template = js.read()
    template.format(url=url)
    with open(path, 'w', encoding='utf-8') as js:
        js.write(template)

def process_articles():
    articles_path = STATIC_DIR / 'articles'
    for folder_path in articles_path.glob('**/*/'):
        output = folder_path.with_suffix('.json')
        processor = DocumentProcessor(folder_path)
        processor.dump(output, indent=4, ensure_ascii=False)
        # TODO
        # with open(folder_path / '00_meta.md', 'r', encoding='utf-8') as meta:
        #     title = meta.read().rsplit('# ', maxsplit=1)[-1]
        #     template = TEMPLATES_DIR / folder_path.with_suffix('.html').name
        #     javascript = STATIC_DIR / 'js'
        #     javascript /= folder_path.with_suffix('.js')
        #     url = output.relative_to(STATIC_DIR.parent)
        #     write_article_template(title, javascript.name, template)
        #     write_article_js(url, javascript)


def process_context():
    data = {}
    # navbar
    key = 'index'
    data[key] = {}
    filename = context_path / f'{key}.json'
    for folder in templates_path.glob('**/*/'):
        for item in folder.glob('**/*'):
            title = extract_title_from_templates(item)
            file_title = item.relative_to(
                templates_path
            ).with_suffix('').parent
            index, title = str(file_title).rsplit('_', maxsplit=1)
            if index not in data[key]:
                data[key][index] = {}
            if index in data[key]:
                if title not in data[key][index]:
                    data[key][index][title] = []
            path = "/" / item.relative_to(templates_path).with_suffix('')
            subtitle = str(path).rsplit('/', maxsplit=1)[-1]
            subtitle = subtitle.rsplit('_', maxsplit=1)[-1]
            subtitle = subtitle.replace('-', ' ').capitalize()
            # print(index, title, data)
            data[key][index][title].append(
                {
                    "subtitle": subtitle,
                    "path":  str(path)
                }
            )
    data = {
        context: {
            key: value[key] for key in sorted(value)
        } for context, value in data.items()
    }
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    return data

if __name__ == '__main__':
    process_articles()
    process_context()
