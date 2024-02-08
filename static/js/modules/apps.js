import { Component } from "./base.js";
import { ArticleSet, Steps, Menu, Skeleton} from "./components.js";
import { sleep } from "./tools.js";

export class SkeletonApp extends Component {
    constructor(jsonPath) {
        super('div', 'skeleton-app-container');
        this.menu = new Skeleton(4);
    }
    renderApp(into) {
        this.menu.load();
        this.menu.render(this.element);
        this.render(into);
    }
}

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
        this.stepsOuterContainer = new Component('div', 'steps-outer-container');
        this.stepsInnerContainer = new Component('div', 'steps-inner-container');
        this.articles = new ArticleSet(jsonPath, this.articlesSetContainer.element);
        this.steps = new Steps();
        this.steps.render(this.stepsInnerContainer.element);
        this.stepsInnerContainer.render(this.stepsOuterContainer.element);
        this.stepsOuterContainer.render(this.element)        
        this.articlesSetContainer.render(this.element)
        this.updateSteps = this.updateSteps.bind(this);
        this.articlesSetContainer.element.addEventListener('scroll', (event) => {this.updateSteps(event)});
    }
    async renderApp(into) {
        this.render(into);
        await this.articles.load();
        let breakWhile = 40;
        const skeleton = new Skeleton(4);
        skeleton.addItem(4);
        skeleton.addItem(3);
        skeleton.addItem(2);
        for (let i = 0; i <= 18; i++) {
            skeleton.addItem(1);
        }
        skeleton.render(this.articlesSetContainer.element);
        while (
            (this.articles.numberOfArticles === 0  ||
            Object.keys(this.articles.items).length < this.articles.numberOfArticles)) {
            console.debug("Waiting articles rendering...");
            if (breakWhile === 0) {
                skeleton.remove();
                break;
            };
            await sleep(100);
            breakWhile -= 1;
        }
        if (skeleton) skeleton.remove();
        Object.keys(this.articles.items).forEach((articleId) => {
            this.steps.addItem(this.articles.items[articleId].title, articleId);
        })

        
    }
    updateSteps(event) {
        let lastStepId = null;
    
        // Find the ID of the last element with 'step-primary' class
        for (const articleId in this.steps.items) {
            if (this.steps.items[articleId].element.classList.contains('step-primary')) {
                lastStepId = articleId;
            }
        }
    
        // If there's a last step found, scroll it into view
        if (lastStepId !== null) {
            const lastStepElement = this.steps.items[lastStepId].element;
            lastStepElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    
        // Iterate through all steps to update their classes
        for (const articleId in this.steps.items) {
            const stepElement = this.steps.items[articleId].element;
            const articlesElement = this.articles.items[articleId].element;
            const halfWindowHeight = window.innerHeight / 2 + 200;
    
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