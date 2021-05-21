def tabuada_multiplicacao(numero):
    contador = 0
    if numero < 10:
        while contador < 10:
            contador += 1
            print(numero, ' * ', contador, ' = ', contador * numero)
    else:
        while contador < numero:
            contador += 1
            print(numero, ' * ', contador, ' = ', contador*numero)


num = int(input("Digite o número que deseja ver a tabuada de multiplicação: "))

tabuada_multiplicacao(num)
