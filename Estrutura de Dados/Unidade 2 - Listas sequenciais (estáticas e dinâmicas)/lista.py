# Uma nova lista
generos = ['policial', 'indefinido', 'terror', 'suspense', 'amor']

# Varrendo a lista
for prog in generos:
    print(prog)

# Trocando o último elemento
generos[-1] = 'romantico'

# incluindo
generos.append('drama')

# Removendo
generos.remove('indefinido')

# Imprime numerado
for i, prog in enumerate(generos):
    print(i + 1, '=>', prog)

print(generos)

# Fim
