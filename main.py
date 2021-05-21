def verifica_repeticao(lista, numero):
    i = 0
    for n in lista:
        if n == numero:
            i += 1
    return i


numeros = [1, 2, 5, 7, 8, 4, 6, 5, 4, 2, 3, 2, 1, 8, 7, 6, 4, 2, 1]

num = int(input("Digite o número que deseja verificar: "))

num_repeticoes = verifica_repeticao(numeros, num)

print("O número " + str(num) + " aparece " + str(num_repeticoes) + " vez(es) na lista")