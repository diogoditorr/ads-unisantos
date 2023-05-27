class Fila {
    constructor() {
        this.elements = [];
    }

    enqueue(element) {
        this.elements.push(element);
    }

    dequeue() {
        this.elements.shift()
    }
}