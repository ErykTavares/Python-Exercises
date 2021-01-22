import PySimpleGUI as sg  

num= sg.popup_get_text("Digite um numero: ")
num_1= int(num)


for i in range(100):
    flag= (num_1 * i)
    res= f"{num_1} x {i} = {flag}"
    sg.Print(res)
    sg.easy_print_close()
   
       
   
