# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:15:12 2021

@author: Louis
"""
import math

def encondePassword(password):
    encript=[]
    for n in range(20):
        x=ord(password[n])
        encriptPeriod=1.4*math.cos(2.1*x+3)+math.cos(4.3*x+2)+0.2*math.cos(12*x+5)
        if n != 0:
            encript.append(encriptPeriod+encript[n-1])
        else:
            encript.append(encriptPeriod)
    return encript


userDictionary={}


cheese=True
while cheese == True:
    option=input("Login or signup? (l/s)\n")
    if option=="l":
        cheese2=True
        while cheese2==True:
            username : str =input("username:\n")
            password : str =input("password:\n")
            try:
                if encondePassword(password) == userDictionary[username]:
                    cheese=False
                    cheese2=False
                    print("Access Granted")
                    del password
                else:
                    exitt=input("Incorrect username or password. (e to exit)\t")
                    if exitt=="e":
                        cheese2=False
            except KeyError:
                exitt=input("Incorrect username or password. (e to exit)\t")
                if exitt=="e":
                    cheese2=False
    
    elif option=="s":
        username : str =input("username:\n")
        password : str =input("password:\n")
        userDictionary.update({username : encondePassword(password)})
        


#%%



import PySimpleGUI as sg

sg.Window(title="Louis' App", layout=[[]], margins=(100, 50)).read()

#%%


import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK"), sg.Button('Close Window')], [sg.InputText('', size=(10,1), key='cheese')]]

# Create the window
window = sg.Window("Demo", layout)
event, values = window.Read()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == 'OK':
        cheese2 = int(values['cheese'])
    if event == "Close Window" or event == sg.WIN_CLOSED:
        break

window.close()


#%%



import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
cheeseeee="Input Text to display"
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text(cheeseeee)]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])
    cheeseeee=values[0]

window.close()
































