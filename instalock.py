import keyboard
import pyautogui as pg
from tkinter import Label
import tkinter as tk
import json


with open('config.json', 'r') as f:
    agent_coords = json.load(f)

window = tk.Tk()
window.geometry("650x420")
window.title("Valorant Instalocker Console")
window.resizable(False, False)


def instalock(character):
    text_output = Label(window, text=f"Instalock Script active for {character}", fg='black', font=("Helvetica", 11))
    text_output.grid(row=14, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(agent_coords[character][0], agent_coords[character][1])
        pg.doubleClick()
        pg.PAUSE = 0.035
        pg.moveTo(agent_coords["Lock"])
        pg.doubleClick()

        try:
            if keyboard.is_pressed('p'):
                print('Stopping Instalocker')
                break
        except:
            break


title = tk.Label = Label(text="Instalockscript V.1 by xHype - Instalockmode", fg="black", font=('Helvetica', 20))
title.grid(row=0, column=0, sticky='W', padx=(20, 0), pady=(2, 0))

subtitle = tk.Label = Label(text="Updated from Gabryy-yy's source @Github: 'Valorant-InstaLocker'", fg="black",
                            font=('Helvetica', 11))
subtitle.grid(row=1, column=0, sticky='W', padx=(20, 0), pady=(0, 0))


astrap = tk.Button(text='Pick Astra', command=lambda: instalock("Astra"), fg='purple',
                   font=("Helvetica", 14))
astrap.grid(row=4, column=0, sticky='W', padx=(20, 0), pady=(5, 0))

breachp = tk.Button(text='Pick Breach', command=lambda: instalock("Breach"), fg='OrangeRed4',
                    font=("Helvetica", 14))
breachp.grid(row=5, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

brimstonep = tk.Button(text='Pick Brimstone', command=lambda: instalock("Brimstone"),
                       fg='orange2', font=("Helvetica", 14))
brimstonep.grid(row=6, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

chamberp = tk.Button(text='Pick Chamber', command=lambda: instalock("Chamber"),
                     fg='gold3', font=("Helvetica", 14))
chamberp.grid(row=7, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

cypherp = tk.Button(text='Pick Cypher', command=lambda: instalock("Cypher"),
                    fg='LightBlue3', font=("Helvetica", 14))
cypherp.grid(row=8, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

jettp = tk.Button(text='Pick Jett', command=lambda: instalock("Jett"),
                       fg='skyblue1', font=("Helvetica", 14))
jettp.grid(row=9, column=0, sticky="W", padx=(20, 0), pady=(5, 0))

killjoyp = tk.Button(text='Pick Killjoy', command=lambda: instalock("Killjoy"),
                     fg='gold', font=("Helvetica", 14))
killjoyp.grid(row=4, column=0, padx=(20, 0), pady=(5, 0))

kayop = tk.Button(text='Pick KAY/O', command=lambda: instalock("KAY/O"),
                  fg='blue', font=("Helvetica", 14))
kayop.grid(row=5, column=0, padx=(20, 0), pady=(5, 0))

neonp = tk.Button(text='Pick Neon', command=lambda: instalock("Neon"),
                  fg='purple', font=("Helvetica", 14))
neonp.grid(row=6, column=0, padx=(20, 0), pady=(5, 0))

omenp = tk.Button(text='Pick Omen', command=lambda: instalock("Omen"),
                  fg='slateblue3', font=("Helvetica", 14))
omenp.grid(row=7, column=0, padx=(20, 0), pady=(5, 0))

phoenixp = tk.Button(text='Pick Phoenix', command=lambda: instalock("Phoenix"),
                     fg='red2', font=("Helvetica", 14))
phoenixp.grid(row=8, column=0, padx=(20, 0), pady=(5, 0))

razep = tk.Button(text='Pick Raze', command=lambda: instalock("Raze"),
                  fg='orange red', font=("Helvetica", 14))
razep.grid(row=9, column=0, padx=(20, 0), pady=(5, 0))


reynap = tk.Button(text='Pick Reyna', command=lambda: instalock("Reyna"),
                   fg='mediumpurple3', font=("Helvetica", 14))
reynap.grid(row=4, column=0, padx=(400, 0), pady=(5, 0))

sagep = tk.Button(text='Pick Sage', command=lambda: instalock("Sage"),
                  fg='turquoise1', font=("Helvetica", 14))
sagep.grid(row=5, column=0, padx=(400, 0), pady=(5, 0))

skyep = tk.Button(text='Pick Skye', command=lambda: instalock("Skye"),
                  fg='spring green', font=("Helvetica", 14))
skyep.grid(row=6, column=0, padx=(400, 0), pady=(5, 0))

sovap = tk.Button(text='Pick Sova', command=lambda: instalock("Sova"),
                  fg='cyan3', font=("Helvetica", 14))
sovap.grid(row=7, column=0, padx=(400, 0), pady=(5, 0))

viperp = tk.Button(text='Pick Viper', command=lambda: instalock("Viper"),
                   fg='orange red', font=("Helvetica", 14))
viperp.grid(row=8, column=0, padx=(400, 0), pady=(5, 0))

yorup = tk.Button(text='Pick Yoru', command=lambda: instalock("Yoru"),
                  fg='mediumpurple3', font=("Helvetica", 14))
yorup.grid(row=9, column=0, padx=(400, 0), pady=(5, 0))


exitp = tk.Button(text='Exit', command=lambda: exit(), fg='black', font=("Helvetica", 14))
exitp.grid(row=10, column=0, sticky="W", padx=(20, 0), pady=(30, 50))

tk_stop = tk.Label = Label(text="Stop Instalock by spamming 'P' Key", fg="black", font=('Helvetica', 14))
tk_stop.grid(row=10, column=0, padx=(200, 0), pady=(30, 50))

       
if __name__ == "__main__":
    window.mainloop()
