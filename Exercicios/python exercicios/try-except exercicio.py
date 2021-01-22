try:
    num_1, num_2 = input("Digite um numero: ").split()

    num_1 = int(num_1)

    num_2 = int(num_2)

except ValueError: 
    msg = "Não e possivel fazer a soma de palavras!" 
    print(msg)

else:   
    print(num_1+num_2)