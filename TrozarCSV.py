#!/usr/bin/python
# -*- coding: utf8 -*-
import c
import csv
import comcop
import Analizar
import Clasif
def io(entrada,out2, lista, desde, hasta, filtros):
	vector=[]	
	with open(entrada,  encoding='utf-8' ) as csvfile:
		c.k(['Se ha abierto el fichero de entrada '+entrada], 8)
		with open(lista, 'w', newline='') as csvfileS: #Salida
			c.k(['Se ha abierto el fichero de salda '+lista], 10)
			employee_writer2 = csv.writer(csvfileS)				#La salida
			csv_reader = csv.reader(csvfile, delimiter=',')			#La entrada
			contador=0			
			HistorialAcade=[]
			HistorialEmp=[]
			Prueba=[]
			bandera=False
			Candi=[]
			for row in csv_reader:
				contador=contador+1
				if  desde< contador and contador<hasta:
					for filtro in filtros:
						#c.k([filtro, comcop.Cadena(row)], 25)
						if filtro in comcop.Cadena(row):
							#bandera=True
							#c.k(['Filtrado',row],25)	
							[HistorialEmp,THisE]=Celdas('"company"',str(row[21]))
							
							[HistorialEdu,THisF]=Celdas('"institute"',str(row[20]))
							[HistorialPsi,THisP]=Celdas('"test_type"',str(row[22]))
							#c.k([THisE,len(HistorialEmp),THisF,len(HistorialEdu),THisP,len(HistorialPsi)],20203182136)
							#c.k(HistorialEmp, 24)
							#c.k(HistorialEdu, 25)
							#c.k(HistorialPsi, 26)	
							identificador=0
							Inventario=0
							for i in range (THisE):	
								if (i)*9+2  < len(HistorialEmp):
									identificador=i*9
									try: 	
										[puesto,y]=Clasif.comparar('files/Ocupaciones.csv', eval(str(HistorialEmp[identificador+1])),0)
									
										#0print(HistorialEmp)
										Inventario=Inventario+1	
										tiempo=Analizar.tiempo(HistorialEmp[identificador+2],HistorialEmp[identificador+3],HistorialEmp[identificador+4])
										#c.k([tiempo, HistorialEmp[identificador+2],HistorialEmp[identificador+3],HistorialEmp[identificador+4]],2020318002)
										#if comcop.moda(puesto)==0:									
										#	True
										if len(puesto)==1:
											#c.k([puesto, y],20203182000)
											moda=puesto[0]
											employee_writer2.writerow([row[0],moda,tiempo])
										else:
											if (comcop.moda(puesto))==0:
												
												#c.k([puesto, y],20203182001)
												for k in puesto:
													#c.k([puesto, y],20203182002)
													employee_writer2.writerow([row[0],k,tiempo])
											else:
												#c.k(['La moda no es cero'+str(puesto), y],20203182003)
												employee_writer2.writerow([row[0],comcop.moda(puesto),tiempo])
									except:
										True
							if (THisE) >0 or (THisE)>0:
								Candi=Candi+[row[0]]
							identificador=0
							Inventario=0
							for i in range (THisF):	
								prom=0
								if (i)*7+2  < len(HistorialEdu):
									identificador=i*7
									[puesto,y]=Clasif.comparar('files/Profesiones.csv', eval(str(HistorialEdu[identificador+1])),1)
									#0print(HistorialEmp)
									Inventario=Inventario+1	
									#tiempo=Analizar.tiempo(HistorialEdu[identificador+2],HistorialEdu[identificador+3],HistorialEmp[identificador+4])
									#c.k([tiempo, HistorialEmp[identificador+2],HistorialEmp[identificador+3],HistorialEmp[identificador+4]],2020318002)
									#if comcop.moda(puesto)==0:									
									#	True
									
									if len(puesto)>0:			
										#c.k([(HistorialEdu[identificador+2],HistorialEdu[identificador+3],HistorialEmp[identificador+4])],20203182100)
										#c.k(['La moda no es cero'+row[0], puesto],202031908)
										employee_writer2.writerow([row[0],puesto[0]+100,y])
									
							
	print('Se ha generado el fichero en la carpeta "Salida"')								
	return Candi

def Celdas(criterio, d):
	#Esta función extrade de un json datos en forto de matriz simple de python, retornandolos en formato
	# ([Empresa1... Empresa n], int(Numero de antecedentes), tipo)=Celda(str(criterio), JSON[])
	#donde cada empresa contiene sus campos pertinentes, ya sea empresa, universidad o pruebas psicotècnicas
	empresa=[]


	Historia=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
	Ninicio=0	
	index=0
	tipo=0
	banderaAlta=True
	fin=0
	while banderaAlta:
		
		if criterio in d[Ninicio:]:
			Tipo=2#1, Académica, 2=Laboral,3. Psicotècica
			inicio=fin+d[Ninicio:].find(criterio)
			fin=fin+d[Ninicio:].find('}')
			Ninicio=fin+1
			#print (Historia)
			#print(str(len(c))+' '+str(len(Historia))+' '+str((index))+' '+str((inicio))+' '+str((fin)) )
			Historia[index]=d[inicio:fin]
			index=index+1
			fin=fin+1					
		else: 
			banderaAlta=False
	counter=0

	for Experiencia in Historia:

		counter=counter+1
		contador=0
		marca=[0,0,0,9,9,9,9,9,9,9,9,9,9,9,8,0,0,0,0,0,0,0,0,0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
		#Para dividir la cadena en pequeños trozos separados por : para relacionar o por , para difereciar
		if ('":"')  in Experiencia:
			banderaOn=True
			contador=1
			marca[contador]=Experiencia.find('":"')	+2

			empresa.append(Experiencia[marca[contador]:Experiencia.find('",')+1])

		else: 
			banderaOn=False
		while banderaOn:
			contador =contador+1
			if Experiencia[marca[contador-1]+1:].find('":')==-1:
				banderaOn=False
			else:
				marca[contador]=marca[contador-1]+(Experiencia[marca[contador-1]+1:]).find('":')+2
				coma=marca[contador]+(Experiencia[marca[contador]+1:]).find(',"')+1	
				empresa.append(Experiencia[marca[contador]+1:coma])
		


		
		#compania= Experiencia[Experiencia.find('"compañia"')+len('"compañia"')+1:Experiencia.find('","')+1]
	#print(empresa)
	if '"test_type"' ==criterio:
		c.k(empresa,20203200841)
	return(empresa, index)





