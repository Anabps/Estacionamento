class Veiculo:
    def __init__(self, placa, modelo, cor):
        self.placa = placa
        self.modelo = modelo
        self.cor = cor

    def __str__(self):
        return f'Veículo: {self.modelo}, Placa: {self.placa}, Cor: {self.cor}'
