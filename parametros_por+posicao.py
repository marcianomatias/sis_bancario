
def criar_carro( modelo, ano, placa, /, marca, motor, combustivel):# passado por posição
    print(modelo, ano, placa, motor, combustivel)
#criar_carro("Palio", 1990, "AB1-2C34", marca="Fiat", motor="1.0", combustivel="Flex")
criar_carro("Palio", 1990, "AB1-2C34", "Fiat", "1.0", "Flex")

def criar_carro2(*, modelo, ano, placa,  marca, motor, combustivel):# passado por nome
    print(modelo, ano, placa, motor, combustivel)
criar_carro2(modelo="Palio", ano=1990, placa="AB1-2C34", marca="Fiat", motor="1.0", combustivel="Flex")

def criar_carro( modelo, ano, placa, /, *, marca, motor, combustivel):# passado por posição e nome
    print(modelo, ano, placa, motor, combustivel)
criar_carro("Palio", 1990, "AB1-2C34", marca="Fiat", motor="1.0", combustivel="Flex")
