# Importing the libraries
import numpy as np
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

import PsicoAnalisis
candidatos,matriz = PsicoAnalisis.formatear(('files/Psychometrics.csv'))


nb_users = len(matriz)
nb_candidate = len(matriz[0])

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0, 1))
matrizTrain = sc.fit_transform(matriz)


# Converting the data into Torch tensors
training_set = torch.FloatTensor(matrizTrain)

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
nb_epoch = 2

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

def predict(psytestPath):
    Apruba = np.zeros(nb_users)
    for i in range (len(psytestPath)):
        if (psytestPath[i][0]>= 0.5):
            Apruba[i] += 1 
       
    return Apruba


Permanencia = predict(outputgroup)
print (Permanencia)
    
    
