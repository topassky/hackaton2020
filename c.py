#!/usr/bin/python
# -*- coding: utf8 -*-
#Librería

import os, sys
import datetime

def k(entrada,Linea):
	imprimir(str(datetime.datetime.now()) +' Linea ' +str(Linea))
	for i in (entrada):
		imprimir('\t'+ str(i))
	return 0

def imprimir(frase):
	sys.stdout=open("logs/tmpfras","w")
	print(frase)
	sys.stdout.close()
	concatenar()
	os.system('rm logs/tmpfras')
	sys.stdout = sys.__stdout__
	return 0

def concatenar():
	os.system('echo "$(cat logs/tmpfras)" >> logs/logs.CMP')
	return 0