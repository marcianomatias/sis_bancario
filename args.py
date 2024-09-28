def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n{texto}\n{meta_dados}"
    print(mensagem)


exibir_poema("sexta-feira 27 set 2024", "Zen of Python", "Beautiful is better than ugly", "Beautiful is better than ugly", "Beautiful is better than ugly", autor="Tim Petters", ano=1999)