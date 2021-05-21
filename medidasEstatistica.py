def medidas_estatisticas(lista):
    desvio_medio = 0  # inicializacao e declaracao de variavel
    print('quantidade itens: ', len(lista))

    ordenada = sorted(lista)
    print('lista em ordem: ', ordenada)

    soma_lista = sum(lista)
    print('somatorio: ', soma_lista)

    media = soma_lista / len(lista)
    print('media: {:.2f}'.format(media))

    if len(ordenada) % 2 == 0:
        mediana = int(len(ordenada) / 2)
        print('mediana:', (ordenada[mediana - 1] + ordenada[mediana]) / 2)
    else:
        mediana = float(len(ordenada) / 2)
        mediana_tratada = round(mediana - 0.5)
        print('mediana: ', ordenada[mediana_tratada])

    print('Amplitutude total: ', max(lista) - min(lista))

    for n in lista:
        controle = media - n
        if controle < 0:
            controle = controle * -1
            desvio_medio += controle
        else:
            desvio_medio += controle
    print('Desvio Absoluto Medio: ', desvio_medio/len(lista), '\n')


listagem = [4, 5, 6, 7, 1, 3, 2, 7, 9, 12, 15, 21, 19, 17, 9, 5, 9, 8, 11, 20]
lista_2 = [1, 2, 3, 4, 5]

medidas_estatisticas(listagem)
medidas_estatisticas(lista_2)
