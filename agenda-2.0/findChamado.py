# -*- coding: utf-8 -*-

from Tkinter import *

class NewChamadoView:
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
        menuArquivo.add_command(label='Close',command=self.Close) # Cria uma opção para o menu
        
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
        
        self.frmFind = Frame(toplevel)
        self.frmFind.pack()
        Label(self.frmFind,text='Pesquisar por:').pack()
        
        r1 = Radiobutton(toplevel,text='Option 1', value=1)
        r1.pack()
        
        r2 = Radiobutton(toplevel,text='Option 2', value=1)
        r2.pack()
        
        if r1:
            print 'lesvee'
        elif r2:
            print 'mesmo'
        
        # Numero do Chamado
        self.frmN_chamado = Frame(toplevel)
        self.frmN_chamado.pack()
        Label(self.frmN_chamado,text=' Nº do Chamado',width=15).pack(side=LEFT)
        self.entN_chamado = Entry(self.frmN_chamado,width=10)
        self.entN_chamado.pack(side=RIGHT)
        
        # Chamado
        self.frmChamado = Frame(toplevel)
        self.frmChamado.pack()
        Label(self.frmChamado,text='Chamado',width=10).pack(side=LEFT)
        self.entChamado = Entry(self.frmChamado,width=20)
        self.entChamado.pack(side=RIGHT)
        
        # Data do chamado
        self.frmDtChamado = Frame(toplevel)
        self.frmDtChamado.pack()
        Label(self.frmDtChamado,text='Data',width=10).pack(side=LEFT)
        self.spinDia = Spinbox(self.frmDtChamado,width=3,from_=1, to=31)
        self.spinDia.pack(side=LEFT)        
        self.spinMes = Spinbox(self.frmDtChamado,width=3,from_=1, to=12)
        self.spinMes.pack(side=LEFT)
        self.spinAno = Spinbox(self.frmDtChamado,width=5,from_=2012, to=2031)
        self.spinAno.pack(side=LEFT)
        
        # Tipo
        self.frmTipo = Frame(toplevel)
        self.frmTipo.pack()
        Label(self.frmTipo,text='Tipo',width=10).pack(side=LEFT)
        self.entTipo = Entry(self.frmTipo,width=20)
        self.entTipo.pack(side=RIGHT)
        
        # Nome do Cliente
        self.frmCliente = Frame(toplevel)
        self.frmCliente.pack()
        Label(self.frmCliente,text='Cliente',width=10).pack(side=LEFT)
        self.entCliente = Entry(self.frmCliente,width=20)
        self.entCliente.pack(side=RIGHT)
        
        # Nome do Funcionario
        self.frmFuncionario = Frame(toplevel)
        self.frmFuncionario.pack()
        Label(self.frmFuncionario,text='Funcionario',width=10).pack(side=LEFT)
        self.entFuncionario = Entry(self.frmFuncionario,width=20)
        self.entFuncionario.pack(side=RIGHT)
        
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
        
        
    def Close(self):
        app.destroy()
        
app = Tk()
NewChamadoView(app)
app.mainloop()