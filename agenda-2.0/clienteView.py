#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from map import *
import tkMessageBox
import sys
import sqlite3

#conn = sqlite3.connect('/home/rodrigo/workspace/agenda-2.0/data/agenda.db')
#cursor = conn.cursor()

class ClienteView:
    def __init__(self,toplevel):
        
        # Janela
        toplevel.title('Clientes')
        toplevel.geometry()
        
        # Cria a barra de menus
        self.menubar = Menu(toplevel)
        toplevel.config(menu=self.menubar)
        
        fonte=('12')
        
        # Cria o menu Arquivo
        menuArquivo = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo  ',font=fonte,menu=menuArquivo) # cria o menu Cadastros
        menuArquivo.add_command(label='Gravar    ',font=fonte,command=self.set_value)
        menuArquivo.add_command(label='Visualizar',font=fonte,command=self.get_value)
        menuArquivo.add_command(label='Sair      ',font=fonte,command=self.close) # Cria uma opção para o menu
        
        # Cria o menu Ajuda
        menuAjuda = Menu(self.menubar)
        self.menubar.add_cascade(label  = "Ajuda  ",font=fonte,menu=menuAjuda)
        menuAjuda.add_command(label     = 'Sobre  ',font=fonte,command=Ajuda().sobre)
        menuAjuda.add_command(label     = 'Versão ',font=fonte,command=Ajuda().versao)
        menuAjuda.add_command(label     = 'Manual ',font=fonte,command=Ajuda().manual)
        ### FIM BARRA DE MENUS
        
        Label(toplevel,font=fonte,text = 'Nome'         ).grid(row=1,column=1,pady=3,padx=3)
        Label(toplevel,font=fonte,text = 'Telefone'     ).grid(row=1,column=3,pady=3)
        Label(toplevel,font=fonte,text = 'Email'        ).grid(row=2,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'Celular'      ).grid(row=2,column=3,pady=3)
        Label(toplevel,font=fonte,text = 'Site'         ).grid(row=3,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'Aniversário'  ).grid(row=3,column=3,pady=3)
        Label(toplevel,font=fonte,text = 'Cpf/Cnpj'     ).grid(row=4,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'Pessoa'       ).grid(row=4,column=3,pady=3,columnspan=2)
        Label(toplevel,font=fonte,text = 'RG/IE'        ).grid(row=5,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'Endereço'     ).grid(row=6,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'Bairro'       ).grid(row=7,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'CEP'          ).grid(row=7,column=3,pady=3)
        Label(toplevel,font=fonte,text = 'Cidade'       ).grid(row=8,column=1,pady=3)
        Label(toplevel,font=fonte,text = 'UF'           ).grid(row=8,column=3,pady=3)
        
        self.entNome        = Entry(toplevel,width=30,font=fonte)
        self.entNome.grid(row=1,column=2)
        self.entTelefone    = Entry(toplevel,width=12,font=fonte)
        self.entTelefone.grid(row=1,column=4)
        self.entEmail       = Entry(toplevel,width=30,font=fonte)
        self.entEmail.grid(row=2,column=2)
        self.entCelular     = Entry(toplevel,width=12,font=fonte)
        self.entCelular.grid(row=2,column=4)
        self.entSite        = Entry(toplevel,width=30,font=fonte)
        self.entSite.grid(row=3,column=2)
        self.entAniversario = Entry(toplevel,width=12,font=fonte)
        self.entAniversario.grid(row=3,column=4)
        self.entCpfCnpj     = Entry(toplevel,width=30,font=fonte)
        self.entCpfCnpj.grid(row=4,column=2)
        self.entRgIe        = Entry(toplevel,width=30,font=fonte)
        self.entRgIe.grid(row=5,column=2)
        self.rdpFisica		= Radiobutton(toplevel,text='Fisica',font=fonte,value=1)
        self.rdpFisica.grid(row=5,column=3)
        self.rdpJuridica	= Radiobutton(toplevel,text='Jurídica',font=fonte,value=2)
        self.rdpJuridica.grid(row=5,column=4)
        self.entEndereco    = Entry(toplevel,width=30,font=fonte)
        self.entEndereco.grid(row=6,column=2)
        self.entBairro      = Entry(toplevel,width=30,font=fonte)
        self.entBairro.grid(row=7,column=2)
        self.entCep         = Entry(toplevel,width=12,font=fonte)
        self.entCep.grid(row=7,column=4)
        self.entCidade      = Entry(toplevel,width=30,font=fonte)
        self.entCidade.grid(row=8,column=2)
        estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
                   'MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN',
                   'RS','RO','RR','SC','SP','SE','TO']
        select = StringVar(toplevel)
        select.set(estados[24])
        self.entUf=apply(OptionMenu,(toplevel,select)+tuple(estados))
        self.entUf.grid(row=8,column=4,sticky=E+W)
        
        self.entObs = Text(toplevel,width=30,height=5,font=fonte)
        self.entObs.insert(INSERT,'Observações:')
        self.entObs.grid(row=9,column=1,columnspan=2,sticky=E+W)
        
        self.btnHddr   = Button(toplevel,text = 'Novo Hardware',command=Hardware().newHddr).grid(row=9,column=3,columnspan=2,sticky=E+W)
        
        self.btnGravar   = Button(toplevel,text = 'Gravar'  ,width=12,font=fonte,command=self.set_value)
        self.btnGravar.grid(row=10,column=2)
        self.btnCancelar = Button(toplevel,text = 'Cancelar',width=12,font=fonte,command=self.close).grid(row=10,column=3)
        
    def set_value(self):
        self.nome       = self.entNome.get()
        self.telefone   = self.entTelefone.get()
        self.celular    = self.entCelular.get()
        self.email      = self.entEmail.get()
        self.site       = self.entSite.get()
        self.aniversario= self.entAniversario.get()
        self.cpf        = self.entCpfCnpj.get()
        self.rg         = self.entRgIe.get()
#        self.obs        = self.entObs.get()
        try:
            cursor.execute("INSERT INTO pessoa(nome,telefone,celular,email,site,cpf,rg,aniversario) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"
                           % (self.nome,self.telefone,self.celular,self.email,self.site,self.cpf,self.rg,self.aniversario))
            conn.commit()
            box.showinfo('certo!','')
        except:
            box.showerror('Não gravo','')
            
    def get_value(self):
        try:
            cursor.execute("SELECT nome,telefone,celular,email,site,cpf,rg,aniversario FROM pessoa")
            for linha in cursor:
                print linha
        except:
            box.showerror('Não gravo','')
        
    def close(self):
        app.destroy()
        
app = Tk()
ClienteView(app)
app.mainloop()
