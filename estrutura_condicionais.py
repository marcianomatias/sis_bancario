MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("informe sua idade! "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH!")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")
else:
   print("Menor de idade, não pode tirar a CNH!")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH!")
elif idade == IDADE_ESPECIAL:
    print("Pode realizar as aulas teóricas, mas não pode realizara as aulas práticas")
else:
    print("Ainda não pode tirar a CNH")

