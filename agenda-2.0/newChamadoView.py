#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from map import Principal

class NewChamadoView(Principal):
    def __init__(self,toplevel):
        
              
        # Cria a janela 
        toplevel.title("Novo Chamado")
        toplevel.geometry()
        
        ### SESSÃO DA BARRA DE MENUS
        
        # Cria a barra de menus
        self.menubar = Menu(toplevel)
        toplevel.config(menu=self.menubar)
        
        # Cria o menu Arquivo
        menuArquivo = Menu(self.menubar)
        self.menubar.add_cascade(label='Arquivo',menu=menuArquivo) # cria o menu Cadastros
        menuArquivo.add_command(label='Close',command=self.close) # Cria uma opção para o menu
        
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
        
        # Numero do Chamado
#        self.frmN_chamado = Frame(toplevel)
#        self.frmN_chamado.pack()
#        Label(self.frmN_chamado,text=' Nº do Chamado',width=15).pack(side=LEFT)
#        self.entN_chamado = Entry(self.frmN_chamado,width=10)
#        self.entN_chamado.pack(side=RIGHT)
        
        # Chamado
        self.frmChamado = Frame(toplevel)
        self.frmChamado.pack()
        Label(self.frmChamado,text='Chamado',width=10,height=2).pack(side=LEFT)
        self.entChamado = Entry(self.frmChamado,width=20)
        self.entChamado.pack(side=LEFT)
        
        # Data do chamado
        self.frmDtChamado = Frame(toplevel)
        self.frmDtChamado.pack()
        Label(self.frmDtChamado,text='Data',width=12,height=2).pack(side=LEFT)
        self.spinDia = Spinbox(self.frmDtChamado,width=3,from_=1, to=31)
        self.spinDia.pack(side=LEFT)        
        self.spinMes = Spinbox(self.frmDtChamado,width=3,from_=1, to=12)
        self.spinMes.pack(side=LEFT)
        self.spinAno = Spinbox(self.frmDtChamado,width=5,from_=2012, to=2031)
        self.spinAno.pack(side=LEFT)
        
        # Tipo
        self.frmTipo = Frame(toplevel)
        self.frmTipo.pack()
        Label(self.frmTipo,text='Tipo: ',width=10,height=2).pack(side=LEFT)
        self.r1Tipo = Radiobutton(self.frmTipo,value=1,text='Normal')
        self.r1Tipo.pack(side=LEFT)
        self.r2Tipo = Radiobutton(self.frmTipo,value=2,text='Urgente')
        self.r2Tipo.pack(side=LEFT)
        
        # Nome do Cliente
        self.frmCliente = Frame(toplevel)
        self.frmCliente.pack()
        Label(self.frmCliente,text='Cliente',width=10,height=2).pack(side=LEFT)
        self.entCliente = Entry(self.frmCliente,width=15)
        self.entCliente.pack(side=LEFT)
        self.btnFindCli = Button(self.frmCliente,text='...')
        self.btnFindCli.pack(side=LEFT)
        
        # Nome do Funcionario
        self.frmFuncionario = Frame(toplevel)
        self.frmFuncionario.pack()
        Label(self.frmFuncionario,text='Funcionario',width=10,height=2).pack(side=LEFT)
        funcionario = ['Rodrigo Attique','Eduardo Attique']
        select = StringVar(self.frmFuncionario)
        select.set(funcionario[0])
        self.funcionario=apply(OptionMenu,(self.frmFuncionario,select)+tuple(funcionario))
        self.funcionario.pack(side=LEFT)
        
        self.obs=Text(toplevel,height=5,width=30)
        self.obs.pack()
        
        self.frmSpace = Frame(toplevel)
        self.frmSpace.pack()
        Label(self.frmSpace,text='').pack()
        
        # Botão Gravar
        self.frmButton = Frame(toplevel)
        self.frmButton.pack()
        self.btnGravar = Button(self.frmButton,text='Gravar',width=15,command=self.msg)
        self.btnGravar.pack(side=LEFT)  
        # Botão Cancelar
        self.btnCancelar = Button(self.frmButton,text='Cancelar',width=15,command=self.close)
        self.btnCancelar.pack(side=RIGHT)
        
    def close(self):
        app.destroy()
        
app = Tk()
NewChamadoView(app)
app.mainloop()