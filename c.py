#!/usr/bin/python
# -*- coding: utf8 -*-
#Librería

import os, sys
import datetime

def k(entrada,Linea):
	imprimir(str(datetime.datetime.now()) +' Linea ' +str(Linea),'logs/logs.CMP')
	for i in (entrada):
		imprimir('\t'+ str(i),'logs/logs.CMP')
	return 0

def L(entrada,Linea):
	j=0
	imprimir(str(datetime.datetime.now()) +' Linea ' +str(Linea),'logs/Salida.txt')
	for i in (entrada):
		j+=1
		imprimir('  '+str(j)+'-  '+ str(i),'logs/Salida.txt')
	return 0


def imprimir(frase,files):
	sys.stdout=open("logs/tmpfras","w")
	print(frase)
	sys.stdout.close()
	concatenar(files)
	os.system('rm logs/tmpfras')
	sys.stdout = sys.__stdout__
	return 0

def concatenar(files):
	os.system('echo "$(cat logs/tmpfras)" >> '+files)
	return 0