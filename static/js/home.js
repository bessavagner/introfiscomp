import { MenuApp } from "./modules/apps.js";

const path = '/static/context/index.json';
const menuApp = new MenuApp(path);

document.addEventListener("DOMContentLoaded", function () {
    
    console.log('Sanity check: home!');
    
    const appElement = document.getElementById('dropdown-hero');
    console.log(appElement);
    menuApp.menu.ul.setClassList('ul-menu-hero');
    menuApp.renderApp(appElement);

});