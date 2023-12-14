import os
import cloudscraper
import csv
import re
from bs4 import BeautifulSoup

#BARAY SAFAHAT url=f'https://isorepublic.com/photos/page/{a}/'    ke a shomare safhe ast
url='https://isorepublic.com/photos/'
#  use cookies : cookies={'cookies_1':'_ga_CMYE6TT6N0=GS1.1.1701169125.2.1.1701173906.0.0.0; _ga=GA1.2.1228346308.1701161948; _gid=GA1.2.1102704095.1701161955; ' }

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
y_category=[]

if re.findall('https://isorepublic.com/photo/.+/"',soup.prettify()):
    list_save.append(re.findall('https://isorepublic.com/photo/.+/"',soup.prettify()))

list_save_del_reaprat=set(list_save[0])
list_save=list(list_save_del_reaprat)
#print(list_save)
#-------ok ta inja miad adrres har page ro behemon mideh   az inja be bad page photo ekhtwsasi hast

for item in range(len(list_save)):
    request_image_page=scrapper.get(list_save[item])
    with open('behnam00.csv','wb') as q:
        q.write(request_image_page.content)
            
    soup1 = BeautifulSoup (open("behnam00.csv"), features="html.parser")
                
    if re.findall('href="https://isorepublic.com/wp-content/uploads.+.jpg',soup1.prettify()):
        y_image.append(re.findall('href="https://isorepublic.com/wp-content/uploads.+.jpg',soup1.prettify()))
        y_author.append(re.findall('https://isorepublic.com/media-author.+" ',soup1.prettify()))
        y_category.append(re.findall('href="https://isorepublic.com/media-category.+/"',soup1.prettify()))
        
        dict_save[y_author[item][0]]=y_image[item][0]

#-------------------------in ghesmat bad moshakhasat ti file save mikona
    
header=['category','author','tag','url']
for item1 in range(len(list_save)):
    data=[y_category[item1][0][45:-3],y_author[item1][0][37:-2],y_author[item1][0][37:-2],y_image[item1][0][6:]]
    with open('inform.csv', 'a', encoding='UTF8') as f5:
        writer = csv.writer(f5)
        writer.writerow(header)
        writer.writerow(data)
#print(y_category)
# az inja be bad dige sakht poshe v download photo ast

list_check_not_reapeat_folder=[]
for d1,d2 in dict_save.items():
    image_check = str(d1[37:-2])
    if image_check not in list_check_not_reapeat_folder:
        os.makedirs(str(d1[37:-2]))
    request3=scrapper.get(d2[6:])
    with open(f"{str(d1[37:-2])}/new.jpg",'wb') as save5:
        save5.write(request3.content)
    list_check_not_reapeat_folder.append(str(d1[37:-2]))
  
