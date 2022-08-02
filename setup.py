from tkinter import Label
import tkinter as tk
from pynput import mouse
import json

NumberOfMouseClicks = 0
agentCoordinates = {
    "Astra": "",
    "Breach": "",
    "Brimstone": "",
    "Chamber": "",
    "Cypher": "",
    "Jett": "",
    "Killjoy": "",
    "KAY/O": "",
    "Omen": "",
    "Neon": "",
    "Phoenix": "",
    "Raze": "",
    "Reyna": "",
    "Sage": "",
    "Skye": "",
    "Sova": "",
    "Viper": "",
    "Yoru": "",
    "Lock": ""
}
curren_agent_coordinates_x = ""
curren_agent_coordinates_y = ""


def on_click(x, y, button, pressed):
    global NumberOfMouseClicks
    global curren_agent_coordinates_x
    global curren_agent_coordinates_y
    if NumberOfMouseClicks == 0:
        NumberOfMouseClicks += 1
        curren_agent_coordinates_x = x
        curren_agent_coordinates_y = y
        return False


def character_capture(character, row, column):
    global NumberOfMouseClicks
    print(f"Setting up positon for {character}")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    agent_bundled_position = [curren_agent_coordinates_x, curren_agent_coordinates_y]
    agentCoordinates[character] = agent_bundled_position
    NumberOfMouseClicks = 0
    print("{0} setup with {1}".format(character, agentCoordinates[character]))

    confirmation_label = tk.Label = Label(text="✓", fg="green", font=("Helvetica", 14))
    if column == 1:
        column = 0
        confirmation_label.grid(row=row, column=column, sticky='W', padx=(270, 0))
    elif column == 2:
        column = 0
        confirmation_label.grid(row=row, column=column, sticky='W', padx=(490, 0))
    else:
        confirmation_label.grid(row=row, column=column, sticky='W')


def save_config():
    json_string = json.dumps(agentCoordinates)
    json_file = open("config.json", "w")
    json_file.write(json_string)
    json_file.close()


window = tk.Tk()
window.geometry("750x450")
window.title("Valorant Instalocker Console")
window.resizable(False, False)

title = tk.Label = Label(text="Instalockscript V.1 by xHype - Setupmode", fg="black", font=('Helvetica', 20))
title.grid(row=0, column=0, sticky='W', padx=(20, 0), pady=(2, 0))

subtitle = tk.Label = Label(text="Updated from Gabryy-yy's source @Github: 'Valorant-InstaLocker'", fg="black",
                            font=('Helvetica', 11))
subtitle.grid(row=1, column=0, sticky='W', padx=(20, 0), pady=(0, 0))

astrap = tk.Button(text='Position for Astra', command=lambda: character_capture("Astra", 4, 0), fg='purple',
                   font=("Helvetica", 14))
astrap.grid(row=4, column=0, sticky='W', padx=(20, 0), pady=(5, 0))

breachp = tk.Button(text='Position for Breach', command=lambda: character_capture("Breach", 5, 0), fg='OrangeRed4',
                    font=("Helvetica", 14))
breachp.grid(row=5, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

brimstonep = tk.Button(text='Position for Brimstone', command=lambda: character_capture("Brimstone", 6, 0),
                       fg='orange2', font=("Helvetica", 14))
brimstonep.grid(row=6, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

chamberp = tk.Button(text='Position for Chamber', command=lambda: character_capture("Chamber", 7, 0),
                     fg='gold3', font=("Helvetica", 14))
chamberp.grid(row=7, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

cypherp = tk.Button(text='Position for Cypher', command=lambda: character_capture("Cypher", 8, 0),
                    fg='LightBlue3', font=("Helvetica", 14))
cypherp.grid(row=8, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

jettp = tk.Button(text='Position for Jett', command=lambda: character_capture("Jett", 9, 0),
                       fg='skyblue1', font=("Helvetica", 14))
jettp.grid(row=9, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

killjoyp = tk.Button(text='Position for Killjoy', command=lambda: character_capture("Killjoy", 4, 1),
                     fg='gold', font=("Helvetica", 14))
killjoyp.grid(row=4, column=0, padx=(100, 0), pady=(5, 0))

kayop = tk.Button(text='Position for KAY/O', command=lambda: character_capture("KAY/O", 5, 1),
                     fg='blue', font=("Helvetica", 14))
kayop.grid(row=5, column=0, padx=(100, 0), pady=(5, 0))

neonp = tk.Button(text='Position for Neon', command=lambda: character_capture("Neon", 6, 1),
                  fg='purple', font=("Helvetica", 14))
neonp.grid(row=6, column=0, padx=(100, 0), pady=(5, 0))

omenp = tk.Button(text='Position for Omen', command=lambda: character_capture("Omen", 7, 1),
                  fg='slateblue3', font=("Helvetica", 14))
omenp.grid(row=7, column=0, padx=(100, 0), pady=(5, 0))

phoenixp = tk.Button(text='Position for Phoenix', command=lambda: character_capture("Phoenix", 8, 1),
                     fg='red2', font=("Helvetica", 14))
phoenixp.grid(row=8, column=0, padx=(100, 0), pady=(5, 0))

razep = tk.Button(text='Position for Raze', command=lambda: character_capture("Raze", 9, 1),
                  fg='orange red', font=("Helvetica", 14))
razep.grid(row=9, column=0, padx=(100, 0), pady=(5, 0))


reynap = tk.Button(text='Position for Reyna', command=lambda: character_capture("Reyna", 4, 2),
                   fg='mediumpurple3', font=("Helvetica", 14))
reynap.grid(row=4, column=0, padx=(510, 0), pady=(5, 0))

sagep = tk.Button(text='Position for Sage', command=lambda: character_capture("Sage", 5, 2),
                  fg='turquoise1', font=("Helvetica", 14))
sagep.grid(row=5, column=0, padx=(510, 0), pady=(5, 0))

skyep = tk.Button(text='Position for Skye', command=lambda: character_capture("Skye", 6, 2),
                  fg='spring green', font=("Helvetica", 14))
skyep.grid(row=6, column=0, padx=(510, 0), pady=(5, 0))

sovap = tk.Button(text='Position for Sova', command=lambda: character_capture("Sova", 7, 2),
                  fg='cyan3', font=("Helvetica", 14))
sovap.grid(row=7, column=0, padx=(510, 0), pady=(5, 0))

viperp = tk.Button(text='Position for Viper', command=lambda: character_capture("Viper", 8, 2),
                   fg='orange red', font=("Helvetica", 14))
viperp.grid(row=8, column=0, padx=(510, 0), pady=(5, 0))

yorup = tk.Button(text='Position for Yoru', command=lambda: character_capture("Yoru", 9, 2),
                  fg='mediumpurple3', font=("Helvetica", 14))
yorup.grid(row=9, column=0, padx=(510, 0), pady=(5, 0))

lock_in_button = tk.Button(text='Position for Lock In', command=lambda: character_capture("Lock", 10, 2),
                           fg='black', font=("Helvetica", 14))
lock_in_button.grid(row=10, column=0, padx=(510, 0), pady=(5, 0))


savep = tk.Button(text='Save config', command=lambda: save_config(), fg='black', font=("Helvetica", 14))
savep.grid(row=10, column=0, sticky="W", padx=(20, 0), pady=(50, 0))

exitp = tk.Button(text='Exit', command=lambda: exit(), fg='black', font=("Helvetica", 14))
exitp.grid(row=10, column=0, sticky="W", padx=(160, 0), pady=(50, 0))

if __name__ == "__main__":
    window.mainloop()
