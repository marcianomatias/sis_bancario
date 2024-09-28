def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da oparação é = {resultado}")


resultado(10, 10, somar)
resultado(10, 10, subtrair)
resultado(10, 10, multiplicar)

op = somar
print(f"A soma de  a + b é: {op(1,5)}")
