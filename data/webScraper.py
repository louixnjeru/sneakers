import requests
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

class Scraper:
    
    def __init__(self, url, filePath):
        self.url = url
        self.filePath = filePath
        if not os.path.isdir(filePath): os.makedirs(filePath)
        
    def isValidUrl(self, url):
        parsedUrl = urlparse(url)
        return bool(parsedUrl.netloc) and bool(parsedUrl.scheme)
    
    def getImageUrls(self):
        soup = bs(requests.get(self.url).content, 'html.parser')
        urls = []
        
        for img in soup.find_all('img'):
            imgUrl = img.attrs.get('src')
            if not imgUrl or imgUrl[-4:] != '.jpg':
                continue
        
            try:
                pos = imgUrl.index('?')
                imgUrl = imgUrl[:pos]
            except ValueError:
                pass
            
            if self.isValidUrl(imgUrl) and not os.path.isfile(os.path.join(self.filePath,imgUrl.split('/')[-1])):
                urls.append(imgUrl)
        
        return urls
    
    def downloadImage(self, imgUrl):
        response = requests.get(imgUrl, stream = True)
        fileName = os.path.join(self.filePath, imgUrl.split('/')[-1])
        
        with open(fileName, 'wb') as f:
            for data in response.iter_content(1024):
                f.write(data)
                
    def scrape(self):
        for img in self.getImageUrls():
            self.downloadImage(img)
        
    
        
    