class Pilha {
    constructor() {
        this.elements = [];
    }

    push(element) {
        this.elements.push(element);
    }

    pop() {
        this.elements.pop();
    }
}

const pilha = new Pilha();
pilha.push(1);
pilha.push(4);
pilha.push(3);
console.log(pilha.elements);
