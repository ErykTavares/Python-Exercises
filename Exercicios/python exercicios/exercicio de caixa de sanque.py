saque = int(input("digite o valor do saque"))
if 10 <= saque <= 600 :
    cem = saque // 100
    saque = saque % 100

    cinquenta = saque // 50
    saque = saque % 50

    vinte = saque // 20
    saque = saque % 20 

    dez = saque // 10
    saque = saque % 10

    cinco = saque // 5
    saque = saque % 5

    dois = saque // 2
    saque = saque % 2

    um = saque // 1

    if cem > 0 :
        print(cem, "Notas de 100R$")
    
    if cinquenta > 0 :
        print(cinquenta, "Notas de 50R$")
    
    if vinte > 0:
        print(vinte, "Notas de 20R$")
    
    if dez > 0 :
        print(dez, "Notas de 10R$")
    
    if  cinco > 0 :
        print(cinco, "Notas de 5R$")

    if dois > 0:
        print(dois, "Notas de 2R$")
    
    if um > 0 :
        print (um, "Notas de 1R$")

else :
    print("Não e possivel realizar o saque!")
