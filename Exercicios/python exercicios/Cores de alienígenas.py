import random

life =["verde", "amarelo", "vermelho"]
v= ("vermelho")
a = ("amarelo")
v1 = ("verde")

while True:
    dano = (random.choice(life))
    
    print(dano)
    
    if dano == v1:
        print("Voce Ganhou 5 pontos!")

    elif dano == a:
        print("voce ganhou 15 pontos!")

    elif dano == v :
        print("voce ganhou 30 pontos!")

    print("[1] repetir \n[2] sair")
    cont = int(input(": "))

    if cont == 2:
        break
