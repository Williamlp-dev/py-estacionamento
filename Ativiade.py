import random
from datetime import datetime, timedelta

# Classe principal que gerencia todas as operações do estacionamento
class SistemaEstacionamento:
    def __init__(self):
        # Configuração da capacidade máxima de veículos por tipo
        # Limita o número de vagas para organização do estacionamento
        self.vagas_carros = 5  # Total de vagas para carros
        self.vagas_motos = 3   # Total de vagas para motos
        
        # Repositório central de veículos estacionados
        # Usa placa como chave para acesso rápido e único
        self.veiculos_estacionados = {}
        
        # Tabela de preços por tipo de veículo
        # Define o custo por hora de acordo com a categoria do veículo
        self.precos = {
            'carro': 5.00,  # Tarifa para carros por hora
            'moto': 3.00    # Tarifa para motos por hora
        }
    
    def estacionar_veiculo(self, placa, tipo):
        """
        Registra a entrada de um novo veículo no estacionamento.
        
        Etapas de verificação:
        1. Verifica limite de vagas para o tipo de veículo
        2. Impede entrada de veículos com placa duplicada
        3. Registra informações do veículo
        
        Parâmetros:
        - placa: Identificação única do veículo
        - tipo: Categoria do veículo (carro ou moto)
        
        Retorna:
        - Boolean indicando sucesso ou falha do estacionamento
        """
        # Bloqueia entrada se limite de vagas para carros foi atingido
        if tipo == 'carro' and len([v for v in self.veiculos_estacionados.values() if v['tipo'] == 'carro']) >= self.vagas_carros:
            print("Desculpe, não há vagas disponíveis para carros.")
            return False
        
        # Bloqueia entrada se limite de vagas para motos foi atingido
        if tipo == 'moto' and len([v for v in self.veiculos_estacionados.values() if v['tipo'] == 'moto']) >= self.vagas_motos:
            print("Desculpe, não há vagas disponíveis para motos.")
            return False
        
        # Verifica se o veículo já está estacionado para evitar duplicidades
        if placa in self.veiculos_estacionados:
            print("Este veículo já está estacionado.")
            return False
        
        # Registra informações do veículo no dicionário de estacionados
        self.veiculos_estacionados[placa] = {
            'tipo': tipo,        # Armazena o tipo de veículo
            'entrada': datetime.now()  # Registra o momento exato da entrada
        }
        
        print(f"Veículo {placa} estacionado com sucesso!")
        return True
    
    def remover_veiculo(self, placa):
        """
        Processa a saída de um veículo do estacionamento.
        
        Etapas de processamento:
        1. Verifica existência do veículo
        2. Gera tempo de permanência simulado
        3. Calcula valor a ser cobrado
        4. Remove veículo do estacionamento
        
        Parâmetro:
        - placa: Identificação do veículo a ser removido
        
        Retorna:
        - Boolean indicando sucesso ou falha da remoção
        """
        # Interrompe processo se veículo não foi encontrado
        if placa not in self.veiculos_estacionados:
            print("Veículo não encontrado no estacionamento.")
            return False
        
        # Recupera dados do veículo antes da remoção
        veiculo = self.veiculos_estacionados[placa]
        
        # Simula tempo de permanência para cálculo de tarifa
        # Gera valor aleatório entre 1 e 5 horas para fins didáticos
        tempo_permanencia = random.randint(1, 5)
        
        # Calcula valor total baseado no tipo de veículo e tempo
        valor_hora = self.precos[veiculo['tipo']]
        valor_total = tempo_permanencia * valor_hora
        
        # Remove registro do veículo do estacionamento
        del self.veiculos_estacionados[placa]
        
        # Apresenta resumo da permanência e cobrança
        print(f"Veículo {placa} permaneceu por {tempo_permanencia} horas.")
        print(f"Total a pagar: R$ {valor_total:.2f}")
        
        return True
    
    def listar_veiculos(self):
        """
        Apresenta relação de veículos atualmente estacionados.
        
        Funcionalidades:
        - Verifica se há veículos
        - Exibe informações de cada veículo
        """
        # Verifica se existem veículos estacionados
        if not self.veiculos_estacionados:
            print("Não há veículos estacionados.")
            return
        
        # Exibe informações detalhadas de cada veículo
        print("Veículos estacionados:")
        for placa, veiculo in self.veiculos_estacionados.items():
            print(f"Placa: {placa} | Tipo: {veiculo['tipo'].capitalize()}")
    
    def menu_principal(self):
        """
        Interface interativa principal do sistema.
        
        Fornece menu para:
        1. Estacionar veículo
        2. Remover veículo
        3. Listar veículos
        4. Encerrar sistema
        
        Gerencia fluxo de interação e tratamento de erros
        """
        while True:
            # Apresentação do menu de opções
            print("\nBem-vindo ao sistema de estacionamento!")
            print("1. Estacionar veículo")
            print("2. Remover veículo")
            print("3. Listar veículos estacionados")
            print("4. Sair")
            
            try:
                # Captura escolha do usuário
                opcao = int(input("Escolha uma opção: "))
                
                # Fluxo para estacionamento de veículo
                if opcao == 1:
                    placa = input("Digite a placa do veículo: ").upper()
                    tipo = input("Digite o tipo do veículo (carro/moto): ").lower()
                    
                    # Valida tipo de veículo antes de estacionar
                    if tipo in ['carro', 'moto']:
                        self.estacionar_veiculo(placa, tipo)
                    else:
                        print("Tipo de veículo inválido. Escolha 'carro' ou 'moto'.")
                
                # Fluxo para remoção de veículo
                elif opcao == 2:
                    placa = input("Digite a placa do veículo: ").upper()
                    self.remover_veiculo(placa)
                
                # Fluxo para listagem de veículos
                elif opcao == 3:
                    self.listar_veiculos()
                
                # Opção para encerramento do sistema
                elif opcao == 4:
                    print("Saindo do sistema...")
                    break
                
                # Tratamento para opção inválida
                else:
                    print("Opção inválida. Tente novamente.")
            
            # Captura erro de entrada inválida
            except ValueError:
                print("Por favor, digite um número válido.")

# Ponto de entrada do programa
if __name__ == "__main__":
    # Inicializa e inicia o sistema de estacionamento
    sistema = SistemaEstacionamento()
    sistema.menu_principal()