conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("saldo insuficiente!")
    else:
        print("Saque realizado com sucesso!")