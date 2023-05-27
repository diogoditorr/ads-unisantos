class Carro:
    def __init__(self, marca, modelo, tanque=0) -> None:
        self.marca = marca
        self.modelo = modelo
        self.tanque = tanque

    def colocar_gasolina(self, quantidade=10):
        self.tanque += quantidade

    def mostrar_quantidade_tanque_de_combustivel(self):
        print(self.tanque, 'Litros')


meu_carro_favorito = Carro('Hyundai', 'Hyundai HB20', 10)
meu_carro_favorito.mostrar_quantidade_tanque_de_combustivel()