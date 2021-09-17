import PySimpleGUI as sg
from files import *
from themes import *
from fonts import *


#Definindo o tema
theme = 'theme.txt'
themes = ['Dark', 'DarkAmber', 'DarkBrown1', 'DarkBrown4', 'DarkGrey', 'System Default']

if not exist(theme):
    create(theme)
    write(theme, 'DarkBrown')

temaAtual = read(theme)
sg.ChangeLookAndFeel(temaAtual)


#Detectando o tema
for c in range(0, len(themes)):
    if themes[c] == temaAtual:
        themes[c] = themes[c] + ' (atual)'


#Cópia do sistema de Tema, depois fazer uma função talvez.
#Definindo a fonte
font = 'font.txt'
fonts = ['Arial', 'Consolas', 'Arbery', 'Ink Free', 'Impact', 'Palooka BB', 'GOOD PEOPLE', 'Wild Words Roman BR']

if not exist(font):
    create(font)
    write(font, 'Consolas')

fontAtual = read(font)


#Detectando a fonte
for c in range(0, len(fonts)):
    if fonts[c] == fontAtual:
        fonts[c] = fonts[c] + ' (atual)'


about = '''Version 1.4
Authors: A Cultist and Kauê Guimarães
--------------------------//--------------------------------
A Cultist Instagram: @ldmasterken
Kauê Guimarães Instagram: @kaueguimaraesk'''
update = '''- Fonts'''
WIN_W = 90
WIN_H = 25
filename = None

file_new = 'New NovyTxt.............(CTRL+N)'
file_open = 'Open..............(CTRL+O)'
file_save = 'Save............(CTRL+S)'

menu_layout = [['File', [file_new, file_open, file_save, 'Save as', '---', 'Leave']],
                     ['Settings', ['Themes', 'Fonts']],
                     ['Help', ['About', 'New']]]

layout = [[sg.Menu(menu_layout)],
                [sg.Text('> New NovyTxt <', font=('Consolas', 10), size=(WIN_W, 1), key='_INFO_')],
                [sg.Multiline(font=(fontAtual, 12), size=(WIN_W, WIN_H), key='_BODY_')]]
window = sg.Window('NovyPad 1.4', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True)
window.read(1)
window['_BODY_'].expand(True, True)


while True:
    event, values = window.read()
    
    if event in (None, 'Leave'):
        break
    if event in (file_new, 'n:78'):
        filename = new_file(window)
    if event in (file_open, 'o:79'):
        filename = open_file(window)
    if event in (file_save, 's:83'):
        save_file(window, values, filename)
    if event in ('Save as',):
        filename = save_file_as(window, values)
    if event in ('About',):
        createWindow(about, 'About')
    if event in ('New',):
        createWindow(update, 'New')

    #Themes
    if event in ('Themes',):
        createThemesWindowButton(themes, 'Themes')
    
    #Fonts
    if event in ('Fonts',):
        createFontsWindowButton(fonts, 'Fonts')