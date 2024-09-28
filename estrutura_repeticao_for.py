texto = input("Digite algo: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print('final do laço')

# Ranger
# for numbers in range(0, 51, 5):
    # print(numbers, end=" ")

#While
opcao = -1
while opcao != 0:
    opcao = int(input("[1] somar [2] multiplicar [3] maior [0] sair do programa:"))

    if opcao == 1:
        print("somando")
    elif opcao == 2:
        print("multiplicando")
    elif opcao == 3:
        print("maior")
    elif opcao == 0:
        print("saindo do programa")