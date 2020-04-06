#!/usr/bin/python
# -*- coding: utf8 -*-

# Importing the libraries
import numpy as np
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
import os
import TrozarCSV
import Analizar


def Organizar(candidatos):
	os.system('rm logs/*')
	desde=0
	hasta=5000000
	print('Inicio del clasificador')
	TrozarCSV.io('files/Candidates.csv','Salidas/Paralelo.csv' , 'Salidas/Lista.csv', desde, hasta, [''])
	[candidatosTrain, matrizTrain, candidatosTest, matrizTest]=Analizar.formato('Salidas/Lista.csv')

	return candidatosTrain, matrizTrain, candidatosTest, matrizTest


candidatosTrain, matrizTrain, candidatosTest, matrizTest=Organizar('files/Candidates.csv')

candidatosTrain = np.asarray(candidatosTrain )
matrizTrain = np.asarray(matrizTrain)
nb_users = len(matrizTrain)
nb_candidate = len(matrizTrain[0])

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
matrizTrain = sc.fit_transform(matrizTrain)
matrizTest = sc.fit_transform(matrizTest)

# Converting the data into Torch tensors
training_set = torch.FloatTensor(matrizTrain)
test_set = torch.FloatTensor(matrizTest)

# Creating the architecture of the Neural Network
class SAE(nn.Module):
    def __init__(self, ):
        super(SAE, self).__init__()
        self.fc1 = nn.Linear(nb_candidate, 10)
        self.fc2 = nn.Linear(10, 5)
        self.fc3 = nn.Linear(5, 10)
        self.fc4 = nn.Linear(10, nb_candidate)
        self.activation = nn.Sigmoid()
    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc3(x))
        x = self.fc4(x)
        return x
sae = SAE()

criterion = nn.MSELoss()
optimizer = optim.RMSprop(sae.parameters(), lr = 0.01, weight_decay = 0.5)

# Training the SAE
nb_epoch = 200

for epoch in range(1, nb_epoch + 1):
    train_loss = 0
    s = 0.
    for id_user in range(nb_users):
        input = Variable(training_set[id_user].T).unsqueeze(0)
        target = input.clone()
        if torch.sum(target.data > 0) > 0:
            output = sae(input)
            target.require_grad = False
            output[target == 0] = 0
            loss = criterion(output, target)
            mean_corrector = nb_candidate/float(torch.sum(target.data > 0) + 1e-10)
            loss.backward()
            train_loss += np.sqrt(loss.data*mean_corrector)
            s += 1.
            optimizer.step()
    print('train loss: '+str(train_loss/s))


## Testing the SAE
test_loss = 0
s = 0.
for id_user in range(nb_candidate):
    input = Variable(training_set[id_user])
    target = Variable(test_set[id_user])
    if torch.sum(target.data > 0) > 0:
        output = sae(input)
        target.require_grad = False
        output[target == 0] = 0
        loss = criterion(output, target)
        mean_corrector = nb_candidate/float(torch.sum(target.data > 0) + 1e-10)
        test_loss += np.sqrt(loss.data*mean_corrector)
        s += 1.
    print('test loss: '+str(test_loss/s))


    
outputgroup = []
for userd_id in range (nb_users):
    user_input = Variable(training_set[userd_id])
    ouput = sae(user_input)
    output = ouput.data.numpy()
    n_max = max(output)
    outputScaling = np.zeros(len(output))
    for i in range (0, len(output)):
        outputScaling[i] = outputScaling[i] + output[i]*(1/n_max)
        
    outputgroup.append(outputScaling)
    
#print(outputgroup)

def chi2_distance(featuresA, featuresB, eps = 1e-10):
    # compute the chi-squared distance
	d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
	for (a, b) in zip(featuresA, featuresB)])
	# return the chi-squared distance
	return d

def logtolin(matriz):
	j=0
	matriz2=[]
	matriz3=matriz
	NoCeros=not(0 in matriz)
	while not(NoCeros):
		matriz2=[]
		for i in matriz3:
			matriz2.append(i)
			j+=1
		j=0
		matriz2[matriz2.index(min(matriz2))]=78
		NoCeros=not(0 in matriz2)
		matriz3=matriz2
	segundomenor=min(matriz2)
	#print(f'Segundomenor {segundomenor}')
	for i in matriz:
		matriz[j]=i+segundomenor
		j=j+1

	#print(matriz)
	minimus=segundomenor
	maximus=max(matriz)
	k= 1/ (np.log(minimus)-np.log(maximus))
	j=0
	lineal=matriz
	#print(k)
	for i in matriz:
		#print(i)
		lineal[j]=k*(np.log(minimus)-np.log(i))
		j+=1
	return lineal 



def fit(vacantsPath, applicationsPath  ):
    best_candidate = np.zeros(len(applicationsPath))
    for i in range (len(applicationsPath)):
        probabilityFe = chi2_distance(vacantsPath, applicationsPath[i])
        best_candidate[i]+= probabilityFe

    
    return best_candidate

best_candidate = fit(outputgroup[-1], outputgroup)
position_candidate = []
for i in range (0, 5):
    indice_min = int(np.where(best_candidate==min(best_candidate))[0][0])
    best_candidate = np.delete(best_candidate, indice_min)
    position_candidate.append(indice_min)

position_candidate.pop(0)          
mejores_candidatos = []
for i in position_candidate:
    mejores_candidatos.append(candidatosTrain[i])

best_candidate = fit(outputgroup[-1], outputgroup)
best_candidatonorm = logtolin(best_candidate)

puntuacion = []
for i in position_candidate:
    puntuacion.append(best_candidatonorm[i])

putuacion_100 = []    
for i in puntuacion:
    n = (1-i)
    putuacion_100.append(n)

aprueba = []
for i in putuacion_100:
    if (i == max(putuacion_100)):
        aprueba.append(1)
    else:
        aprueba.append(0)
        
import csv
total = [[int(mejores_candidatos[i]),float(putuacion_100[i]) , int(aprueba[i])] for i in range(len(position_candidate))]

myFile = open('Salidas/Salida_Reto1.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(total)
     
print("Writing complete")
    
    
    
    
    
    



    
    
    
    
    
    
    
    







