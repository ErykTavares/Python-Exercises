def make (tm, tx):
    return F"A camisa de tamanho {tm} com a estampa {tx}"

tamanho = int(input("Digite o tamanho da camisa: "))
estampa = input("Digite a estampa da camisa: ")

print(make(tamanho, estampa))

