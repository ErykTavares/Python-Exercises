import PySimpleGUI as sg  

sg.theme("Dark Red 2") 

event, values = sg.Window("Get File Exemple", [[sg.Text("FileName")],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]).read(close=True)

sg.popup(event, values[0])


