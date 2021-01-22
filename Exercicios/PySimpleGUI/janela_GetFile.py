import PySimpleGUI as sg  


event, value = sg.Window("Get File", [[sg.Text("File Name")], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)