compra = float(input("digite o valor do produto: R$"))
desc = int(input("digite o valor do desconto: %"))

valor =  compra - ((desc /100) * compra)
print (f"O valor da compra  com o deconto {desc}% igual a {compra:.2f}R$")