#!/usr/bin/python
# -*- coding: utf8 -*-

import csv
import os, sys
import datetime
import Analizar
import c
import comcop

sys.stdout.encoding

def pareado(acomparar ,data, identificador,index,EmpleoFormacionpsico):
	c.k([acomparar], 20203201644)
	#####c.k(['acomparar',acomparar],15)
	####c.k(['data'	,data],15)
	####c.k(['id',identificador],15)
	palabrasEXT=''
	resultado=0
	contadori=100
	resultados=[]
	resultadoV=0
	modificar=1
	encontrada=False
	k=[]
	
	#print (acomparar)
	palabras=comcop.antiSplit(acomparar).split(' ')
	###c.k(palabras,23)
	contadorj=0
	modificar=1
	for palabra in palabras:
		contadorj=contadorj+1
		encontrada=False
		if palabra!= ' ' and len(palabra)>2:
			contadori=99
			###c.k([palabra], 3333)
			for i in data:
				contadori=contadori+1
				#c.k([str(contadori)], 30)

								
				if palabra[1:len(palabra)-3].lower() in i.lower():
					#c.k(['coincide '+ palabra+'  dentro de'+ i], 37)
					####c.k(['Se agregarà un posible tipo '+str(contadori)],38)
					modificar=0
					encontrada=True
					if contadori>100:
						resultados.append(contadori)
						#print(['Resultados']+resultados)
						#c.k([resultados, palabra],42)
		if not(encontrada):
			
			palabrasEXT=palabrasEXT+str(palabra).lower()+' '


	#####c.k(['modificar vale 1', modificar],43435)
	modificar=1
	for palabra in (palabrasEXT).split():
		if len(palabra)>2:
			print (palabras)
			if EmpleoFormacionpsico==100:
				print('=========Experiencia Laboral====== ')
			if EmpleoFormacionpsico==10:
				print('=========Educación====== ')
			for i in range(1,len(identificador)):						
				print([str(identificador[i])+'----'+ str(i) ])
			resultado=int(input('-->'+palabra+'<--'+' a que corresponde?: '))
			resultado=resultado-1
			NuevoT=''
			if resultado>=i:
				NuevoT=str(input('Ingrese nuevo tipo: '))
				data=data+[palabra]
				identificador=identificador+[NuevoT]
				#c.k([identificador],2020318134)
			else:
				resultado=resultado+100
				data[resultado-100+1]= data[resultado-100+1]+' '  +palabra
			if resultado>101:
				resultados.append(resultado)
	

		
		
	
	#####c.k(['El resultado es '+str(resultado)],64)
	#####c.k(k,99)
	#Gurdar

	######c.k(['rutina para guardar nuevo files/csv'],34)
	#data---------->csvlñ-<
	#index--------->csv
	#identificador->csv
	if EmpleoFormacionpsico==100:
		resultado=comcop.moda(resultados)
		with open('files/nuevaList.csv', 'w', newline='') as csvfileS2:
			#c.k(['Se ha abierto file'], 202031723)
			employee_writer2 = csv.writer(csvfileS2) 
			for k in range(1,len(identificador)):
				f7(data[k])
				#c.k([data],202021815)
				#print((['len id', len(identificador),'index', len(index),'data ', len(data2)]))
				##c.k([identificador[k],str(int(resultado)),data[k]],20203181212)
				employee_writer2.writerow([identificador[k],str(int(k)),data[k]])
		os.system('rm files/Ocupaciones.csv')
		os.system('mv files/nuevaList.csv files/Ocupaciones.csv')
	if EmpleoFormacionpsico==10:
		with open('files/nuevaList2.csv', 'w', newline='') as csvfileS2:
			
			for i in range(len(data)):
				for palabra in palabras:
					if palabra[0:4].lower() in data[i].lower():
						acomparar=i
						#print(i)

			#c.k(['Se ha abierto file'], 202031723)
			employee_writer2 = csv.writer(csvfileS2) 
			for k in range(1,len(identificador)):
				f7(data[k])
				#c.k([data],202021815)
				#print((['len id', len(identificador),'index', len(index),'data ', len(data2)]))
				##c.k([identificador[k],str(int(resultado)),data[k]],20203181212)
				employee_writer2.writerow([identificador[k],str(int(k)),data[k]])
		os.system('rm files/Profesiones.csv')
		os.system('mv files/nuevaList2.csv files/Profesiones.csv')
	if EmpleoFormacionpsico==1:
		with open('files/nuevaList.csv', 'w', newline='') as csvfileS2:
			#c.k(['Se ha abierto file'], 202031723)
			employee_writer2 = csv.writer(csvfileS2) 
			for k in range(1,len(identificador)):
				f7(data[k])
				#c.k([data],202021815)
				#print((['len id', len(identificador),'index', len(index),'data ', len(data2)]))
				##c.k([identificador[k],str(int(resultado)),data[k]],20203181212)
				employee_writer2.writerow([identificador[k],str(int(k))])
		os.system('rm files/Ocupaciones.csv')
		os.system('mv files/nuevaList.csv files/Psico.csv')
		
	return ([resultados,data,identificador, modificar,acomparar,contadorj])


def comparar(referencia, acomparar,tipo):
	####c.k(['inicion de comparación: Referencia', referencia],14)
	####c.k(['inicion de comparación: busqueda', acomparar],142)
	if tipo==0:
		data=['']
		index=[888]
		identificador=[[]]
		with open(referencia,  encoding='utf-8' ) as csvfile2:
			csv_reader = csv.reader(csvfile2, delimiter=',') #Entrada[]
			LongRef=0
			for row in csv_reader:
				#c.k(['linea 19 ',row],202031814)
				identificador=identificador+[row[0]]			
				index=index+[row[1]]			
				data=data+[row[2]]
				LongRef=LongRef+1 
		#####c.k(['contador de longitud '+str(LongRef)], 22) 

		#####c.k([data, index, identificador, LongRef], 28)#Tengo los tres campos de referencia en tres variables paralelas
		#El de identificador es [[888],[id1],[id2],... [id n]]
		####c.k(['lo que se iba a comparar era: ', acomparar[0], data, identificador], 313106)
		#c.k([acomparar,data,identificador],2020318132)
		[resultado,data2,id2, modificar,y,contadorj]=pareado([str(acomparar)] ,data,identificador,index,100)
	if tipo==1:
	
		data=['']
		index=[888]
		identificador=[[]]
		with open(referencia,  encoding='utf-8' ) as csvfile2:
			csv_reader = csv.reader(csvfile2, delimiter=',') #Entrada[]
			LongRef=0
			for row in csv_reader:
				#c.k(['linea 19 ',row],202031814)
				identificador=identificador+[row[0]]			
				index=index+[row[1]]			
				data=data+[row[2]]
				LongRef=LongRef+1 
		#####c.k(['contador de longitud '+str(LongRef)], 22) 

		#####c.k([data, index, identificador, LongRef], 28)#Tengo los tres campos de referencia en tres variables paralelas
		#El de identificador es [[888],[id1],[id2],... [id n]]
		####c.k(['lo que se iba a comparar era: ', acomparar[0], data, identificador], 313106)
		#c.k([acomparar,data,identificador],2020318132)
		[resultado,data2,id2, modificar,y,contadorj]=pareado([str(acomparar)] ,data,identificador,index,10)
	return [resultado,y]


def f7(seq):#https://www.lawebdelprogramador.com/foros/Python/1526986-Convertir-Cadena-a-Lista-y-Eliminar-elementos-repetidos-sin-perder-el-orden.html

    seen = set()

    seen_add = seen.add

    return [x for x in seq if not (x in seen or seen_add(x))]

