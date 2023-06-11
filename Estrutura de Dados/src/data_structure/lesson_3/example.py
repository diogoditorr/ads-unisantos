from ..classes.linked_list import LinkedList

def main():
    lista_encadeada = LinkedList()
    print("Lista vazia:\n", lista_encadeada.is_empty())

    lista_encadeada.insert(5)
    print("Lista contém um único elemento:\n", lista_encadeada)

    lista_encadeada.insert(10)
    lista_encadeada.insert(10)
    print("Inserindo um novo elemento\n", lista_encadeada)
    print("Existe um elemento com valor 10?", lista_encadeada.has_element(10))
    print("Existe um elemento com valor 9?", lista_encadeada.has_element(9))

if __name__ == '__main__':
    main()