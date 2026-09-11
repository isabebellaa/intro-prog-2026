nomes = ["maria","joao","jose","rosa"]
print (f"nomes: {nomes}")
while True:
    nome = input("nome para adicionar")
    if nome == "":
        break
    else:
        nomes.append(nome)
print(f"nomes: {nomes}")