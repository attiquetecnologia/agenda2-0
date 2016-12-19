#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class ClienteView:
    def __init__(self,toplevel):
        
        # Janela
        toplevel.title('Cadastro de Funcionarios')
        toplevel.geometry('800x220')
        
        # Espaçamento
        self.frmSpace = Frame(toplevel)
        self.frmSpace.pack()
        
        # Cria a barra de menus
        self.menubar = Menu(toplevel)
        toplevel.config(menu=self.menubar)
        
        # Cria o menu Arquivo
        menuArquivo = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo',menu=menuArquivo) # cria o menu Cadastros
        menuArquivo.add_command(label='Gravar')
        menuArquivo.add_command(label='Cancelar')
        menuArquivo.add_command(label='Sair') # Cria uma opção para o menu
        
        # Cria o menu Ajuda
        menuAjuda = Menu(self.menubar)
        self.menubar.add_cascade(label="Ajuda",menu=menuAjuda)
        menuAjuda.add_command(label='Sobre')
        menuAjuda.add_command(label='Versão')
        menuAjuda.add_command(label='Manual')
        
        ### FIM BARRA DE MENUS
        
        ### SESSÃO DE FRAMES
        
        self.frmSpace = Frame(toplevel)
        self.frmSpace.pack()
        Label(self.frmSpace,text='').pack()
 
        ### Armazena Nome, telefone e celular
        self.frmFrame1 = Frame(toplevel)
        self.frmFrame1.pack()
        ### Armazena email, site e aniversario
        self.frmFrame2 = Frame(toplevel)
        self.frmFrame2.pack()
        ### Armazena cpf e rg, Endereco
        self.frmFrame3 = Frame(toplevel)
        self.frmFrame3.pack()
        ### Armazena Endereco, Bairro e cep
        self.frmFrame4 = Frame(toplevel)
        self.frmFrame4.pack()
        ### Armazena Bairro,cep,Cidade, UF,
        self.frmFrame5 = Frame(toplevel)
        self.frmFrame5.pack()
        
        
        ### FIM DOS FRAMES
        
        ### CAMPOS
        
        # Nome do Cliente
        Label(self.frmFrame1,text='Nome',width=10,height=2).pack(side=LEFT)
        self.entNome = Entry(self.frmFrame1,width=35)
        self.entNome.pack(side=LEFT)
        
        #Telefone
        Label(self.frmFrame1,text='Telefone',width=10).pack(side=LEFT)
        self.entTelefone = Entry(self.frmFrame1,width=12)
        self.entTelefone.pack(side=LEFT)
        
        # Box Celular
        Label(self.frmFrame1,text='Celular',width=11).pack(side=LEFT)
        self.celular=Entry(self.frmFrame1,width=12)
        self.celular.pack(side=LEFT)
        
        # Box do Email
        Label(self.frmFrame2,text='Email',width=10).pack(side=LEFT)
        self.email=Entry(self.frmFrame2,width=25,)
        self.email.pack(side=LEFT)     
        
        # Box site
        Label(self.frmFrame2,text='Site',width=9).pack(side=LEFT)
        self.site=Entry(self.frmFrame2,width=25,)
        self.site.pack(side=LEFT)
        
        # Data de Aniversario
        Label(self.frmFrame2,text='Aniversário',width=10).pack(side=LEFT)
        self.aniversario=Entry(self.frmFrame2,width=11,)
        self.aniversario.pack(side=LEFT)
        
        # Box cpf
        Label(self.frmFrame3,text='CPF/CNPJ',width=10,height=2).pack(side=LEFT)
        self.cpf=Entry(self.frmFrame3,width=14,)
        self.cpf.pack(side=LEFT)

        # Box rg
        Label(self.frmFrame3,text='RG/IE',width=10).pack(side=LEFT)
        self.rg=Entry(self.frmFrame3,width=14,)
        self.rg.pack(side=LEFT)
        
        # Box Endereco
        Label(self.frmFrame3,text='   Endereço',width=17).pack(side=LEFT)
        self.endereco=Entry(self.frmFrame3,width=25,)
        self.endereco.pack(side=LEFT)
        
        # Box Bairro
        Label(self.frmFrame4,text='Bairro',width=10).pack(side=LEFT)
        self.bairro=Entry(self.frmFrame4,width=20,)
        self.bairro.pack(side=LEFT)
        
        # Box CEP
        Label(self.frmFrame4,text='CEP',width=10).pack(side=LEFT)
        self.cep=Entry(self.frmFrame4,width=12,)
        self.cep.pack(side=LEFT)
        
        # Box Cidade
        Label(self.frmFrame4,text='Cidade',width=10).pack(side=LEFT)
        self.cidade=Entry(self.frmFrame4,width=20,)
        self.cidade.pack(side=LEFT)
        
        # Box UF
        Label(self.frmFrame4,text='UF',width=5).pack(side=LEFT)
        estados = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA',
                   'MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN',
                   'RS','RO','RR','SC','SP','SE','TO']
        select = StringVar(self.frmFrame4)
        select.set(estados[24])
        self.uf=apply(OptionMenu,(self.frmFrame4,select)+tuple(estados))
        self.uf.pack(side=LEFT)
        
        # Salario
        Label(self.frmFrame5,text='Salario R$',width=10,height=2).pack(side=LEFT)
        self.f=Entry(self.frmFrame5,width=10,)
        self.f.pack(side=LEFT)
                      
        self.frmSpace = Frame(toplevel)
        self.frmSpace.pack()
        Label(self.frmSpace,text='').pack()
        
        # Botão Gravar
        self.frmButton = Frame(toplevel)
        self.frmButton.pack()
        self.btnGravar = Button(self.frmButton,text='Gravar',width=15)
        self.btnGravar.pack(side=LEFT)  
        # Botão Cancelar
        self.btnCancelar = Button(self.frmButton,text='Cancelar',width=15)
        self.btnCancelar.pack(side=RIGHT)

app = Tk()
ClienteView(app)
app.mainloop()