lista = [1, 4, 5, 7, 10, 6, 9]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)    # NA TUPLA NÃO DA PARA ALTERA
print(tupla)

print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 10
print(lista_numerica)

# lista.sort()  # ORDENAR A LISTA
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()    # PARA ORDENAR DE OUTRA MANEIRA
# print(lista_animal)

# print(lista_animal[1])
#
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não existe um lobo na lista. Será incluido.')
#     lista_animal.append('lobo')
#     print(lista_animal)

#lista_animal.remove('elefante')  #PARA RETIRA UM INTEM DA LISTA QUE VOCÊ SAIBA O NOME
#print(lista_animal)


# lista_animal.pop(1)  PARA RETIRA O ULTIMO INTEN DA LISTA
# print(lista_animal)

#nova_lista = lista_animal * 3
#print(nova_lista)

#print(min(lista)) PARA SABER O MENOR VALOR E TAMTEM SERVE PARA LITRAS

#print(max(lista)) PARA SABER O MAIOR VALOR

#print(sum(lista)) PARA SOMAR

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
