
while True:
    idade = int(input("Qual e a sua idade?: "))
    if idade <= 3 or idade >= 65:
        print("Seu ingresso e gratuito!")
    
    elif idade < 12: 
        print("O seu ingresso custa 10R$!")
    
    elif idade >=12 :
        print("Seu ingresso custa 15R$!")
    
    print("[1] para continuar \n[2] para sair")
    flag = int(input(":"))
    if flag == 2 :
        break