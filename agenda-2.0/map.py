#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox as box
import os
import commands
import sys
import string

#try:
#   import MySQLdb
#except:
#    box.showerror('Erro de importação', 'Modulo MySQLdb não encontrado!')
    
### Criando a conexão
#try:
#    conn = MySQLdb.connect('localhost','root','1235')
#except:
#    box.showerror('Erro de importação', 'Não foi possivel conectar ao banco de dados!')

class Principal(object):
    def __init__(self):
        pass
    
    def closeUI(self,app):
        app.destroy()

class Ajuda(object):
    def sobre(self):
        box.showinfo('Sobre', 
                     'MAP - Minha Agenda em Python\nEscrito por: Rodrigo Attique\ncontato@desenvolvesolucoes.net')
    def versao(self):
        box.showinfo('Versão', 'Versão: 2.0 Alfa')
        
    def manual(self):
        box.showinfo('Manual', 'Em desenvolvimento')
                
class Pessoa(object):
    def __init__(self,nome,tel):
        self.nome = nome
        self.tel = tel
        
        
    def maker(self):
        box.showinfo('Deu certo','Nome: ' + self.nome)
        print self.nome
                
                
class Cliente(Pessoa):
    def __init__(self):
        pass
    
    def insert(self):
        pass
    
    def visual(self):
        pass
    
    def cad_cli(self):
        os.system('python clienteView.py')
    
    def gravar(self):
        box.showinfo('Gravado com sucesso', 'Gravado com sucesso!')
        
        
class Hardware(object):
    def newHddr(self):
        os.system('python pcView.py')
