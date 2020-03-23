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
	
	Candi2=[]
	for i in Candi:
		if i!= '':
			Candi2+=[i]
 
	ochenta=int(len(Candi)*0.80)
	return Candi2[0:ochenta], matrizTrain, Candi2[ochenta:len(Candi)], matrizTest


candidatosTrain, matrizTrain, candidatosTest, matrizTest=Organizar('files/Candidates.csv')

nb_users = int(max(len(matrizTrain),len(matrizTest)))
nb_candidate = int(max(len(matrizTrain[0]),len(matrizTest[0])))

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
nb_epoch = 50

for epoch in range(1, nb_epoch + 1):
    train_loss = 0
    s = 0.
    for id_user in range(nb_users):
        input = Variable(training_set[id_user]).unsqueeze(0)
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

def fit(vacantsPath, applicationsPath  ):
    best_candidate = np.zeros(len(applicationsPath))
    for i in range (len(applicationsPath)):
        probabilityFe = chi2_distance(vacantsPath, applicationsPath[i])
        best_candidate[i]+= probabilityFe
    
    position_candidate = []
    for i in range (0, 5):
        indice_min = int(np.where(best_candidate==min(best_candidate))[0])
        
        best_candidate = np.delete(best_candidate, indice_min)
        position_candidate.append(indice_min)
      
    position_candidate.pop(0)
    mejores = []
    for i in position_candidate:
        mejores.append(candidatosTrain[i])
    
    return mejores

best_candidato = fit(outputgroup[-1], outputgroup)
print(best_candidato)
    





