salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f" lista auxiliar {lista_aux}")


    salario += bonus
    return salario

lista = [1]
print(f"O salário com o bônus é: {salario_bonus(500,lista)}")
print(f"lista original = {lista}")
