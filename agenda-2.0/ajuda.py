#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox as box

class Ajuda:
    def sobre(self):
        box.showinfo('Sobre', 
                     'MAP - Minha Agenda em Python\nEscrito por: Rodrigo Attique\ncontato@desenvolvesolucoes.net')
    def versao(self):
        box.showinfo('Versão', 'Versão: 2.0 Alfa')
        
    def manual(self):
        box.showinfo('Manual', 'Em desenvolvimento')