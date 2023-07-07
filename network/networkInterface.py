import torch
import torch.nn as nn
import torch.optim as optim
import os
from neuralNetwork import Net

class runModel():
    
    def __init__(self, learningRate = 1e-5, modelPath = './modelWeights/sneakNet1.pth'):
        self.net = Net()
        self.modelPath = modelPath
        if os.path.isfile(modelPath): self.net.load_state_dict(torch.load(self.modelPath))
        self.criterion = nn.BCELoss()
        self.optimiser = optim.Adam(self.net.parameters(), lr=1e-5)
        
    def trainModel(self, data, label):
        label = torch.tensor([[label]], dtype = torch.float32)
        self.optimiser.zero_grad()
        output = self.net(data)
        loss = self.criterion(output,label)
        loss.backward()
        self.optimiser.step()
        
    def predictLabel(self, data):
        with torch.no_grad():
            output = self.net(data)
            return -output[0][0], output.round() == 1
        
    def saveModel(self):
        torch.save(self.net.state_dict(), self.modelPath)
            
        
