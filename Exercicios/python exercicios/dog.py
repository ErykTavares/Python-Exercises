class Dog():
    def __init__(self, name, age ):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " Esta sentado agora!.")
    def roll_over(self):
        print(self.name.title() + " Esta rolando agora!.")


dog = Dog((input("Digite o nome ")), int(input('Digite a idade ')))

print("O nome do animal é " + dog.name.title() + ".")
print("Sua idade é " + str(dog.age) + ".")
dog.sit()
dog.roll_over()