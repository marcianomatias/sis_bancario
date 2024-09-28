# Solicita ao usuário que insira um número
number = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar usando o operador de módulo (%)
if number % 2 == 0:
    print(f"O número {number} é par.")
else:
    print(f"O número {number} é ímpar.")