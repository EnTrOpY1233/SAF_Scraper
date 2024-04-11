import requests
import json
import csv,re

companies=[]
companyInfos=[]
with open('Data/Company.csv','r') as companyfile:
    csv_reader=(csv.DictReader(companyfile))
    for line in csv_reader:
        companies.append(line['name'])


safRelated=[' sustainable aviation fuel ',' saf ',' biofuel ',' renewable aviation fuel ',' alternative aviation fuel ']

API_KEY=open("SearchAPIKey.txt","r").read()
SEARCH_ENGINE_ID=open("SearchEngineKey.txt","r").read()
info='production capacity'
for company in companies:
    #search for production capacity, only first related key word due to limit of chatgpt
    query = company+safRelated[0]+info
    para={
        'key':API_KEY,
        'q':query,
        'cx':SEARCH_ENGINE_ID
    }
    url="https://www.googleapis.com/customsearch/v1"
    data = requests.get(url,params=para).json()
    results=[]
    for item in data['items'][0:5]:
        pattern = r'[^a-zA-Z0-9\s]'
        cleaned_text = re.sub(pattern, '', item['title'].replace('.',''))
        newDict={
            #handle special case!!!
            'Title':cleaned_text,
            'Link':item['link'],
            'Intro':item['snippet']
        }
        results.append(newDict)
    companyInfo={
        'name':company,
        'searchResults':results
    }
    companyInfos.append(companyInfo)

dictionary={
    'companies':companyInfos
}

#open a json file to store possible links to scrape for one company's capacity

file=open('Data/CompanyCapacityLinks.json','w')
json.dump(dictionary,file,indent=6)
file.close()
print(f"Links about {info} for each company has been recorded in Data/CompanyCapacityLinks.json")




