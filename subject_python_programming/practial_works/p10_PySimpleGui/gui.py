from convert import *

import PySimpleGUI as sg
import os


def create_img_cmprs_window():
    layout_img = [
        [sg.Text("Persent of compress 1 - 95%"), sg.InputText(key="-RES-", size=(20, 1))],
        [sg.Text("New file name          "), sg.InputText(key="-NAME-", size=(20, 1))],
        [sg.Button("OK"), sg.Button("Exit")]

    ]
    return sg.Window("Image compress", layout_img, finalize=True)


def create_main_window():
    sg.theme("Green")
    file_list_column = [
        [
            sg.Text("Folder", text_color='white'),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]
    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Choose an action:", text_color="white")],
        [sg.Listbox(values= [], size=(40, 5), key="-TOUT-", enable_events=True, horizontal_scroll=True)],
        [sg.Text("", key="-END-", background_color='#d8d584', size=(36, 1))],
        [sg.Text("Selected files:", text_color='white')],
        [sg.Listbox(values=[], size=(40, 5), key="-VIEW FILES-", enable_events=True)],
        [sg.Button("Working with multiple files", button_color='#517239', key="-MANY FILES-"),
         sg.Button("Update", button_color='#517239', key="-RELOAD-")]
    ]

    layout_main = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column)
        ]
    ]
    return sg.Window("Office tweaks", layout_main, finalize=True, resizable=True)


def create_choice_files():
    layout = [[sg.Text('Choose files:'), sg.Input(key="-CHOSEN FILES-"), sg.FilesBrowse()],
              [sg.Button('Open', key="-CHOICE-"), sg.Button('Cancel')]]

    return sg.Window('File selection dialog', layout, finalize=True)


window_main, window_cmprs = create_main_window(), None

commands_docx = ["Convert to pdf", "Delete"]
commands_pdf = ["Convert to docx", "Delete"]
commands_img = ["Compress", "Delete"]
commands_all = ["Delete all", "Delete all files starts with",
                "Delete all files ends with",
                "Delete all files contains",
                "Delete all files by extension"]
commands_all_docx = commands_all + ["Convert all to .pdf"]
commands_all_pdf = commands_all + ["Convert all to .docx"]
commands_all_img = commands_all + ["Compress all"]
file_paths = []
# Run the Event Loop
while True:
    window, event, values = sg.read_all_windows()
    if window == window_main and event in ("Exit", sg.WIN_CLOSED):
        break
    # Folder name was filled in, make a list of files in the folder
    if window == window_main and event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder) # список объектов в каталоге
            os.chdir(folder) # смена директории
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif", "jpeg", "jpg", ".pdf", ".docx"))
        ]
        window["-FILE LIST-"].update(fnames) # список высвечивается в левом окошке
    elif window == window_main and event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            if filename.endswith((".png", ".gif", "jpeg", "jpg")):
                window["-TOUT-"].update([com for com in commands_img])
            elif filename.endswith(".docx"):
                window["-TOUT-"].update([com for com in commands_docx])
            elif filename.endswith(".pdf"):
                window["-TOUT-"].update([com for com in commands_pdf])
        except:
            pass

    elif window == window_main and event == "-TOUT-":
        print(window, event, values)
        if file_paths == []:
            path = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]).replace("/", "\\")
        else:
            path = file_paths
        print(path)
        if values["-TOUT-"][0] == "Delete file":
            os.remove(os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0]))
            window["-END-"].update("The file has been successfully deleted")
            fnames.remove(values["-FILE LIST-"][0])
            window["-FILE LIST-"].update(fnames)

        elif values["-TOUT-"][0] == "Compress":
            window_cmprs = create_img_cmprs_window()

        elif values["-TOUT-"][0] == "Convert to pdf":
            docx_to_pdf(path)
            if values["-FILE LIST-"][0][:-4] + "pdf" in fnames:
                fnames.remove(values["-FILE LIST-"][0][:-4] + "pdf")
            fnames.append(values["-FILE LIST-"][0][:-4]+"pdf")
            window["-FILE LIST-"].update(fnames)
            window["-END-"].update("The file has been successfully converted")

        elif values["-TOUT-"][0] == "Convert to docx":
            pdf_to_docx(path)
            if values["-FILE LIST-"][0][:-3] + "docx" in fnames:
                fnames.remove(values["-FILE LIST-"][0][:-3] + "docx")
            fnames.append(values["-FILE LIST-"][0][:-3] + "docx")
            window["-FILE LIST-"].update(fnames)
            window["-END-"].update("The file has been successfully converted")

        elif values["-TOUT-"][0] == "Delete all":
            for p in path:
                os.remove(p)
            file_paths = []
            f_chosen = []
            window["-VIEW FILES-"].update([])

        elif values["-TOUT-"][0] == "Convert all to .pdf":
            for p in path:
                docx_to_pdf(p)
                f_chosen = []
                window["-VIEW FILES-"].update([])

        elif values["-TOUT-"][0] == "Convert all to .docx":
            for p in path:
                pdf_to_docx(p)
                f_chosen = []
                window["-VIEW FILES-"].update([])
    elif window == window_cmprs and event in ("Exit", sg.WIN_CLOSED):
        window_cmprs.close()

    elif window == window_cmprs and event == "OK":
        if values["-RES-"][0] != [] and values["-NAME-"] != []:
            image_compress(path, int(values["-RES-"]), values["-NAME-"])
            window_main["-END-"].update("The file has been successfully compressed")
            window_cmprs.close()

    elif window == window_main and event == "-MANY FILES-":
        print("applied")
        window_choice_files = create_choice_files()

    elif window == window_choice_files and event in ("Cancel", sg.WIN_CLOSED):
        window_choice_files.close()

    elif window == window_choice_files and event == "-CHOICE-" and values["-CHOSEN FILES-"] != "":
        print(values["-CHOSEN FILES-"])
        file_paths = values["-CHOSEN FILES-"].split(';')
        print("file_paths", file_paths)
        f_chosen = [file.split("/")[-1] for file in file_paths]
        print("f_coisen:",f_chosen)
        window_choice_files.close()

    elif window == window_main and event == "-RELOAD-":
        window["-VIEW FILES-"].update(f_chosen)
        print(values["-VIEW FILES-"])
        if all(file.endswith('.docx') for file in f_chosen):
            window["-TOUT-"].update([com for com in commands_all_docx])

        elif all(file.endswith('.pdf') for file in f_chosen):
            window["-TOUT-"].update([com for com in commands_all_pdf])

        elif all(file.endswith((".png", ".gif", "jpeg", "jpg")) for file in f_chosen):
            window["-TOUT-"].update([com for com in commands_all_img])

        else:
            window["-TOUT-"].update([com for com in commands_all])
window_main.close()