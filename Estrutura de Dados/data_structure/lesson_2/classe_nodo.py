#Metodo que verifica se a Lista está Vazia, Caso positivo Retorna True caso contrário False
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo

    def __repr__(self) -> str:
        return '%s -> %s' % (self.conteudo, self.proximo)

    def new_method(self):
        pass 
    
class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    # def __repr__(self) -> str:
    #     return "[" + str(self.inicio) + "]"
    
def ListaVazia(lista):
    if lista.inicio == None :
        return True
    else:
        return False
    
#Programa Principal de teste
lista = ListaEncadeada()
print("A Lista está vazia: ", ListaVazia(lista))

nodo = Nodo("Primeiro")
lista.inicio = nodo

print("A lista está vazia: ", ListaVazia(lista))