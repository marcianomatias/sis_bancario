from strings import mensagem


def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca} {modelo} {ano} {placa}")
#salvar_carro("Fiat", "Palio", 1999, "AB1-2C34")
#salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="AB1-2C34")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "AB1-2C34"})#dicionario

