from veiculo import Veiculo 

class Vaga:
    def __init__(self, numero):
        self.numero = numero
        self.disponivel = True
        self.veiculo = None

    def estacionar(self, veiculo):
        if self.disponivel:
            self.veiculo = veiculo
            self.disponivel = False
            return f'Veículo {veiculo.placa} estacionado na vaga {self.numero}.'
        return 'Vaga ocupada.'

    def retirar(self):
        if not self.disponivel:
            veiculo = self.veiculo
            self.veiculo = None
            self.disponivel = True
            return f'Veículo {veiculo.placa} retirado da vaga {self.numero}.'
        return 'Vaga já está vazia.'

    def __str__(self):
        if self.disponivel:
            return f'Vaga {self.numero} está disponível.'
        return f'Vaga {self.numero} ocupada pelo veículo {self.veiculo.placa}.'