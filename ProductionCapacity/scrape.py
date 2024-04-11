import json
import sys

sys.path.insert(0, 'E://Programming//Web scaper//SAF_Scraper') 

from ScrapeIndividual import getText 
from ScrapeIndividual import RecordHTML

if __name__=='__main__':
    with open('ProductionCapacity/Info.json','r') as file:
        datas=json.load(file)
        print(datas)
        file.close()

    for result in datas:
        url=result['URL']
        articleTile=result['Company']
        directory='ProductionCapacity/HtmlList/'
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
        
    with open('ProductionCapacity/Info.json','w') as file:
        json.dump(datas,file,indent=3)
        file.close()

