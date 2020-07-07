n1 = int(input('Primeiro bimestre: '))
while n1 > 10:
    n1 = int(input('Você digitou errado. Primeiro bimestre: '))
n2 = int(input('Segundo bimestre: '))
while n2 > 10:
    n2 = int(input('Você digitou errado. Segundo bimestre: '))
n3 = int(input('Terceiro bimestre: '))
while n3 > 10:
    n3 = int(input('Você digitou errado. Terceiro bimestre: '))
n4 = int(input('Quarto bimestre: '))
while n4 > 10:
    n4 = int(input('Você digitou errado. Quarto bimestre: '))
media = (n1 + n2 + n3 + n4) / 4
print('Média {}'.format(media))


# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Entre com a nota correta: '))



# NUMERO PRIMOS
# a = int(input('Entre com um valor: '))
# for num in range(a + 1):
#     div = 0
#     for x in range(1, num + 1):
#         resto = num % x
#         # print(num , resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# num = int(input('Entre com o número:'))
#
# div = 0
# for x in range (1 ,num + 1):
#     resto = num % x
#     print(num , resto)
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Número {} é primo.'.format(num))
# else:
#     print('Número {} não é primo.'.format(num))



