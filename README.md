# Sistema de Estacionamento 🚗🏅

## Descrição do Projeto
Projeto acadêmico de Sistema de Gerenciamento de Estacionamento desenvolvido em Python, permitindo o controle de entrada, saída e listagem de veículos com fins educacionais.

## 🌟 Funcionalidades
- Estacionar veículos (carros e motos)
- Remover veículos do estacionamento
- Listar veículos estacionados
- Cálculo automático de valores
- Controle de vagas por tipo de veículo

## 🛠️ Requisitos
- Python 3.7+
- Bibliotecas utilizadas:
  - `random`
  - `datetime`

## 📦 Instalação

### Clonagem do Repositório
```bash
git clone https://github.com/Williamlp-dev/py-estacionamento.git
```

### Navegação e Execução
```bash
cd Estacionamento
python Estacionamento.py
```

## 🔧 Configurações do Sistema

### Capacidade de Vagas
- Carros: 5 vagas
- Motos: 3 vagas

### Tabela de Preços
- Carro: R$ 5,00 por hora
- Moto: R$ 3,00 por hora

## 📐 Estrutura do Código

### Classe Principal: `SistemaEstacionamento`
Gerencia todas as operações do estacionamento.

#### Métodos Principais
1. `estacionar_veiculo(placa, tipo)`
   - Registra entrada de veículos
   - Verifica disponibilidade de vagas
   - Previne entradas duplicadas

2. `remover_veiculo(placa)`
   - Calcula tempo de permanência
   - Gera valor a ser cobrado
   - Remove veículo do estacionamento

3. `listar_veiculos()`
   - Exibe veículos atualmente estacionados

4. `menu_principal()`
   - Interface interativa de usuário
   - Gerencia fluxo de operações

## 🔄 Fluxo de Operações

### Menu Principal
1. Estacionar veículo
2. Remover veículo
3. Listar veículos
4. Sair do sistema

## 📝 Exemplos de Uso

### Estacionando um Veículo
```
1. Selecione "Estacionar veículo"
2. Insira a placa (ex: ABC1234)
3. Escolha o tipo (carro/moto)
```

### Removendo um Veículo
```
1. Escolha "Remover veículo"
2. Informe a placa do veículo
3. Sistema calcula valor automaticamente
```

## ⚠️ Tratamento de Erros
- Validação de tipos de veículo
- Verificação de vagas disponíveis
- Prevenção de entradas duplicadas
- Tratamento de entradas inválidas

## 🚀 Próximas Melhorias
- Persistência de dados em arquivo
- Desenvolvimento de interface gráfica
- Geração de relatórios gerenciais
- Implementação de cálculo preciso de permanência

## 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar issues
- Enviar pull requests
- Sugerir melhorias

## 📞 Contato
- **Desenvolvedor:** William Lopes
- **Email:** williamlp.dev@gmail.com
- **GitHub:** [Williamlp-dev](https://github.com/Williamlp-dev)

## 📄 Licença
Projeto de código aberto. Consulte o arquivo LICENSE para mais detalhes.
```

Principais atualizações:
- Adicionei contexto acadêmico na descrição
- Atualizei instruções de instalação
- Adicionei emojis para melhor visualização
- Incluí seção de contribuições
- Adicionei links de contato
- Incluí menção à licença
- Formatei o texto para melhor legibilidade