import PySimpleGUI as sg
import os
from os import remove
from PySimpleGUI.PySimpleGUI import Window, theme
from files import *


def changeTheme(file, theme):
    """
    -> Função para trocar o tema do programa.
    :param file: Nome do arquivo que está salvo o tema atual.
    :param theme: Novo tema a ser usado.
    """
    #Corrigindo erro do atual
    if ' (atual)' in theme:
        return

    if exist(file):
        delete(file)

    create(file)
    write(file, theme)

    createWindow('To change your theme please restart the program.')


def themeEvent(event, themes):
    """
    -> Função para verificar se algum tema foi escolhi na tela de opções de temas e altera-lo.
    :param event: Evento da biblioteca sg (PySimpleGUI).
    :param themes: Opções de temas.
    """
    for item in themes:
        if event in item:
            changeTheme('theme.txt', item)
            return True
    
    return False


def createThemesWindowButton(list, name='Window'):
    """
    -> Função para criar uma janela com opções de temas.
    :param list: Opções de temas a serem escolhidos.
    :param name: (Opcional) Nome da janela
    """
    layout = [[]]
    cont = 0
    linha = 0
    for tema in list:
        layout[linha].append(sg.Button(list[cont]))
        cont += 1
        if cont % 3 == 0:
            layout.append([])
            linha += 1
    
    while True:
        event, values = sg.Window(name, layout, auto_close=False).read(close=True)
        if themeEvent(event, list):
            return