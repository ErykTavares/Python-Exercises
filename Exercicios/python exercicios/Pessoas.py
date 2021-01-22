pessoa_1 = {}

pessoa_1["nome"] = str(input("Digite seu nome: "))
pessoa_1["last_nome"] = str(input("Digite seu ultimo nome: "))
pessoa_1["idade"] = int(input("Digite sua idade: "))

pessoa_2 = {}

pessoa_2["nome"] = str(input("Digite seu nome: "))
pessoa_2["last_nome"] = str(input("Digite seu ultimo nome: "))
pessoa_2["idade"] = int(input("Digite sua idade: "))

const = str(input("Digite o nome de quem voce deseja consultar os dados: "))

if const == pessoa_1["nome"]:
    print("Nome:" + pessoa_1["nome"], pessoa_1["last_nome"], "\nidade:" + str(pessoa_1["idade"]))



