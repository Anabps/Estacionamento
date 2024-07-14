from veiculo import Veiculo
from estacionamento import Estacionamento

def main():
    # Criando instâncias de veículos
    veiculo1 = Veiculo('ABC-1234', 'Toyota Corolla', 'Preto')
    veiculo2 = Veiculo('XYZ-9876', 'Honda Civic', 'Branco')

    # Criando instância do estacionamento com 5 vagas
    estacionamento = Estacionamento(5)

    # Estacionando veículos
    print(estacionamento.estacionar_veiculo(veiculo1))  # Estacionar o Toyota Corolla
    print(estacionamento.estacionar_veiculo(veiculo2))  # Estacionar o Honda Civic

    # Listando vagas disponíveis
    print([str(vaga) for vaga in estacionamento.listar_vagas_disponiveis()])

    # Listando veículos estacionados
    print([str(vaga) for vaga in estacionamento.listar_veiculos_estacionados()])

    # Retirando um veículo
    print(estacionamento.retirar_veiculo(1))  # Retirar o veículo da vaga 1

    # Listando veículos estacionados após a retirada
    print([str(vaga) for vaga in estacionamento.listar_veiculos_estacionados()])

if __name__ == '__main__':
    main()

