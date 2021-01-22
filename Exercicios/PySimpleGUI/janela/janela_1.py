import PySimpleGUI as sg  

event, values = window =sg.Window("Enter a Number Exemple", [ [sg.Text("Enter a number")],
          [sg.Input()],
          [sg.Ok()] ]).read(close=True)

sg.popup(event, values[0])

