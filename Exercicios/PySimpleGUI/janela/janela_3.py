import PySimpleGUI as sg   

sg.theme("Dark Red ")

layout = [[sg.Text("Write for here!"), sg.Text(size =(12,1), text_color=("red"), key = "-OUTPUT-")],
         [sg.Input(key ="-IN-")],
         [sg.Button("Show"), sg.Exit()]]

window = sg.Window("window that stay open", layout)

while True: 
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break 
    if event == "Show":
        window["-OUTPUT-"].update(values["-IN-"])
    

window.close()


