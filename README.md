# Sistema de Estacionamento 🚗🏅

## Descrição do Projeto
Sistema de gerenciamento de estacionamento desenvolvido em Python, permitindo o controle de entrada, saída e listagem de veículos.

## Funcionalidades 🌟
- Estacionar veículos (carros e motos)
- Remover veículos do estacionamento
- Listar veículos estacionados
- Cálculo automático de valores
- Controle de vagas por tipo de veículo

## Requisitos 🛠️
- Python 3.7+
- Bibliotecas padrão:
  - `random`
  - `datetime`

## Instalação

### Passos para Configuração
1. Clone o repositório
```bash
gh repo clone Williamlp-dev/py-estacionamento
```

2. Acesse o diretório do projeto
```bash
cd Estacionamento.py
```

3. Execute o script
```bash
python Estacionamento.py
```

## Configurações Predefinidas 🔧

### Capacidade de Vagas
- Carros: 5 vagas
- Motos: 3 vagas

### Tabela de Preços
- Carro: R$ 5,00 por hora
- Moto: R$ 3,00 por hora

## Estrutura do Código

### Classe Principal: `SistemaEstacionamento`
Responsável por gerenciar todas as operações do estacionamento.

#### Métodos Principais
1. `estacionar_veiculo(placa, tipo)`
   - Registra entrada de veículos
   - Verifica disponibilidade de vagas
   - Impede duplicidade

2. `remover_veiculo(placa)`
   - Calcula tempo de permanência
   - Gera valor a ser cobrado
   - Remove veículo do estacionamento

3. `listar_veiculos()`
   - Exibe veículos atualmente estacionados

4. `menu_principal()`
   - Interface interativa de usuário
   - Gerencia fluxo de operações

## Fluxo de Operações 🔄

### Menu Principal
1. Estacionar veículo
2. Remover veículo
3. Listar veículos
4. Sair do sistema

## Exemplos de Uso 📝

### Estacionando um Veículo
```
1. Escolha a opção "Estacionar veículo"
2. Digite a placa (ex: ABC1234)
3. Selecione o tipo (carro/moto)
```

### Removendo um Veículo
```
1. Escolha a opção "Remover veículo"
2. Digite a placa do veículo
3. Sistema calcula valor automaticamente
```

## Tratamento de Erros ⚠️
- Validação de tipos de veículo
- Verificação de vagas disponíveis
- Prevenção de entradas duplicadas
- Tratamento de entradas inválidas

## Próximas Melhorias 🚀
- Persistência de dados
- Interface gráfica
- Relatórios gerenciais
- Cálculo preciso de tempo de permanência

## Contato 📧
- Nome : William Lopes
- Gmail : williamlp.dev@gmail.com
```

Este README.md oferece:
- Visão geral do projeto
- Instruções de instalação
- Explicação das funcionalidades
- Exemplos de uso
- Informações sobre contribuição