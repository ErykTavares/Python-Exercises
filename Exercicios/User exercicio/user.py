import json

def Username(N):
    """Armazena o nome do usuario."""

    user_name= N
    file = "username.json"
    with open("file", "w") as f_obj: 
        json.dump(user_name, f_obj)
        return user_name


def Great_master():
    """Da boas vindas ao mestre."""
    file = "username.json"
    with open("file") as f_obj:
        master = json.load(f_obj)
    return F"Bem vindo de volta mestre {master}, quais são as ordens?"

def Ordem(N):
    """cumpri a ordem."""
    if N == 1:
        return "Irei trazer o café mestre!"

    elif N == 2:
        return "Vou preparar o banho mestre!"
    
