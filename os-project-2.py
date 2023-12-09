import requests
import os
import cloudscraper
import csv
import re
from bs4 import BeautifulSoup

url='https://isorepublic.com/photos/'

cookies={'cookies_1':'_ga_CMYE6TT6N0=GS1.1.1701169125.2.1.1701173906.0.0.0; _ga=GA1.2.1228346308.1701161948; _gid=GA1.2.1102704095.1701161955; '

              }

scrapper=cloudscraper.create_scraper()

request=scrapper.get(url)


with open('behnam01.csv','wb') as b:
    b.write(request.content)


    
print(request)

soup = BeautifulSoup (open("behnam01.csv"), features="html.parser")



list_save=[]
dict_save={}
y_author=[]
y_image=[]


if re.findall('https://isorepublic.com/photo/.+/"',soup.prettify()):
    list_save.append(re.findall('https://isorepublic.com/photo/.+/"',soup.prettify()))
else:
    pass