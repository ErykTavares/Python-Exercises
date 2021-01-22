def city(cid, ps):
    return F"{cid} esta localizado em {ps}."

cidade = input("Digite o nome da cidade: ")
pais = input("Digite o nome do pais: ")

print(city(cidade, pais))