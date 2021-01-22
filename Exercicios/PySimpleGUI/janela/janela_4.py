import PySimpleGUI as sg   

sg.theme("python")

layout = [
     [sg.Text("Visualize imagens ou gifs", size=(20, 1), text_color=("black"))], 
     #[sg.In(size=(23, 1), key="input")],
     [sg.FileBrowse("Selecione a imagem", 
        file_types=(("Imagem", "*.png"),("Gif", "*.gif")), enable_events=(True), 
        key="image_sl"), sg.OK()],
        #[sg.Image(key="img")]
]

          

window = sg.Window("Visualizador", layout)

flag = False

while True: 
    event, values = window.read()
    image_sl = values["image_sl"]
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "OK":
        """window["img"].update( values["image_sl"])"""
        window.hide()
        flag = True
        
        if flag == True: 
            layout_2 = [
                    [sg.Text("Imagem"), sg.Button("Sair", key=("sair"))],
                    [sg.Image(values["image_sl"])]
                    ]
            window_2 =sg.Window("Imagem", layout_2)
    
            while True:
                event_2, values_2 = window_2.read()
                if event_2 == sg.WIN_CLOSED:
                    break
                
                if event_2 == "sair":
                    flag = False
                    window.UnHide()
                    break
            window_2.close()

            
            

window.close()

