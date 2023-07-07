import torch.nn as nn
import torch.nn.functional as F
from torch import flatten

class Net(nn.Module):
    
    def __init__(self):
        super(Net,self).__init__()
        
        self.pool = nn.MaxPool2d(2,2)
        
        self.conv1 = nn.Conv2d(3,6,5,stride=(2,2))
        self.conv2 = nn.Conv2d(6,10,5,stride=(2,2))
        
        self.bn1 = nn.BatchNorm2d(num_features=6)
        self.bn2 = nn.BatchNorm2d(num_features=10)
        self.bn3 = nn.InstanceNorm1d(100)
        
        self.fc1 = nn.Linear(2890,200)
        self.fc2 = nn.Linear(200,100)
        self.fc3 = nn.Linear(100,10)
        self.fc4 = nn.Linear(10,1)
        
    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.bn1(x)
        x = self.pool(F.relu(self.conv2(x)))
        x = self.bn2(x)
        
        x = flatten(x,1)
        
        x = F.tanh(self.fc1(x))
        x = F.tanh(self.fc2(x))
        x = self.bn3(x)
        x = F.tanh(self.fc3(x))
        x = F.sigmoid(self.fc4(x))
        
        return x