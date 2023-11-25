class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
            print(f"{self.modelo} já esta ligado")
        else:
            print(f"{self.modelo} ligado")
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print("Carro Desligado")
            self.ligado = False
        else:
            print("Carro já esta desligado")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"Carro acelerando na velocidade: {self.velocidade} km/h")
        else:
            print("Carro está desligado")

    def frear(self):
        if self.velocidade >= 1:
            self.velocidade -= 1
            print(f"Carro está freando e na velocidade: {self.velocidade} km/h")
        else:
            print("Carro está parado")        