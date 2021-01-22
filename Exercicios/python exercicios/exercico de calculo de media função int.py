def nota(a, b, c, d):
    res = (a + b + c + d) / 4
    if res >=6 :
        return F"Com a nota de {res:.2f} voce foi aprovado."
    elif res < 6:
        return F"Com a nota de {res:.2f} voçe foi reprovado."
    
print("Informe as notas do aluno")
nt1 = float(input(": "))
nt2 = float(input(": "))
nt3 = float(input(": "))
nt4 = float(input(": "))

print(nota(nt1, nt2, nt3, nt4))