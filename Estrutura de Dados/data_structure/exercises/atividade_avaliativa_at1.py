class Produto:
    def __init__(self, codigo: int = 0, proximo_nodo=None):
        self.codigo=codigo
        self.proximo=proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.codigo, self.proximo)
    
class ListaEncadeada:
    def __init__(self):
        self.cabeca: None | Produto = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    

def AddFinal(lista: ListaEncadeada, novoCod: int):
    novo_node = Produto(novoCod)
    node_atual = lista.cabeca

    while True:
        if lista.cabeca == None:
            lista.cabeca = novo_node
            break

        if node_atual is None:
            break

        if node_atual.proximo is None:
            node_atual.proximo = novo_node
            break
        else:
            node_atual = node_atual.proximo


    
def main():
    lista = ListaEncadeada()
    print("Lista vazia:", lista)

    AddFinal(lista, 1111)
    print(lista)

    AddFinal(lista, 2222)
    print(lista)

    AddFinal(lista, 3333)
    print(lista)

if __name__ == '__main__':
    main()