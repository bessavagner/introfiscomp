import { ArticleViewerApp } from "./modules/apps.js";

const path = "/static/articles/01_algoritimos.json";
const app = new ArticleViewerApp(path);

document.addEventListener("DOMContentLoaded", async function () {
    
    console.log('Sanity check!');
    
    const appElement = document.getElementById('app');
    await app.renderApp(appElement);
});
