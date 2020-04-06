#!/usr/bin/python
# -*- coding: utf8 -*-

import comcop
import datetime
import time
import c
import csv
from operator import itemgetter
import numpy as np


def tiempo(FechaIni, FechaFin, actual):
	fecha1=datetime.datetime.now()
	fecha2=datetime.datetime.now()
	[Sirve1, fecha1]=validateDateEs(FechaIni)
	[Sirve2, fecha2]=validateDateEs(FechaFin)
	#c.k([fecha1,fecha2,Sirve1,Sirve2], 20203181821)
	if ( Sirve1 ) and (Sirve2 or FechaFin=='null') :
		#c.k([fecha1,fecha2], 20203181817)
		True
	if not(Sirve2) and actual=='true':
		fecha2=datetime.datetime.now()
	#c.k([fecha2,fecha1],20203181752)
	return (int((fecha2-fecha1).days))	

def validateDateEs(date):
	"""
	Funcion para validar una fecha en formato:
	Y-m-d	
	"""
	aprov=False
	result=	datetime.datetime.now()
	if (len(date)) == 12 :
		result=datetime.datetime.strptime(eval(date), "%Y-%m-%d")
		aprov=True		
	if (date) == 'null':
		aprov=True
		result=	datetime.datetime.now()
	return (aprov,result)

def Abrir(Archivo1,Archivo2):
		data=[]
		contador=0
		with open(Archivo1,  encoding='utf-8' ) as csvfile:
			csv_reader = csv.reader(csvfile, delimiter=',')	
			for row in csv_reader:
				#c.k([data], 20203191235)
				data=data+[[row[0], int(row[1])+200]]
				contador+=1
		with open(Archivo2,  encoding='utf-8' ) as csvfile:
			csv_reader = csv.reader(csvfile, delimiter=',')	
			for row in csv_reader:
				#c.k([data], 20203191235)
				data=data+[[row[0], int(row[1])+100]]
				contador+=1
		return sorted(data, key=itemgetter(1)), contador

def Personal(Archivo):
	personal=[]
	TamP=0
	with open(Archivo,  encoding='utf-8' ) as csvfile:
		#aBRIR PSICOTECNICO AQUI
		csv_reader = csv.reader(csvfile, delimiter=',')	
		concandi=0
		for row in csv_reader:
			personal=personal+[row]
			TamP+=1
	return personal, TamP

def formato(Archivo):
	
	personal=[]
	personalo=[]
	matriz=[]
	longRef=0
	TamP=0
	print('Se darà formato a la matriz')
	data, tam=Abrir('files/Profesiones.csv','files/Ocupaciones.csv')
	#c.k([len(data), tam],20203191441)
	personal,TamP=Personal(Archivo)
	#c.k(personal,20203191033)
	#c.k([TamP],20203191033)
	p=personal[0]
	listado=[p[0]]
	count=0
	#c.k(p,20203191545)	
	p2=[p]
	#print (p2)
	i=0
	vector=personal[0][0]
	while True:
		#print(len(personal[i][0]))
		#print(len(p2))
		
		if p[0]==personal[i+1][0]:
			
			p2=p2+[personal[i+1]]
			p=personal[i+1]
			
		else: 
			vector=vector+personal[i+1][0]
			
			p3=sorted(p2, key=itemgetter(1))
			listado=listado+[p3[0][0]]
			#print(len(p3[0]))
			#c.k(p3,20203191743)
			m=[]
			n=[]
			o=[]
			for l in p3:
				#print(l)
				m = m+[l[1]]	
				o=o+[l[2]]

			renglon=[]
			for j in data:
				
				#c.k(['Comparando ',j[1],m], 20203191627)
				if str(j[1]) in (m):
						
					renglon=renglon+[int(o[m.index(str(j[1]))])]
					#c.k(['agrupado coincidente', renglon], 20203191623)
				else:
					renglon=renglon+[0]
					#c.k(['agrupado no coincidente', renglon], 20203191623)
			if comcop.promedio(renglon[0:30])>100:
				##Đprint(renglon[0:30])
				False
			else:
				matriz=matriz+[renglon]	
			#c.k(['Longitud de la matriz es: ', len(matriz), 'Del renglon es: ', len(renglon)],20203191755)
			#c.k(['Provicional'], 20203191624)						
			#Crear nuevo vector
			p2=[personal[i+1]]
			p=personal[i+1]
			count+=1
		#c.k(p2, 20203191522)
		i=i+1
		if i==len(personal)-1:
			break

	#c.k([len(matriz)],20203191913)
	ochentaL= int((len(listado)-1)*0.80)
	ochentaM= int(len(matriz)*0.80)
	c.L(listado, 20204021900)
	c.L(matriz,20204021900)
	#c.k(['Se rettornan 2 matrices y dos vectores: ',['Listado: ', str(len(listado[0:ochentaL]))],['Matriz: '+str(len(matriz[0:ochentaM]))],['Listado: ',str(len(listado[ochentaL:len(listado)]))],['Matriz: ',str(len(matriz[ochentaM:len(matriz)]))]],20203192131)
	return np.array(listado[1:ochentaL+1]),np.matrix(matriz[0:ochentaM]),np.array(listado[ochentaL+2:len(listado)]),np.matrix(matriz[ochentaM+1:len(matriz)])
	#return (listado[0:ochentaL]),(matriz[0:ochentaM]),(listado[ochentaL:len(listado)]),(matriz[ochentaM:len(matriz)])
