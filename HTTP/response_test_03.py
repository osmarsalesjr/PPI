from bs4 import BeautifulSoup
import requests
import re

url = input("Digite o endereco web:\n>> ")
response = requests.get(url).content
soup = BeautifulSoup(response)
links = soup.findAll('a', attrs={'href': re.compile("^http://")})
for link in links:
    print(link.get('href'))

print(type(links))
