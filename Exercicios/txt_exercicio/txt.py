arq = ("C:/Users/ErykTavares/Desktop/python/txt_exercicio/text_1.txt")

with open(arq) as file_object: 
        for line in file_object:
            print(line.replace("Eryk", "FideumaEgua"))

           