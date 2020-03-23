#!/usr/bin/python
# -*- coding: utf8 -*-
#Libería

import random

def promedio(vector):
	ac=0
	aa=0
	for i in vector:
		ac=ac+1
		aa=aa+1
	
	
	return aa/ac

def moda(lista):
	aux =0
	cont=0
	resultado=0
	#print(lista)
	lista.sort( key=None, reverse=False)
	
	for i in range(len(lista)-1):
		if lista[i]>99:
			if lista[i]==lista[i+1]:	
				cont=cont+1
				if cont>= aux:
					aux=cont
					resultado=lista[i]
			else:
				cont=0
	#print('==========\n=======\n=======\n')	
	#print(lista)
	return resultado

def antiSplit(Vector):
	cadena=''
	for i in Vector:
		if i!= ' ':
			cadena=cadena+i+' '
		#print(i)
	return cadena

def Cadena(vector):
	cadena=''
	for i in vector:
		cadena=cadena+i
	return cadena