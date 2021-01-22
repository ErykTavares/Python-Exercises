arq = ("python\Exercicios\convidado\Guest.txt")
while True:
    with open(arq, "a") as file_object:
        file_object.write(F'{input("Digite o nome do convidado:")}\n')
        flag = input("Ainda resta convidados? ")
        if flag == "não":
                break

with open(arq) as file_object:
        for line in file_object:
            print(line.strip())
            
           

            