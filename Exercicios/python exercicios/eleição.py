n = int(input("digite o numero de eleitores : "))
cand1 = cand2 = cand3 = 0
for cont in range (1, n+1) :
    voto = int(input("digite o valor do voto do eleitor %i :"%cont))
    if voto == 1 :
        cand1 += 1
    elif voto == 2 :
        cand2 += 1
    else:
         cand3 += 1 
if cand1 > cand2:
    if cand1 > cand3:
        print("o candidato 1° ganhou com %i votos" %cand1)
elif cand2 > cand1:
    if cand2 > cand3:
        print("o candidato 2° ganhou com %i votos" %cand2)
else:
    print("o candidato 3° ganhou com %i votos" %cand3)