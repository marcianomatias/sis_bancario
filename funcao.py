#Função

def exibir_mensangem():
    print("Olá Mundo!")
def exibir_mensangem_1(nome):
    print(f"Olá Mundo, {nome}!")
def exibir_mensangem_2(name="Marcia"):
    print(f"Olá Mundo, {name}!")

exibir_mensangem()
exibir_mensangem_1(nome="Marciano")
exibir_mensangem_2()
exibir_mensangem_2(name="Matias")
