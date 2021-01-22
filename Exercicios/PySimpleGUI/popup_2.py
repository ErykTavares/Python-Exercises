import PySimpleGUI as sg   

arq = (r"C:\Users\ErykTavares\Desktop\python\PySimpleGUI\Animes.txt")
with open(arq) as f_obj: 
    texto = f_obj.read()
    sg.popup_scrolled("Anime List", texto, size=(40, None))