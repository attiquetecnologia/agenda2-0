#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class pcView:
    def __init__(self,toplevel):
        
        # Janela
        toplevel.title('Cadastro de computadores')
        toplevel.geometry()
        
        # Espaçamento
        self.frmSpace = Frame(toplevel)
        self.frmSpace.pack()
        Label(self.frmSpace,height=2,text= '').pack()
        
        self.frmCpu= Frame(toplevel)
        self.frmCpu.pack()
        Label(self.frmCpu,width=10,height=2,text= 'Processador').pack(side=LEFT)
        self.cpu = Entry(self.frmCpu,width=20)
        self.cpu.pack(side=LEFT)
        
        self.frmRam= Frame(toplevel)
        self.frmRam.pack()
        Label(self.frmRam,width=10,height=2,text= 'Memória').pack(side=LEFT)
        self.ram = Entry(self.frmRam,width=20)
        self.ram.pack(side=LEFT)
        
        self.frmHd= Frame(toplevel)
        self.frmHd.pack()
        Label(self.frmHd,width=10,height=2,text= 'Disco').pack(side=LEFT)
        self.hd = Entry(self.frmHd,width=20)
        self.hd.pack(side=LEFT)
        
        self.frmSo= Frame(toplevel)
        self.frmSo.pack()
        Label(self.frmSo,text='Sistema',width=10,height=2).pack(side=LEFT)
        self.so = Entry(self.frmSo,width=20)
        self.so.pack(side=LEFT)
        
        self.frmOutros= Frame(toplevel).pack()
        self.outros = Text(self.frmOutros,height=4,width=35)
        self.outros.insert(INSERT,'Resto das peças')
        self.outros.pack()
        
        # Botão Gravar
        self.frmButton = Frame(toplevel)
        self.frmButton.pack()
        self.btnGravar = Button(self.frmButton,text='Gravar',width=15)
        self.btnGravar.pack(side=LEFT)  
        # Botão Cancelar
        self.btnCancelar = Button(self.frmButton,text='Cancelar',width=15,command=self.close)
        self.btnCancelar.pack(side=LEFT)
    def close(self):
        app.destroy()

app = Tk()
pcView(app)
app.mainloop()