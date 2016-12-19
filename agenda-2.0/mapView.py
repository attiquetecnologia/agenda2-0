#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from map import *

class PrincipalView():
    def __init__(self,toplevel):
        
        # Cria a janela 
        toplevel.title("MAP-2.0-Alfa")
        toplevel.geometry('500x300')
        
        fonte=('12')
        
        # Cria a barra de menus
        self.menubar = Menu(toplevel)
        toplevel.config(menu=self.menubar)
        
        # Cria o menu Arquivo
        menuArquivo = Menu(self.menubar)
        self.menubar.add_cascade(label  = 'Arquivo' ,font=fonte,menu=menuArquivo)
        menuArquivo.add_command(label   = 'Backup'  ,font=fonte)
        menuArquivo.add_command(label   = 'Sair'    ,font=fonte,command=self.close)
        
        # Cria um menu Cadastroos
        menuCadastros = Menu(self.menubar)
        self.menubar.add_cascade(label  = 'Cadastros'   ,font=fonte,menu=menuCadastros) # cria o menu Cadastros
        menuCadastros.add_command(label = 'Clientes'    ,font=fonte,command=Cliente().cad_cli) # Cria uma opção para o menu
        menuCadastros.add_command(label = 'Funcionarios',font=fonte)
        
        # Cria o menu Consultas
        menuConsultas = Menu(self.menubar)
        self.menubar.add_cascade(label  = "Consultas"   ,font=fonte,menu=menuConsultas)
        menuConsultas.add_command(label = 'Clientes'    ,font=fonte)
        menuConsultas.add_command(label = 'Funcionarios',font=fonte)
        
        # Cria o menu Chamados
        menuChamados = Menu(self.menubar)
        self.menubar.add_cascade(label  = "Chamados"            ,font=fonte,menu=menuChamados)
        menuChamados.add_command(label  = 'Novo Chamado'        ,font=fonte)
        menuChamados.add_command(label  = 'Localizar Chamado'   ,font=fonte)
        
        # Cria o menu Ajuda
        menuAjuda = Menu(self.menubar)
        self.menubar.add_cascade(label  = "Ajuda" ,font=fonte,menu=menuAjuda)
        menuAjuda.add_command(label     = 'Sobre' ,font=fonte,command=Ajuda().sobre)
        menuAjuda.add_command(label     = 'Versão',font=fonte,command=Ajuda().versao)
        menuAjuda.add_command(label     = 'Manual',font=fonte,command=Ajuda().sobre)
		
		#elf.frame1 = Frame()
		#sself.frame1.pack()
		#self.button = Button(text="TESTE",font=fonte)
		#self.button.pack()
        
    def close(self):
        app.quit()
        
app = Tk()
PrincipalView(app)
app.mainloop() 
