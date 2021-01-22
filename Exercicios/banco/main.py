import conta
import cliente


name = input("digite o nome: ")
cp = input("digite o cpf: ")
age = int(input("digite a idade: "))

psa1 = cliente.User(name, cp, age)

print("Nome: " + psa1.nome, "\nCPF: " + psa1.cpf, "\nIdade: " +str(psa1.idade))

sad = float(input("Digite seu Saldo: "))
lmt = float(input("Digite o limite :"))

cont1 = conta.Conta(psa1, sad, lmt)

print(cont1.Mostrar())



