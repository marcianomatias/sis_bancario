opcao = -1

while True:
    opcao = int(input('digite um numero: '))

    if opcao == 10:
        break
    print(opcao)

for numero in range(100):
    if numero == 10:
        break
    print(numero)

for numero in range(100): # gerar numeros impares
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
