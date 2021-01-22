def loop (i, f, p):
    if i > f :
        p = p-p-p
        f = f - 1 -1
    
    elif p < 0 or p == 0:
        p = 1 
    
    for cont in range (i, f+1, p): 
        print(cont)
         
   
           
            
inicio = int(input("Digite o Inicio: "))
fim = int(input("Digite o Fim: "))
passo = int(input("Digite o Passo:"))

print(F"{loop(inicio, fim, passo)}","\nFim ")
