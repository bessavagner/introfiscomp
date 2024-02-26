import re
import json
from typing import List
from pathlib import Path


class Markers:
    
    title: str = "#"
    section: str = "##"
    subsection: str = "###"
    subsubsection: str = "####"
    code: str = "```"
    ul: str = "-"
    table: str = "|"
    image: str = "!"
    ol_pattern: re.Pattern = re.compile(r'^\d+\.\s*(.+)$', re.MULTILINE)
    table_sep_pattern: re.Pattern = re.compile(r'-{2,}')
    image_path_pattern: re.Pattern = re.compile(
        r'!\[.*?\]\((.+?)(?:\s+".+?")?\)'
    )

    @classmethod
    def set(cls):
        return {
            cls.title,
            cls.section,
            cls.subsection,
            cls.subsubsection,
            cls.code,
            cls.ul,
            cls.table,
            cls.image
        }


class Content:
    def __init__(self, ) -> None:
        self.elements: List[dict] = []

    def add_paragraph(self, text: str) -> None:
        self.elements.append({"p": text})

    def add_paragraphs(self, texts: List[str]) -> None:
        self.elements.extend([{"p": text} for text in texts])

    def add_mockup_code(self,
                        mockup_code: str,
                        language: str,
                        paragraph: str = None):
        content = {}
        if paragraph:
            content["p"] = paragraph
        content["mockupCode"] = {
            "code": mockup_code,
            "language": language
        }
        self.elements.append(content)

    def add_mockup_codes(self,
                         mockup_codes: List[str],
                         language: str,
                         paragraph: str = None):
        content = {}
        if paragraph:
            content["p"] = paragraph
        content["mockupCodes"] = {
            "codes": mockup_codes,
            "language": language
        }
        self.elements.append(content)

    def add_unordered_list(self, items: List[str]):
        self.elements.append({"ul": items})

    def add_ordered_list(self, items: List[str]):
        self.elements.append({"ol": items})

    def add_table(self, header: List[str], rows: List[List]):
        if not all(len(header) == len(row) for row in rows):
            raise ValueError('Rows must have same length as header')
        self.elements.append(
            {
                "table": {"thead": header, "tbody": rows},
            }
        )

    def add_image(self, path: str):
        self.elements.append({'img': path})


class Section:
    def __init__(self, title: str = None):
        self.title = title
        self.content = Content()

    def add_content(self,
                    mockup_codes: str | List[str] = None,
                    language: str = None,
                    texts: str | List[str] = None,
                    unordered_list: List[str] = None,
                    ordered_list: List[str] = None,
                    table: dict[str, List] = None,
                    image: str = None,
                    subsection: str = None,
                    subsubsection: str = None):
        if texts:
            if isinstance(texts, list):
                if len(texts) == 1:
                    self.content.add_paragraphs(texts)
                else:
                    self.content.add_paragraph(texts[0])
            elif isinstance(texts, str):
                self.content.add_paragraph(texts)
        if mockup_codes:
            if isinstance(mockup_codes, list):
                self.content.add_mockup_codes(mockup_codes, language=language)
            elif isinstance(mockup_codes, str):
                self.content.add_mockup_code(mockup_codes, language=language)
        if unordered_list:
            self.content.add_unordered_list(unordered_list)
        if ordered_list:
            self.content.add_ordered_list(ordered_list)

        if table:
            try:
                self.content.add_table(table["header"], table["body"])
            except KeyError as err:
                raise KeyError(
                    "'table' must have 'header' and 'body' keys"
                ) from err
        if image:
            self.content.add_image(image)
        if subsection:
            self.content.elements.append({"subsection": subsection})

        if subsubsection:
            self.content.elements.append({"subsubsection": subsubsection})

    def json(self,) -> dict:
        return {
            "title": self.title,
            "content": self.content.elements
        }


class SubSection(Section):
    ##TODO
    def __init__(self, title: str = None):
        super().__init__(title)

    def add_to(self, section: Section):
        section.elements.append(
            {
                "subsection": {
                    "title": self.title,
                    "content": self.content
                }
            }
        )
        return section


class Article:
    def __init__(self,
                 title: str = None, lead: str = None,
                 initial_paragraph: str = None) -> None:
        self.title = title
        self.lead = lead
        self.initial_paragraph = initial_paragraph
        self.sections: List[Section] = []

    def new_section(self, ) -> None:
        self.sections.append(Section())

    def new_content(self,
                    mockup_codes: str | List[str] = None,
                    texts: str | List[str] = None) -> None:
        """Add conents to `Content` attribute of las section"""
        self.sections[-1].add_content(mockup_codes, texts)

    def add_section(self, title: str, content: Content) -> None:
        section = Section(title=title)
        section.content = content
        self.sections.append(section)

    def json(self,) -> dict:
        data = {
            "title": self.title,
            "sections": [section.json() for section in self.sections]
        }
        if (self.lead):
            data["lead"] = self.lead
        return data

    def save(self, path: str | Path):
        data = self.json()
        with open(path, 'w', encoding='utf-8') as out:
            json.dump(self.json(), out, indent=4)
        return data

    def load(self, path: str | Path):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        self.title = data['title'],
        self.lead = data.get('lead'),
        self.initial_paragraph = data.get('initialParagraph')

        for section_data in data['sections']:
            section = Section(title=section_data['title'])
            section.content.elements = section_data['content']
            self.add_section(section.title, section.content)

        return self


class Document:

    def __init__(self) -> None:
        self.articles: dict[str, Article] = {}

    def add(self, key: str, article: Article):
        self.articles[key] = article

    def json(self,):
        return {
            "articles": [article.json() for article in self.articles.values()]
        }

    def save(self, path: str | Path, **kwargs):
        data = self.json()
        with open(path, 'w', encoding='utf-8') as out:
            json.dump(self.json(), out, **kwargs)
        return data

    def __getitem__(self, key: str) -> Article:
        """
        Retrieves an article by key.
        """
        return self.articles[key]
