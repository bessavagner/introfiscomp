import { MenuApp } from "./modules/apps.js";

const path = '/static/context/index.json';
const menuApp = new MenuApp(path);

document.addEventListener("DOMContentLoaded", function () {
    
    console.log('Sanity check: navbar!');
    
    const appElement = document.getElementById('app-menu');
    menuApp.renderApp(appElement);

});