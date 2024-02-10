import logging
import json
from app.articles.processors import DocumentProcessor
from app.utils import (
    write_article_template,
    write_article_js
)
from app.settings import (
    STATIC_DIR,
    ARTICLES_DIR,
    JAVASCRIPT_PROCESSED_DIR,
    ARTICLES_PROCESSED_DIR,
    TEMPLATES_PROCESSED_DIR,
    CONTEXT_PATH_DIR
)

logger = logging.getLogger('client')

def process_data():
    """
        Process data to build pages at client side.

        - Parse articles 'manuscripts' (.md files) into
        json.
        - Generate .js and .html files (those are the ones client
        uses to build page.)
        - Save article's content (article pages's lateral menu).

        'ARTICLES_DIR' must contain the following structure:
        
        ```
        /static/articles/
                |_ 01_content
                    |_ 00_meta.md
                    |_ 01_article
                        |_ 00_meta.md
                        |_ 01_section.md
                        |_ 02_section.md
                |_ 02_content
                    |_ 00_meta.md
                    |_ 01_section.md
                    |_ 02_section.md

        ```
            - Every folder must contain a file named `00_meta.md`.
            - The `00_meta.md` must contain the title to the content
            or article: "# Title of The Content Or Article
    """
    JAVASCRIPT_PROCESSED_DIR.mkdir(exist_ok=True)
    ARTICLES_PROCESSED_DIR.mkdir(exist_ok=True)
    TEMPLATES_PROCESSED_DIR.mkdir(exist_ok=True)
    ROOT = STATIC_DIR.parent
    FOLDERS = ARTICLES_DIR.relative_to(ROOT).glob('*/')
    META_FILE_NAME = '00_meta.md'

    menu = {}
    logger.info(">>> Starting processing")
    for folder in sorted(FOLDERS):
        index = str(folder.name).rsplit("_", maxsplit=1)[0]
        if index not in menu:
            menu[index] = {}
        with open(folder / META_FILE_NAME, 'r', encoding='utf-8') as meta:
            lines = meta.read().split('\n')
            title = lines[0].rsplit('#', maxsplit=1)[-1]
            menu[index]["title"] = title
            logger.info(">>> Processing %s", title)
        lista = list(folder.glob('*/'))
        if lista:
            menu[index]["sections"] = []
            for item in sorted(lista):
                section_data = {}
                with open(
                    item / META_FILE_NAME, 'r', encoding='utf-8'
                ) as meta:
                    lines = meta.read().split('\n')
                    section_title = lines[0].rsplit('#', maxsplit=1)[-1]
                    section_data["title"] = section_title
                    logger.info("\t|___Processing %s", section_title)
                name = item.with_suffix('.json').name
                directory = ARTICLES_PROCESSED_DIR / folder.name
                directory.mkdir(parents=True, exist_ok=True)
                dump_to = directory / name
                processor = DocumentProcessor(item)
                processor.dump(dump_to, indent=4, ensure_ascii=False)
                section_data["jsonPath"] = str(
                    dump_to.relative_to(ARTICLES_PROCESSED_DIR.parent)
                )
                section_data["url"] = str(
                    dump_to.relative_to(ARTICLES_PROCESSED_DIR).with_suffix('')
                )
                js_path = JAVASCRIPT_PROCESSED_DIR / section_data["url"]
                js_path.parent.mkdir(parents=True, exist_ok=True)
                write_article_js(
                    f"{section_data['jsonPath']}",
                    js_path.with_suffix('.js'),
                    subfolder=True
                )
                template_path = TEMPLATES_PROCESSED_DIR / section_data["url"]
                template_path.parent.mkdir(parents=True, exist_ok=True)
                write_article_template(
                    section_data["title"],
                    js_path.relative_to(STATIC_DIR).with_suffix('.js'),
                    template_path.with_suffix('.html')
                )
                section_data["jsonPath"] = f"/{section_data['jsonPath']}"
                section_data["url"] = f"/{section_data['url']}"
                menu[index]["sections"].append(section_data)
                logger.info("\t|___%s processed!", section_title)
        else:
            name = folder.with_suffix('.json').name
            directory = ARTICLES_PROCESSED_DIR
            processor = DocumentProcessor(folder)
            dump_to = directory / name
            processor.dump(dump_to, indent=4, ensure_ascii=False)
            menu[index]["jsonPath"] = str(
                dump_to.relative_to(ARTICLES_PROCESSED_DIR.parent)
            )
            menu[index]["url"] = str(
                dump_to.relative_to(ARTICLES_PROCESSED_DIR).with_suffix('')
            )
            js_path = JAVASCRIPT_PROCESSED_DIR / menu[index]["url"]
            js_path.parent.mkdir(parents=True, exist_ok=True)
            write_article_js(
                f"{menu[index]['jsonPath'] }", js_path.with_suffix('.js')
            )
            template_path = TEMPLATES_PROCESSED_DIR / menu[index]["url"]
            write_article_template(
                menu[index]["title"],
                js_path.relative_to(STATIC_DIR).with_suffix('.js'),
                template_path.with_suffix('.html')
            )
            menu[index]["jsonPath"] = f"/{menu[index]['jsonPath']}"
            menu[index]["url"] = f"/{menu[index]['url']}"
            logger.info("\t|___%s processed!", title)

    with open(
        CONTEXT_PATH_DIR / 'index.json', 'w', encoding='utf-8'
    ) as json_file:
        json.dump({"index": menu}, json_file, indent=4, ensure_ascii=False)
    logger.info(">>> Processing finished!")

if __name__ == '__main__':
    logger.info("> Build process started.")
    process_data()
    logger.info("> Build process finished!")
