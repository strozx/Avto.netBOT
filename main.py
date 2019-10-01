import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = "https://www.avto.net/Ads/results.asp?znamka=Renault&model=Clio&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=&cenaMin=0&cenaMax=999999&letnikMin=0&letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=&mocMax=&kmMin=0&kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&zaloga=10&arhiv=0&presort=1&tipsort=ASC&stran=1&subSORT=7&subTIPSORT=DESC"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
clios = soup.findAll("div", {"class": "ResultsAd"})
for index, car in clios:
    clio = car.find("div", {"class": "ResultsAdDataTop"})
    specs = clio.find("ul")
    print(specs.content)
    i=0