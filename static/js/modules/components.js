import { cleanText, randomId } from "./tools.js";
import { Component } from "./base.js";

class Paragraph extends Component {
    constructor(text, classList) {
        super('p');
        this.element.innerHTML = text;
        this.element.classList = classList;
    }
}

class ParagraphJustified extends Paragraph {
    constructor(text) {
        super(text, "text-justify");
    }
}

class Lead extends Paragraph {
    constructor(text) {
        super(text, "lead");
    }
}

class Heading extends Component {
    constructor(text, level = "1") {
        if (level < 1 || level > 6) {
            throw new Error(
                "Invalid heading level. Must be between 1 and 6."
            );
        }
        super(`h${level}`);
        this.element.innerText = text;
    }
    setText(text) {
        this.element.innerText = text;
    }
}

class Code extends Component {
    constructor(code) {
        super('code');
        this.element.innerText = code;
    }
}

class PreCode extends Component {
    constructor(code, dataPrefix = "") {
        super('pre');
        this.element.setAttribute("data-prefix", dataPrefix);
        const codeComponent = new Code(code);
        codeComponent.render(this.element);
    }
}

class MockupCode extends Component {
    constructor() {
        super('div');
        this.codeContainer = new Component('div');
        this.codeContainer.element.classList = "mockup-code";
        this.element.classList = "mockup-code-container max-w-full overflow-x-scroll";
        this.codeContainer.render(this.element);
        this.addCodes = this.addCodes.bind(this);
    }
    addCode(code) {
        const dataPrefix = `${this.codeContainer.element.childNodes.length + 1}`;
        const codeComponent = new PreCode(code, dataPrefix);
        codeComponent.render(this.codeContainer.element);
        return this.element;
    }
    addCodes(codes) {
        for (const code of codes) {
            const dataPrefix = `${this.codeContainer.element.childNodes.length + 1}`;
            const codeComponent = new PreCode(code, dataPrefix);
            codeComponent.render(this.codeContainer.element);
        }
        return this.element;
    }
    async addCodesFromFile(path) {
        const configRequest = new Request(path, {
            method: "GET",
            headers: {
                "Content-Type": 'text/txt',
            },
        });
        const response = await fetch(configRequest)
        const text = await response.text();
        const lines = text.split("\n");
        return this.addCodes(lines);
        // try {
        // } catch (error) {
        //     console.error("Error loading code from file:", error);
        // }
    }
}

class Table extends Component {
    constructor(header=null) {
        super('table');
        this.container = new Component('div');
        this.head = new Component('thead');
        this.body = new Component('tbody');
        this.container.setClassList('table-auto');
        const tr = new Component('tr');
        for (const element of header) {
            const th = new Component('th');
            th.setContent(element);
            th.render(tr.element);
        }
        tr.render(this.head.element);
        this.head.render(this.element);
        this.body.render(this.element);
        this.render(this.container.element);
    }
    addRow(row) {
        const tr = new Component('tr');
        for (const data of row) {
            const td = new Component('td');
            td.setContent(data);
            td.render(tr.element);
        }
        tr.render(this.body.element);
    }
}

class Image extends Component {
    constructor(src) {
        super('img');
        const container = new Component('div');
        this.element.src = src;
        this.render(this.container.element);
    }
}

class List extends Component {
    constructor(items=null, type='ul') {
        switch (type) {
            case 'ul':
                super(type);
                break;
            case 'ol':
                super(type);
                break;
            default:
                throw Error("Only 'ul' or 'ol' are accepted as type");
        }
        if (items) {
            if (!Array.isArray(items)) {
                throw Error('Items must be of type Array')
            }
            for (const item of items) {
                this.addItem(item);
            }
        }
        this.addItems = this.addItem.bind(this);
    }
    addItem(item) {
        const li = new Component('li');
        li.setContent(item);
        li.render(this.element);
    }
    addItems(items) {
        for (const item of items) {
            this.addItem(item);
        }
    }
}

class Article extends Component {
    constructor(title = "", leadText = "") {
        super('article');
        this.title = ""
        this.element.id = randomId();
        this.heading = new Heading("", '3');
        this.heading.render(this.element);
        this.element.classList = "prose";
        if (title) { this.setTitle(title); }
        if (leadText) { this.addLead(leadText); }
    }
    
    setTitle(title) {
        this.element.id = cleanText(title);
        this.heading.setText(title);
        this.title = title;
    }
    
    addHeading(title, level) {
        this.heading = new Heading(title, level);
        this.heading.id = cleanText(title);
        this.heading.render(this.element);
    }
    
    addSection(title) {
        this.addHeading(title, '4')
    }

    addSubSection(title) {
        this.addHeading(title, '5');
    }

    addParagraph(text) {
        const p = new ParagraphJustified(text);
        p.render(this.element);
    }

    addLead(text) {
        const p = new Lead(text);
        p.render(this.element);
    }

    addUnorderedList(items) {
        const ul = new List(items, "ul");
        ul.render(this.element);
    }

    addOrderedList(items) {
        const ol = new List(items, "ol");
        ol.render(this.element);
    }

    addCodes(codes) {
        const mockupCode = new MockupCode();
        mockupCode.addCodes(codes);
        mockupCode.render(this.element);
    }
    async addCodeFromFile(path) {
        const mockupCode = new MockupCode();
        await mockupCode.addCodesFromFile(path);
        mockupCode.render(this.element);
    }

