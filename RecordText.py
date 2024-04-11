import json
from ScrapeIndividual import getText,RecordHTML


#record main text
with open('Data/CompanyCapacityLinks.json', 'r') as file:
    data = json.load(file)
    file.close()


for company in data['companies']:
    for result in company["searchResults"]:
        url=result['Link']
        articleTile=result['Title']
        directory='Data/HtmlList/'
        recordSuccess=RecordHTML.record(url,articleTile,directory)
        result['Text body']=''
        if (recordSuccess):
            result['Allow scrape']=True
            result['HTMLSource']=directory+articleTile+'.html' #record location of the html source stored in the computer
            txt=getText.extractText(directory,articleTile)
            result['Text body']=txt
        else:
            result['Allow scrape']=False
            result['HTMLSource']=None
            result['Text body']=None

file1=open('Data/CompanyCapacityLinks.json','w')
json.dump(data,file1,indent=4)
file1.close()
print('All main texts are recorded in Data/CompanyCapacityLinks2.json')

