

// Found the code to move the items around at this Source: https://htmldom.dev/drag-and-drop-element-in-a-list/
document.addEventListener('DOMContentLoaded', function() {
    // this is used to test if the javascript is connected to the .html correctly.
    document.querySelector('#test').innerHTML = "Bella"

    // Query the list element
    const list = document.getElementById('list');

    // Query all items
    [].slice.call(list.querySelectorAll('.draggable')).forEach(function(item) {
        item.addEventListener('mousedown', touchStartHandler);
        item.addEventListener('touchstart', touchStartHandler, false);
    });

});

// The current dragging item
let draggingEle;

// The current position of mouse relative to the dragging element
let x = 0;
let y = 0;

let placeholder;
let isDraggingStarted = false;



const touchStartHandler = function(e) {
    draggingEle = e.target;
    draggingEle.style.backgroundColor = 'Gray';

    // Calculate the mouse position
    const rect = draggingEle.getBoundingClientRect();
    // x = e.pageX - rect.left;
    x = e.pageX;
    y = e.pageY-rect.top-window.scrollY;

    // stop the page from scrolling when dragging.
    // document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow = 'hidden';
    e.preventDefault();

    // Attach the listeners to `document`
    document.addEventListener('mousemove', touchMoveHandler);
    document.addEventListener('mouseup', touchEndHandler);
    document.addEventListener('touchmove', touchMoveHandler);
    document.addEventListener('touchend', touchEndHandler);
    document.addEventListener('touchcancel', touchEndHandler);
};

const swap = function(nodeA, nodeB) {
    const parentA = nodeA.parentNode;
    const siblingA = nodeA.nextSibling === nodeB ? nodeA : nodeA.nextSibling;

    // Move `nodeA` to before the `nodeB`
    nodeB.parentNode.insertBefore(nodeA, nodeB);

    // Move `nodeB` to before the sibling of `nodeA`
    parentA.insertBefore(nodeB, siblingA);
};

const touchMoveHandler = function(e) {

    const draggingRect = draggingEle.getBoundingClientRect();

    if (!isDraggingStarted) {
        // Update the flag
        isDraggingStarted = true;
        
        // Let the placeholder take the height of dragging element
        // So the next element won't move up
        placeholder = document.createElement('div');
        placeholder.classList.add('placeholder');

        draggingEle.parentNode.insertBefore(
            placeholder,
            draggingEle.nextSibling
        );

        // Set the placeholder's height
        placeholder.style.height = `${draggingRect.height}px`;
    }
    // Set position for dragging element
    draggingEle.style.position = 'absolute';
    draggingEle.style.top = `${e.pageY - y}px`; 
    draggingEle.style.left = `${e.pageX - x}px`;

    // The current order:
    // prevEle
    // draggingEle
    // placeholder
    // nextEle
    const prevEle = draggingEle.previousElementSibling;
    const nextEle = placeholder.nextElementSibling;   
    
    // User moves item to the top
    if (prevEle && isAbove(draggingEle, prevEle)) {
        // The current order    -> The new order
        // prevEle              -> placeholder
        // draggingEle          -> draggingEle
        // placeholder          -> prevEle
        swap(placeholder, draggingEle);
        swap(placeholder, prevEle);
        return;
    }
    // User moves the dragging element to the bottom
    if (nextEle && isAbove(nextEle, draggingEle)) {
        // The current order    -> The new order
        // draggingEle          -> nextEle
        // placeholder          -> placeholder
        // nextEle              -> draggingEle
        swap(nextEle, placeholder);
        swap(nextEle, draggingEle);
    }
};

const touchEndHandler = function() {
    // Remove the placeholder
    placeholder && placeholder.parentNode.removeChild(placeholder);
    // Reset the flag
    isDraggingStarted = false;
    // Remove the position styles
    draggingEle.style.removeProperty('top');
    draggingEle.style.removeProperty('left');
    draggingEle.style.removeProperty('position');
    draggingEle.style.removeProperty('background-color');

    x = null;
    y = null;
    draggingEle = null;

    // allow the page to be scrolled again.
    // document.documentElement.style.overflow = 'auto';
    e.preventDefault()
    document.body.style.overflow = 'auto';

    // Remove the handlers of `mousemove` and `mouseup`
    document.removeEventListener('touchmove', touchMoveHandler);
    document.removeEventListener('touchend', touchEndHandler);
    document.removeEventListener('mousemove', touchMoveHandler);
    document.removeEventListener('mouseup', touchEndHandler);
    document.removeEventListener('touchcancel', touchEndHandler);
};


const isAbove = function(nodeA, nodeB) {
    // Get the bounding rectangle of nodes
    const rectA = nodeA.getBoundingClientRect();
    const rectB = nodeB.getBoundingClientRect();

    return (rectA.top + rectA.height / 2 < rectB.top + rectB.height / 2);
};