import requests 
from bs4 import BeautifulSoup

url = "http://data.fixer.io/api/latest?access_key=d6a438b48a657738727e52bbf4299352"

response = requests.get(url)

veri = response.json() # json verısı aldıgımız ıcın onda donusturme yapıyoruz html yerıne

while True:
    istenilen = input("Tl hesabı için para birimi giriniz (USD,EUR)").upper()

    try:
        t = veri["rates"]["TRY"]
        d = veri["rates"][istenilen]
        print("1 {} {} Türk Lirasina eşittir".format(istenilen,t / d))
        break
    except KeyError:
        print("Yanlış para birimi girdiniz")
            
