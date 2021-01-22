import veiculos


while True: 
    print("Carro = [1] \nmoto = [2] \ncaminhão = [3]")

    veiculo = input("Qual foi o numero do veiculo alugado? ")
    dias = int(input("quantos dias vc rodou com o veiculo? "))
    km = int(input("quantos km vc percorreu com o veiculo? "))


    if veiculo == "1" :
        print(F"O preço do aluguel é R${veiculos.carro(dias, km)}")

    elif veiculo == "2" :
        print(F"O preço do aluguel é R${veiculos.moto(dias, km)}")

    elif veiculo == "3" :
        print(F"O preço do aluguel é R${veiculos.caminhão(dias, km)} ")

    flag = input("[1] Para Consultar o orçamento Novamente \n[2] Para sair \n: ")
    if flag == "2":
        break
