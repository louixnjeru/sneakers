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

urls = getImageUrls('https://www.sneakerjagers.com/en/releases/out-now/page/100')
print(len(urls))
print(urls)