import moeda

num = float(input("Digite o valor do Dinheiro :"))
print(f"{num} Com 10% a mais e {moeda.aumentar(num, 10)}")
print(f"{num} Com 13% a menos e {moeda.diminuir(num, 13)}")
print(f"{num} O dobro e {moeda.dobro(num)}")
print(f"{num} A metade e {moeda.metade(num)}")