    addTable(table) {
        if (!table.thead || !table.tbody) {
            throw Error("Table must have 'thead' and 'tbody' properties");
        }
        const tableComponent = new Table(table.thead);
        for (const row of table.tbody) {
            tableComponent.addRow(row);
        }
        tableComponent.render(this.element);
    }
}

export class Steps extends Component {
    constructor(type='vertical', classList=null) {
        super('ul');
        switch (type) {
            case 'vertical':
                this.setClassList('steps steps-vertical');
                break
            case 'horizontal':
                this.setClassList('steps');
                break;
            default:
                throw Error(
                    "Only 'vertical' or 'horizontal' are accepted as type"
                );
        }
        this.addClass(classList);
        this.items = {}
    }
    addItem(name, idItem) {
        const li = new Component('li');
        const anchor = new Component('a');
        li.setClassList('step');
        li.element.setAttribute('for', idItem);
        anchor.element.setAttribute('href', `#${idItem}`);
        anchor.render(li.element);
        anchor.setContent(name);
        li.render(this.element);
        this.items[idItem] = li;
    }
}

export class ArticleSet {
    constructor(jsonPath, into) {
        this.jsonPath = jsonPath;
        this.parent = into;
        this.items = {};
        this.numberOfArticles = 0;
    }
    async load() {
        const configRequest = new Request(this.jsonPath, {
            method: "GET",
            headers: {
                "Content-Type": 'application/json',
            },
        });
        fetch(configRequest)
            .then(async (response) => {
                if (!response.ok || response.status != 200) {
                    throw Error(
                        `Error (${response.status}): ${response.statusText}`
                    );
                }
                return await response.json();
            })
            .then(async (data) => {
                if (!data.articles) {
                    console.error(`Expected 'articles' attribute: ${data}`);
                    throw Error("Missing 'articles' attribute");
                }
                this.numberOfArticles = Object.keys(data.articles).length;
                for (const articlesData of data.articles) {
                    let article = new Article();
                    if (articlesData.title) {
                        article.setTitle(articlesData.title);
                    }
                    if (articlesData.lead) {
                        article.addLead(articlesData.lead);
                    }
                    if (articlesData.sections) {
                        for (const section of articlesData.sections) {
                            if (section.title) {
                                article.addSection(section.title);
                            }
                            for (const content of section.content) {
                                if (content.mockupCodePath) {
                                    await article.addCodeFromFile(content.mockupCodePath);
                                }
                                if (content.mockupCodes) {
                                    article.addCodes(content.mockupCodes, content.p);
                                }
                                if (content.p) {
                                    article.addParagraph(content.p);
                                }
                                if (content.ul) {
                                    article.addUnorderedList(content.ul);
                                }
                                if (content.ol) {
                                    article.addOrderedList(content.ol);
                                }
                                if (content.table) {
                                    article.addTable(content.table);
                                }
                                if (content.subsection) {
                                    article.addSubSection(content.subsection);
                                }
                            }
                        }
                    }
                    article.render(this.parent);
                    this.items[article.element.id] = article;
                }
            })
            .catch((error) => {
                console.error(error);
            });
    }
}

export class Menu extends Component {
    constructor(jsonPath) {
        super('div', 'menu-container');
        this.ul = new List(null, 'ul');
        this.ul.setClassList('ul-menu');
        this.ul.element.setAttribute('tabindex', "0");
        this.ul.render(this.element);
        this.jsonPath = jsonPath;
    }
    addItems(title, items) {
        if (items) {
            
            if (items.length > 0) {
                if (items.length == 1 && items[0].subtitle) {
                    const anchor = Component('a');
                    const li = new Component('li');
                    if (!items[0].path) throw Error(
                        `'subtitle' and 'title' properties must be provided: ${items[0]}`
                    )
                    anchor.element.setAttribute('href', items[0].path);
                    anchor.render(li.element);
                    this.ul.addItem(anchor.element);
                } else {
                    const detailsComponent = new Component('details');
                    const summary = new Component('summary');
                    const ul = new List(null, 'ul');
                    summary.setContent(title);
                    summary.render(detailsComponent.element);
                    items.forEach((item) => {
                        if (!item.subtitle && !item.path || item.subtitle == null && item.path == null) {
                            throw Error(
                                `'subtitle' and 'title' properties must be provided: ${item}`
                                )
                        }
                        const anchor = new Component('a');
                        // console.log(item.subtitle, item.path);
                        anchor.element.setAttribute('href', item.path);
                        anchor.setContent(item.subtitle);
                        console.log(anchor.element.outerHTML);
                        ul.addItem(anchor.element.outerHTML);
                    })
                    ul.render(detailsComponent.element);
                    detailsComponent.render(this.ul.element);
                }
            }
        }
    }
    load() {
        const configRequest = new Request(this.jsonPath, {
            method: "GET",
            headers: {
                "Content-Type": 'application/json',
            },
        });
        fetch(configRequest)
            .then(async (response) => {
                if (!response.ok || response.status != 200) {
                    throw Error(
                        `Error (${response.status}): ${response.statusText}`
                    );
                }
                return await response.json();
            })
            .then(async (data) => {
                if (!data.index) {
                    console.error(`Expected 'index' attribute: ${data}`);
                    throw Error("Missing 'index' attribute");
                }
                Object.keys(data.index).forEach((key) => {
                    Object.keys(data.index[key]).forEach((title) =>{
                        if (data.index[key][title]) {
                            this.addItems(title, data.index[key][title])
                        }
                    })
                })
            });
    }
}

