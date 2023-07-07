import requests
import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
from tqdm import tqdm

def isValid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def getImageUrls(url):
    soup = bs(requests.get(url).content, 'html.parser')
    urls = []
    
    for img in tqdm(soup.find_all('img'),'Extracting Images'):
        imgUrl = img.attrs.get('src')
        if not imgUrl or imgUrl[-4:] != '.jpg':
            continue
        
        try:
            pos = imgUrl.index('?')
            imgUrl = imgUrl[:pos]
        except ValueError:
            pass
        
        if isValid(imgUrl): urls.append(imgUrl)
        
    return urls

def downloadImage(url,filePath):
    if not os.path.isdir(filePath): os.makedirs(filePath)
    
    response = requests.get(url,stream=True)
    fileSize = int(response.headers.get("Content-Length", 0))
    fileName = os.path.join(filePath, url.split('/')[-1])
    progress = tqdm(response.iter_content(1024), f"Downloading {fileName}", total=fileSize, unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(fileName, 'wb') as f:
        for data in progress.iterable:
            f.write(data)
            progress.update(len(data))
            
def scraper(url,filePath):
    urls = getImageUrls(url)
    for img in urls: downloadImage(img, filePath)

'''urls = getImageUrls('https://www.sneakerjagers.com/en/releases/out-now/page/100')
print(len(urls))
print(urls)'''


for i in range(136,151):
    print(i)
    scraper(f'https://www.sneakerjagers.com/en/releases/out-now/page/{i}','data/trainData')