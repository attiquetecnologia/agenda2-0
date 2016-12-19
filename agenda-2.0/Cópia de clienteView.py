#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from ajuda import Ajuda


class ClienteView:
    def __init__(self,toplevel):
        
        # Janela
        toplevel.title('Clientes')
        toplevel.geometry()
        
        # Cria a barra de menus
        self.menubar = Menu(toplevel)
        toplevel.config(menu=self.menubar)
        
        fonte=('Arial','11')
        
        # Cria o menu Arquivo
        menuArquivo = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo  ',font=fonte,menu=menuArquivo) # cria o menu Cadastros
        menuArquivo.add_command(label='Gravar    ',font=fonte)
        menuArquivo.add_command(label='Sair      ',font=fonte,command=self.close) # Cria uma opção para o menu
        
        # Cria o menu Ajuda
        menuAjuda = Menu(self.menubar)
        self.menubar.add_cascade(label  = "Ajuda  ",font=fonte,menu=menuAjuda)
        menuAjuda.add_command(label     = 'Sobre  ',font=fonte,command=Ajuda().sobre)
        menuAjuda.add_command(label     = 'Versão ',font=fonte,command=Ajuda().versao)
        menuAjuda.add_command(label     = 'Manual ',font=fonte,command=Ajuda().manual)
        ### FIM BARRA DE MENUS
        
        ### CAMPOS Label da coluna 1
        Label(toplevel,text='Nome ',     width=10,height=1,font=fonte).grid(column=1,row=2,sticky=W,pady=3)
        Label(toplevel,text='Telefone ',    width=10,height=1,font=fonte).grid(column=1,row=3,sticky=W,pady=3)
        #Label(toplevel,text='Email ',    width=10,height=1,font=fonte).grid(column=1,row=3,sticky=W,pady=3)
        Label(toplevel,text='CPF/CNPJ ', width=10,height=1,font=fonte).grid(column=1,row=4,sticky=W,pady=3)
        Label(toplevel,text='Bairro ',   width=10,height=1,font=fonte).grid(column=1,row=5,sticky=W,pady=3)
        
        ### Campos da coluna 2
        
        # Nome do Cliente
        self.entNome = Entry(toplevel,width=35,font=fonte).grid(column=2,row=2,sticky=E+W)
        # Box do telefone
        self.telefone   = Entry(toplevel,width=12,font=fonte).grid(column=2,row=3)
        # Box do Email
        #self.email   = Entry(toplevel,width=25,font=fonte).grid(column=2,row=3,sticky=E+W)     
        # Box cpf
        self.cpf     = Entry(toplevel,width=14,font=fonte).grid(column=2,row=4,sticky=E+W)
        # Box Bairro
        self.bairro  = Entry(toplevel,width=20,font=fonte).grid(column=2,row=5,sticky=E+W)
        
        ### Campos da Coluna 3
        Label(toplevel,text ='Telefone '  ,width=10,font=fonte).grid(column=3,row=2,sticky=W)
        Label(toplevel,text ='Site '      ,width=9,font=fonte).grid(column=3,row=3,sticky=W)
        Label(toplevel,text ='RG/IE '     ,width=10,font=fonte).grid(column=3,row=4,sticky=W)
        
        ### Camos da Coluna 4
        #Telefone
        self.entTelefone = Entry(toplevel,width=12,font=fonte).grid(column=4,row=2,sticky=W)
        # Box site
        self.entSite     = Entry(toplevel,width=25,font=fonte).grid(column=4,row=3,sticky=E+W)
        # Box rg
        self.rg          = Entry(toplevel,width=14,font=fonte).grid(column=4,row=4,sticky=E+W)
        
        # Box Celular
        Label(toplevel,text='Celular',width=11).grid(column=4,row=2,columnspan=2)
        self.celular=Entry(toplevel,width=12)
        self.celular.grid(column=5,row=2)
        
        
        # Data de Aniversario
        Label(toplevel,text='Aniversário',width=10).grid(column=5,row=3)
        self.aniversario=Entry(toplevel,width=11,)
        self.aniversario.grid(column=6,row=3)   
        
        # Box Endereco
        Label(toplevel,text='   Endereço',width=17).grid(column=5,row=4)
        self.endereco=Entry(toplevel,width=25,)
        self.endereco.grid(column=6,row=4)
        
        
        
        # Box CEP
        Label(toplevel,text='CEP',width=10).grid(column=3,row=5)
        self.cep=Entry(toplevel,width=12,)
        self.cep.grid(column=3,row=5)
        
        # Box Cidade
        Label(toplevel,text='Cidade',width=8).grid(column=4,row=5)
        self.cidade=Entry(toplevel,width=20,)
        self.cidade.grid(column=5,row=5)
        
        # Box UF
        Label(toplevel,text='UF',width=3).grid(column=6,row=5)
        estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
                   'MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN',
                   'RS','RO','RR','SC','SP','SE','TO']
        select = StringVar(toplevel)
        select.set(estados[24])
        self.uf=apply(OptionMenu,(toplevel,select)+tuple(estados))
        self.uf.grid(column=6,row=5)
        '''
        # Observações
        self.obs = Text(toplevel,height=5,width=40)
        self.obs.insert(INSERT,"observações")
        self.obs.grid(column=1,row=6)
        self.btnNovoHdwr = Button(toplevel,text='Adicionar novo hardware')
        self.btnNovoHdwr.grid(column=2,row=6)
        '''
        self.btnGravar = Button(toplevel,text='Gravar',width=15)
        self.btnGravar.grid(column=1,row=7)  
        # Botão Cancelar
        self.btnCancelar = Button(toplevel,text='Cancelar',width=15,command=self.close)
        self.btnCancelar.grid(column=2,row=7)
        
    def close(self):
        app.destroy()
        
app = Tk()
ClienteView(app)
app.mainloop()