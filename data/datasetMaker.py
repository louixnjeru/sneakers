from torchvision import transforms
from torch.utils.data import Dataset
import os
from PIL import Image

class CustomDataset(Dataset):
    def __init__(self,path):
        self.transform = transforms.Compose([transforms.Resize(300), transforms.ToTensor()])
        self.filePath = path
        self.imageList = os.listdir(self.filePath)
        
    def __len__(self):
        return len(self.imageList)
        
    def __getitem__(self,idx):
        location = os.path.join(self.filePath, self.imageList[idx])
        image = Image.open(location).convert('RGB')
        transformedImage = self.transform(image)
        
        return transformedImage