print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)


saldo = 1000
saque = 200
limite = 100
especial = True



exp = saldo >= saque and saque <= limite or especial and saldo >= saque
print(exp)  # True

exp2 = (saldo >= saque and saque <= limite) or (especial and saldo >= saque)

print(exp2)  
print(exp == exp2)  # True

conta_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_saldo_sulficiente = especial and saldo >= saque

exp3 = conta_com_saldo_suficiente or conta_especial_saldo_sulficiente
print(exp3)  # True


