#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkMessageBox as box 

class pcView:
    def __init__(self,toplevel):
        
        fonte=('11')
        
        # Janela
        toplevel.title('Cadastro de computadores')
        toplevel.geometry()
        
        Label(toplevel,text= 'Processador ',font=fonte).grid(column=1,row=1,pady=3,sticky=W)
        self.cpu = Entry(toplevel,width=20,font=fonte)
        self.cpu.grid(column=2,row=1,pady=3)
        self.cpu.focus_force()
        
        Label(toplevel,text= 'Memória ',font=fonte).grid(column=1,row=2,pady=3,sticky=W)
        self.ram = Entry(toplevel,width=20,font=fonte)
        self.ram.grid(column=2,row=2,pady=3)
        
        Label(toplevel,text= 'Disco ',font=fonte).grid(column=1,row=3,pady=3,sticky=W)
        self.cpu = Entry(toplevel,width=20,font=fonte)
        self.cpu.grid(column=2,row=3,pady=3)
        
        Label(toplevel,text= 'MotherBoard', font=fonte).grid(column=1,row=4,pady=3,sticky=W)
        self.board = Entry(toplevel,width=20,font=fonte)
        self.board.grid(column=2,row=4,pady=3)
        
        self.resto = Text(toplevel,width=32,height=5,font=fonte)
        self.resto.grid(column=1,row=5,columnspan=2)
        self.resto.insert(INSERT,"Restante do equipamento")
        
        self.btnOk      = Button(toplevel,text= 'OK', width=10,font=fonte,command=self.ok).grid(column=1,
                                                            row=6,sticky=E+W,pady=3)
        self.btnCancel  = Button(toplevel,text= 'Cancelar', width=10,font=fonte,command=self.close).grid(column=2,
                                                            row=6,sticky=E+W,pady=3)
        
    def close(self):
        app.destroy()
        
    def ok(self):
        __doc__ = '''
        Deveria chamar um construtor que
        deixasse esses dados para serem 
        inseridos junto com o cadastro
        vamos ver oque vou fazer!
        '''
        app.destroy()
        

app = Tk()
pcView(app)
app.mainloop()