from vaga import Vaga
from veiculo import Veiculo

class Estacionamento:
    def __init__(self, total_vagas):
        self.vagas = [Vaga(i + 1) for i in range(total_vagas)]

    def listar_vagas_disponiveis(self):
        return [vaga for vaga in self.vagas if vaga.disponivel]

    def listar_veiculos_estacionados(self):
        return [vaga for vaga in self.vagas if not vaga.disponivel]

    def estacionar_veiculo(self, veiculo):
        vaga_disponivel = next((vaga for vaga in self.vagas if vaga.disponivel), None)
        if vaga_disponivel:
            return vaga_disponivel.estacionar(veiculo)
        return 'Não há vagas disponíveis.'

    def retirar_veiculo(self, numero_vaga):
        vaga = next((vaga for vaga in self.vagas if vaga.numero == numero_vaga), None)
        if vaga:
            return vaga.retirar()
        return 'Vaga não encontrada.'
