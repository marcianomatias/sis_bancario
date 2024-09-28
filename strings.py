curso = "      MarcIaNo MAtias"

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.strip())
print(curso.rstrip())
print(curso.lstrip())
print(curso.capitalize())
print(curso.swapcase())
print(curso.center(20, "*"))
print(curso.replace(" ", "-"))
print("..".join(curso))
print(curso.replace("Python", "Android"))
print(curso.split())
print(curso.find("o"))
print(curso.index("o"))
print(curso.count("o"))
print(curso.startswith("Py"))
print(curso.endswith("on"))
print(curso.isnumeric())
#interpolação de variáveis
#old style %
name = "Marcio"
age = 25
profission = "Programmer"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos e sou %s e programador em %s." % (name, age, profission, linguagem))

#old style metodo format

print("Olá, me chamo {}. Eu tenho {} anos e sou {} e programador em {}.".format(name, age, profission, linguagem))

#f-string
print(f"Olá me chamo {name}. Eu tenho {age} anos e sou {profission} e programador em {linguagem}.")

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")# formata a quantidade de casas no numeros float
print(f"Valor de PI: {PI:.4f}")# formata a quantidade de casas no numeros float
print(f"Valor de PI: {PI:10.2f}")

# Fatiamento de string

nome1 = "Marciano Matias dos Santos"
print(nome1[0])
print(nome1[:9])
print(nome1[9:])
print(nome1[9:15])
print(nome1[9:15:2])
print(nome1[:])
print(nome1[::-1])

#String múltiplas linhas

name1 = "Marciano"
mensagem = f'''
Ola, meu nome é {name1}, e estou aprendendo Python. '''
print(mensagem)
