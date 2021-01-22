def voto(ano):
    from datetime import date
    atual = date.today().year 
    idade = atual - ano
    if idade < 16:
         return  f"Com {idade} anos : Não Vota!"
    elif 16 <= idade < 18 or idade > 65:
         return f"Com {idade} anos: Voto e Opcional!"
    else:
         return f"Com {idade} anos: Voto e obrigatorio! "

        
print(voto(int(input("Digite seu ano de nascimento :"))))