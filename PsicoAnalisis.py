#!/usr/bin/python
# -*- coding: utf8 -*-
import csv
import c
import Analizar
import datetime, time

def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
    """
    for format in ['%d/%m/%Y']:
        try:
            result = time.strptime(date, format)
            return result
        except:
            pass
    return 0 

def formatear(Archivo):
	with open(Archivo,  encoding='utf-8' ) as csvfile:
		matriz=[]
		candidatos=[]
		duracion=[]
		csv_reader = csv.reader(csvfile, delimiter=',')	
		for roe in csv_reader: 
			contadordecampos=0
			renglon=[]
			bandera=True
			x=False
			if roe[4]== 'Activo' :
				activo='true'
			else:
				activo='false'
			if activo=='true':
				fecha2=datetime.datetime.now()
			else:
				fecha2=datetime.datetime.strptime(roe[2], "%d/%m/%Y")
			fecha1=datetime.datetime.strptime(roe[1], "%d/%m/%Y")
			duracion=int(int((fecha2-fecha1).days)/30)
			#print((roe[0]))
			for campo in roe:	
				x=not(x)
				#print(campo)
				#print(contadordecampos)
				
				
				
				contadordecampos=contadordecampos+1
				if contadordecampos>7 and  contadordecampos<21 :
					if len(campo)>0: 
						
						if x==False: 
							anterior=campo
							
						else :
							sig=[]	
							if 'DP' ==campo:
								sig= [int(anterior),0,0]
							if 'PS'==campo:
								sig= [0,int(anterior),0]
							if 'FP'==campo:
								sig= [0,0,int(anterior)]
							renglon+=sig
					else: 
						bandera=bandera*False
				else:
					if contadordecampos==21 :
						
						sig=[]	
						if 'DP' ==campo:
							sig= [1,0,0]
						if 'PS'==campo:
							sig= [0,1,0]
						if 'FP'==campo:
							sig= [0,0,1]
						renglon+=sig
						renglon=renglon+[duracion]
					else:
						True						

			if bandera== True:
				matriz+=[renglon]
				candidatos+= roe[0]

				
	c.k (matriz, 20203201703)
	ochentac=int(len(candidatos)*0.80)
	ochentam=int(len(matriz)*0.80)
	return (candidatos,matriz)





(formatear('files/Psychometrics.csv'), 202033020)
