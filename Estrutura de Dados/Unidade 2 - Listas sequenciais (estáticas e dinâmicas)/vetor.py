# Inicio
# Declaração de variável - Vetor
funcionario: list[str | int] = ['nome', 'idade', 'salario']
joao = ['joao', 42, 3000]
maria = ['Maria', 45, 4000]
media = 0
i = 0

# impressão de conteúdo em posição específica
print('alunos', joao[0], 'e', maria[0])
print('Idade', joao[1], 'e', maria[1])
print('Renda', joao[2], 'e', maria[2])

# Impressão do vetor completo
print(funcionario)

# Atribuição de conteúdo em posição específica do vetor
funcionario[0] = 'Lucas'
funcionario[1] = 18
funcionario[2] = 5000

# Cálculo da média de salários
media = (funcionario[2] + joao[2] + maria[2]) / 3

# Impressão da média de salários
print('A media dos salarios e de :', media)

# Fim
