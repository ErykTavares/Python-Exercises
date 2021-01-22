
while True :
    temperatura = float(input("Digite a temperatura em C°: "))

    res = int(input("Digite 1 para converter para farenheint \nDigite 2 para converter para Kelvin \n: "))

    if res == 1:
        print(F"A temperatura de {temperatura}C° em Farenheit é de {(1.8 * temperatura)+32:.1f}")

    elif res == 2:
        print(F"A temperatura de {temperatura}C° em Kelvin é de {temperatura + 273}K°")

    c = input("Deseja repetir a conversão? \nDigite 1 para Sim \nDigite 2 para não \n: ")
    if c == "2":
        break