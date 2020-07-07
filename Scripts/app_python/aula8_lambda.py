contador_letras = lambda lista: [len(x) for x in lista]

lista_aminas = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_aminas))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
print('A soma {}'.format(soma(10, 5)))
print('A subtração {}'.format(subtracao(10, 2)))

