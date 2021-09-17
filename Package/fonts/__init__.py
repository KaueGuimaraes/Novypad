import PySimpleGUI as sg
import os
from os import remove
from PySimpleGUI.PySimpleGUI import Window
from files import *


def changeFont(file, font):
    """
    -> Função para trocar a fonte do programa.
    :param file: Nome do arquivo que está salvo o tema atual.
    :param font: Novo tema a ser usado.
    """
    #Corrigindo erro do atual
    if ' (atual)' in font:
        return

    if exist(file):
        delete(file)

    create(file)
    write(file, font)

    createWindow('To change your font please restart the program.')


def fontEvent(event, fonts):
    """
    -> Função para verificar se alguma fonte foi escolhi na tela de opções de temas e altera-lo.
    :param event: Evento da biblioteca sg (PySimpleGUI).
    :param fonts: Opções de temas.
    """
    for item in fonts:
        if event in item:
            changeFont('font.txt', item)
            return True
    
    return False


def createFontsWindowButton(list, name='Window'):
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
        if fontEvent(event, list):
            return