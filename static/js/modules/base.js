export class Component {
    constructor(tag, classList=null) {
        this.tagName = tag;
        this.element = document.createElement(tag);
        this.rendered = false;
        if (classList) {
            this.setClassList(classList);
        }
    }
    setId(id) {
        this.element.id = id;
    }
    setContent(content) {
        this.element.innerHTML = content;
        return this.element;
    }
    setClassList(classList) {
        this.element.classList = classList;
    }
    addClass(classList) {
        this.element.classList += ` ${classList}`;
    }
    removeClass(classItem) {
        this.element.classList.remove(classItem);
    }
    setStyle(style) {
        this.element.style = style;
    }
    render(into, how = 'a', before = null) {

        /* Renders element as child of 'into'
            into (element): parent
            how (string): how to insert
                a - appendChild
                b - insertBefore
                r - replaceChild
        */
        if (into) {
            switch (how) {
                case 'a':  // Append as child
                    into.appendChild(this.element);
                    break;
                case 'b':  // Insert before another child
                    into.insertBefore(this.element, before);
                    break;
                case 'r':  // Replace an existing child
                    if (before) {
                        into.replaceChild(this.element, before);
                        break;
                    }
                    throw new Error(
                        "Cannot replace child without a 'before' element"
                    );
                default:
                    throw new Error(`Invalid insertion method: ${how}`);
            }
            this.rendered = true;
            return this.element;
        }
        throw new Error(
            `A parent element must be provided to argument 'into'`
        );
    }
    remove(){
        this.element.remove();
    }
}