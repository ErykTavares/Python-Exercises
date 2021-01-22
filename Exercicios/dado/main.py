from dado import Dado


while True:
    print("")
    
    print(Dado.Roll())
    
    print("")

    cont = input("Deseja rolar o dado novamente:")
    if cont == "não":
        break
