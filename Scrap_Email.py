from bs4 import BeautifulSoup 
import requests
import re
import warnings 
warnings.simplefilter(action='ignore', category=FutureWarning)

import openpyxl

wb = openpyxl.Workbook()





linkToScrap = ['www.test.com']


def returnPageforElement (url):
    listOfDictFinal = []
    regexExp = "[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
    # re.match(regexExp,t.text.lower())

    # for idx, val in enumerate(listOfWords):
    if (soup(text=lambda t: re.match(regexExp,t.text.lower()))): #and (soup(text=lambda t: re.match(regexExp,t.text.lower()) in t.text.lower())) :
        dictUrl = {url : (soup(text=lambda t: re.match(regexExp,t.text.lower()) ))} #in t.text.lower()))}
        listOfDictFinal.append(dictUrl)
        print(listOfDictFinal)
    return listOfDictFinal
    





session = requests.Session()

print('Démarrage du script...')



for val in linkToScrap:
    try:

        soup = BeautifulSoup(session.get(val).content,features="html.parser" , from_encoding="iso-8859-1")

        all_a = soup.find_all('a')

        for i in range (0,len(all_a)):
            
            baliseA = all_a[i]
            if (baliseA.get('href')) and ('http' in baliseA.get('href')) and (baliseA.get('href') not in linkToScrap) and (val in baliseA.get('href')) : #and ('nos-offres' not in baliseA.get('href')) and 'offre-emploi' not in baliseA.get('href')):
                linkToScrap.append(baliseA.get('href'))
                
                
        returnPageforElement(val)
    except:
        print(f'erreur sur la page {val}')
        
print('Fin de script')
        

    





# url = urljoin(base_url, soup.select('div'))
# print(url)

# # parsing the side bar
# soup = BeautifulSoup(session.get(url).content)

# for a in soup.select('div.portlet_content ul li.brieflinkpopper a'):
#     print a.text, urljoin(base_url, a.get('href'))