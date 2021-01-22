user = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
while senha == user :
    print ("Erro!")
    user = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")
if senha != user :
    print ("completo")
