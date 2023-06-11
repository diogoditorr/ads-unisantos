class Arvore {
    constructor() {
        this.nodes = {}
    }

    insert(tree, value) {
        if (tree.value) {
            if (value > tree.vale) {
                this.insert(tree.right, value)
            } else {
                this.insert(tree.left, value)
            }
        } else {
            tree.value = value
            tree.right = {}
            tree.left = {}
        }
    }
}

const newTree = new Arvore()
newTree.insert(newTree.nodes, 23)
console.log(newTree)
newTree.insert(newTree.nodes, 12)
console.log(newTree)
newTree.insert(newTree.nodes, 4)
newTree.insert(newTree.nodes, 18)
newTree.insert(newTree.nodes, 1)
newTree.insert(newTree.nodes, 27)
newTree.insert(newTree.nodes, 25)
