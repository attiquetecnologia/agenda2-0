#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pessoa(object):
	__codigo = None
	__nome = None
	__email = None
	
	def __init__(self,codigo,nome,email):
		self.codigo = codigo
		self.nome = nome
		self.email = email
		

class Teste(object):
	
nome = raw_input('noME: ')
email = raw_input('eamil: ')
codigo = raw_input('codi: ')

p = Pessoa(codigo,nome,email)

