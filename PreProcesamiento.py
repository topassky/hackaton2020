#!/usr/bin/python
# -*- coding: utf8 -*-
#Secuencia principal
import os
import TrozarCSV
import Analizar
import c
import numpy as np
def Organizar(candidatos):
	os.system('rm logs/*')
	desde=0
	hasta=4000
	print('Inicio del clasificador')
	Candi=TrozarCSV.io('files/Candidates.csv','Salidas/Paralelo.csv' , 'Salidas/Lista.csv', desde, hasta, [''])
	[candidatosTrain, matrizTrain, candidatosTest, matrizTest]=Analizar.formato('Salidas/Lista.csv')
	
	Candi2=[]
	for i in Candi:
		if i!= '':
			Candi2+=[i]
 
	ochenta=int(len(Candi)*0.80)
	return Candi2[0:ochenta], matrizTrain, Candi2[ochenta:len(Candi)], matrizTest


candidatosTrain, matrizTrain, candidatosTest, matrizTest=Organizar('files/Candidates.csv')
#print([len(candidatosTrain), len(matrizTrain), len(candidatosTest), len(matrizTest)])
print(len(candidatosTrain),len( matrizTrain),len( candidatosTest),len( matrizTest))

c.k(candidatosTrain,20203202118)
c.k(matrizTrain,20203202118)
c.k(candidatosTest,20203202118)
c.k(matrizTest,20203202118)
