import re
import json
from pathlib import Path
from collections import OrderedDict
from app.articles.core import Markers, Article, Document

from .utils import replace_tags, naive_senences


class MarkdownParser:

    def __init__(self, path: str | Path):
        self.path = path
        self.text = self.read_file()

    def read_file(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()

    def parse(self):
        extracting_code = False
        extracting_ol = False

        article = Article()
        article.new_section()

        elements = [element for element in self.text.split('\n') if element]
        if elements[0].split(' ')[0] != Markers.title:
            raise ValueError(
                'Article file should start with title marker "#": '
                f'{self.path}'
            )

        article.title = replace_tags(elements.pop(0).split('#')[-1].strip())

        if elements[0].split(' ')[0] not in Markers.set():
            if len(naive_senences(elements[0])) < 3:
                article.lead = elements.pop(0)
            else:
                article.initial_paragraph = elements.pop(0)

        codes = []
        unordered_list = []
        ordered_list = []
        paragraphs = []
        table = {}

        for idx, line in enumerate(elements):

            if paragraphs:
                if len(paragraphs) == 1:
                    paragraphs[0] = replace_tags(paragraphs[0])
                    article.sections[-1].add_content(texts=paragraphs)
                paragraphs = []

            marker = line.split(' ')[0]
            if marker in Markers.set():
                if marker == Markers.section:
                    article.new_section()
                    article.sections[-1].title = line.split(
                        Markers.section
                    )[-1].strip()
                elif marker == Markers.subsection:
                    title = line.split(Markers.subsection)[-1].strip()
                    article.sections[-1].add_content(subsection=title)
                elif marker == Markers.subsubsection:
                    title = line.split(Markers.subsubsection)[-1].strip()
                    article.sections[-1].add_content(subsubsection=title)
                elif marker == Markers.code:
                    if extracting_code:
                        extracting_code = False
                        if len(codes) > 1:
                            article.sections[-1].add_content(
                                mockup_codes=codes
                            )
                        else:
                            if codes:
                                article.sections[-1].add_content(
                                    mockup_codes=codes[0]
                                )
                        codes = []
                        continue
                    extracting_code = True
                elif marker == Markers.ul:
                    list_item = replace_tags(" ".join(line.split(' ')[1:]))
                    unordered_list.append(list_item)
                    if idx + 1 < len(elements):
                        if elements[idx + 1].split(' ')[0] != Markers.ul:
                            article.sections[-1].add_content(
                                unordered_list=unordered_list
                            )
                            unordered_list = []
                            continue
                    if idx + 1 == len(elements):
                        article.sections[-1].add_content(
                            unordered_list=unordered_list
                        )
                elif marker == Markers.table:
                    if 'header' not in table:
                        table['header'] = [
                            replace_tags(value.strip()) for value in line.split('|') if value
                        ]
                        continue
                    if Markers.table_sep_pattern.findall(line):
                        table['body'] = []
                        continue
                    if 'body' in table:
                        table['body'].append(
                            [
                                replace_tags(value.strip())
                                for value in line.split('|') if value
                            ]
                        )
                        if idx + 1 < len(elements):
                            next_marker = elements[idx + 1].split(' ')[0]
                            if next_marker != Markers.table:
                                article.sections[-1].add_content(table=table)
                                table = {}
                        elif idx + 1 == len(elements):
                            article.sections[-1].add_content(table=table)
            else:
                if extracting_code:
                    codes.append(line)
                else:
                    ol_matches = Markers.ol_pattern.findall(line)
                    if ol_matches:
                        ordered_list.append(replace_tags(ol_matches[0]))
                        if not extracting_ol:
                            extracting_ol = True
                    elif extracting_ol:
                        article.sections[-1].add_content(
                            ordered_list=ordered_list
                        )
                        ordered_list = []
                        extracting_ol = False
                    else:
                        paragraphs.append(line)

        return article


class DocumentProcessor:
    def __init__(self, folder_path: str | Path) -> None:
        self.folder_path = Path(folder_path)
        self.__raw_articles = OrderedDict()
        self.processed = False
        file_paths = sorted(
            self.folder_path.glob("*.md"),
            key=lambda p: int(re.search(r"^(0*)(\d+)_", p.name).group(2))
        )
        for file_path in file_paths:
            filename = file_path.name
            match = re.search(r"^(0*)(\d+)_(.*)\.md$", filename)
            if match and not filename.startswith('00'):
                self.__raw_articles[filename] = ''
        if not self.__raw_articles:
            raise ValueError(
                f"Folder {self.folder_path} doesn't have any "
            )
        self.document = Document()

    @property
    def raw_articles(self,):
        for file_name in self.__raw_articles:
            if not self.__raw_articles[file_name]:
                parser = MarkdownParser(self.folder_path / file_name)
                self.document.add(file_name, parser.parse())
                self.__raw_articles[file_name] = parser.text

            yield self.__raw_articles[file_name]

    def raw_article(self, article_file_name):
        if article_file_name not in self.__raw_articles:
            raise KeyError(
                f"Article file '{article_file_name}' "
                f"not in folder {self.folder_path}"
            )
        if not self.__raw_articles[article_file_name]:
            parser = MarkdownParser(self.folder_path / article_file_name)
            self.document.add(article_file_name, parser.parse())
            self.__raw_articles[article_file_name] = parser.text
        return self.__raw_articles[article_file_name]

    @property
    def articles(self,):
        if not self.document.articles:
            for file_name in self.__raw_articles:
                _ = self.raw_article(file_name)
                yield self.document[file_name]
        else:
            for file_name in self.__raw_articles:
                _ = self.raw_article(file_name)
                yield self.document[file_name]

    def article(self, article_file_name):
        if article_file_name not in self.__raw_articles:
            raise KeyError(
                f"Article file '{article_file_name}' "
                f"not in folder {self.folder_path}"
            )
        if not self.__raw_articles[article_file_name]:
            parser = MarkdownParser(self.folder_path / article_file_name)
            self.document.add(article_file_name, parser.parse())
            self.__raw_articles[article_file_name] = parser.text
            return self.document[article_file_name]
        
        return self.document[article_file_name]

    def process(self,):
        if not self.processed:
            _ = list(self.articles)
            self.processed = True
        return self.document.json()

    def dump(self, path: str | Path, **kwargs):
        if not self.processed:
            self.process()
        self.document.save(path, **kwargs)
