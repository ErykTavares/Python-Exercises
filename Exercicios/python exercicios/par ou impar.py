def cond(n):
    res = n % 2
    if res == 0 :
        return F"O numero {n} e par!"
    elif res != 0 : 
        return F"O numero {n} e impar!"


print(cond(int(input("Digite um numero: "))))



