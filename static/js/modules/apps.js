import { Component } from "./base.js";
import { ArticleSet, Steps, Menu} from "./components.js";
import { sleep } from "./tools.js";

export class MenuApp extends Component {
    constructor(jsonPath) {
        super('div', 'menu-app-container');
        this.menu = new Menu(jsonPath);
    }
    renderApp(into) {
        this.menu.load();
        this.menu.render(this.element);
        this.render(into);
    }
}


export class HomePage extends Component {
    constructor() {
        super('div', 'home');
        this.container = new Component('div', 'home-container');
        this.render(this.container.element);
    }
}


export class ArticleViewerApp extends Component {
    constructor(jsonPath) {
        super('div', 'app-container');
        this.articlesSetContainer = new Component('div', 'articles-set-container');
        this.stepsContainer = new Component('div', 'steps-container');
        this.articles = new ArticleSet(jsonPath, this.articlesSetContainer.element);
        this.steps = new Steps('vertical', 'steps-element');
        this.steps.render(this.stepsContainer.element);
        this.stepsContainer.render(this.element)        
        this.articlesSetContainer.render(this.element)
        this.updateSteps = this.updateSteps.bind(this);
    }
    async renderApp(into) {
        await this.articles.load();
        let breakWhile = 3;
        while (
            (this.articles.numberOfArticles === 0  ||
            Object.keys(this.articles.items).length < this.articles.numberOfArticles)) {
            console.debug("Waiting articles rendering...");
            await sleep(1000);
            if (breakWhile === 0) break;
            breakWhile -= 1;
        }
        Object.keys(this.articles.items).forEach((articleId) => {
            this.steps.addItem(this.articles.items[articleId].title, articleId);
        })

        this.render(into);
        this.element.addEventListener('scroll', this.updateSteps);
    }
    updateSteps(){
        for (const articleId in this.steps.items) {
            const stepElement = this.steps.items[articleId].element;
            const articlesElement = this.articles.items[articleId].element
            const halfWindowHeight = window.innerHeight / 2;
            if (!stepElement.classList.contains("step-primary")) {
                if (articlesElement.getBoundingClientRect().top < halfWindowHeight) {
                    this.steps.items[articleId].addClass('step-primary');
                }
            } else {
                if (articlesElement.getBoundingClientRect().top > halfWindowHeight) {
                    this.steps.items[articleId].removeClass('step-primary');
                }
            }
        }
    }
}