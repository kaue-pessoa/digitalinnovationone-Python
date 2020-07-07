def contador_letars(lista_palavars):
    contador = []
    for x in lista_palavars:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['cachorro' , 'gato']
    print(contador_letars(lista))
