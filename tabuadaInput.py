def tabuada_personal(numero, inicio, fim):
        while inicio <= fim:
            print(numero, ' * ', inicio, ' = ', inicio * numero)
            inicio += 1


num = int(input("Digite o número que deseja ver a tabuada de multiplicação: "))
ini = int(input("Digite o número que deseja iniciar a tabuada: "))
fim = int(input("Digite o número que deseja finalizar a tabuada: "))

tabuada_personal(num, ini, fim)