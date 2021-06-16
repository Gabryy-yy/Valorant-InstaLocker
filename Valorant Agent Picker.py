from functools import cmp_to_key
from os import close
from tkinter.constants import COMMAND, LEFT
import keyboard
import pyautogui as pg
import time
from tkinter import Text, Tk, Label, Button, font
import tkinter as tk
import webbrowser
import pynput

window=tk.Tk()
window.geometry("650x420")
window.title("Valorant Instalocker Console")
window.resizable(False, False)

def telegram():
    webbrowser.open_new_tab('t.me/TalkToGabry_bot')
    
def astra():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(666, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 
        
        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break

def breach():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(750, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def brim():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(834, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def cypher():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(918, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def jett():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1002, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break

def killjoy():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1086, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def omen():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1170, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def phoenix():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1254, 925)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break

def raze():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(666, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def reyna():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(750, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def sage(): 
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(834, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def skye():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(918, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def sova():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1002, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def viper():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1086, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
def yoru():
    text_output = Label(window, text="OK! Now go play and carry your team!", fg='black', font=("Helvetica", 11))
    text_output.grid(row=13, column=0, padx=170, sticky='W')
    while True:
        pg.moveTo(1170, 1015)
        pg.doubleClick()
        pg.PAUSE=0.035
        pg.moveTo(954, 812)
        pg.doubleClick() 

        try:  
            if keyboard.is_pressed('p'):  
                print('Loop fermato')
                break  
        except:
            break
        
astrap = tk.Button(text='Pick Astra', command=astra, fg='purple', font=("Helvetica", 14))
astrap.grid(row=4, column=0, sticky='W')

breachp = tk.Button(text='Pick Breach', command=breach, fg='OrangeRed4', font=("Helvetica", 14))
breachp.grid(row=5, column=0, sticky="W")

brimp = tk.Button(text="Pick Brim", command=brim, fg='orange2', font=("Helvetica", 14))
brimp.grid(row=6, column=0, sticky="W")

cypherp = tk.Button(text="Pick Cypher", command=cypher, fg='LightBlue3', font=("Helvetica", 14))
cypherp.grid(row=7, column=0, sticky="W")

jettp = tk.Button(text='Pick Jett', command=jett, fg='skyblue1', font=("Helvetica", 14))
jettp.grid(row=8, column=0, sticky="W")

killjoyp = tk.Button(text='Pick Killjoy', command=killjoy, fg='gold', font=("Helvetica", 14))
killjoyp.grid(row=9, column=0, sticky="W")

omenp = tk.Button(text='Pick Omen', command=omen, fg='slateblue3', font=("Helvetica", 14))
omenp.grid(row=10, column=0, sticky="W")

phoenixp = tk.Button(text='Pick Phoenix', command=phoenix, fg='red2', font=("Helvetica", 14))
phoenixp.grid(row=4, column=0, padx=400, sticky="W")

razep = tk.Button(text= 'Pick Raze', command=raze, fg='orange red', font=('Helvetica', 14))
razep.grid(row=5, column=0, padx=400, sticky='W')

reynap = tk.Button(text='Pick Reyna', command=reyna, fg='mediumpurple3', font=("Helvetica", 14))
reynap.grid(row=6, column=0, padx=400, sticky="W")

sagep = tk.Button(text='Pick Sage', command=sage, fg='turquoise1', font=("Helvetica", 14))
sagep.grid(row=7, column=0, padx=400, sticky="W")

skyep = tk.Button(text='Pick Skye', command=skye, fg='spring green', font=("Helvetica", 14))
skyep.grid(row=8, column=0, padx=400, sticky="W")

sovap = tk.Button(text='Pick Sova', command=sova, fg='cyan3', font=("Helvetica", 14))
sovap.grid(row=9, column=0, padx=400, sticky="W")

viperp = tk.Button(text = 'Pick Viper', command=viper, fg='forest green', font=("Helvetica", 14))
viperp.grid(row=10, column=0, padx=400, sticky="W")

yorup = tk.Button(text='Pick Yoru', command=yoru, fg='medium blue', font=("Helvetica", 14))
yorup.grid(row=11, column=0, padx=400, sticky="W")

first_button = tk.Button(text="For any kind of problem, contact me on telegram by pressing this button", command=telegram, fg='black', font=("Helvetica", 14))
first_button.grid(row=2, column=0, sticky='W')

tk.stop = tk.Label = Label(text="To stop the program, spam 'P'", fg="black", font=('Helvetica', 14))
tk.stop.grid(row= 11, column=0, sticky='W')

tk.titolo = tk.Label = Label(text='Valorant agent picker by @Ga6r13l3', fg='black', font=("Helvetica", 14))
tk.titolo.grid(row=1, column=0, padx=170, sticky='W')
       
if __name__ == "__main__":
    window.mainloop()