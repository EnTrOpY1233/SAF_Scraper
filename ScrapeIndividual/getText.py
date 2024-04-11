import json
from bs4 import BeautifulSoup

def findJSON(soup):
    paragraphs = soup.find('script',type='application/json')
    if (paragraphs!=None):
        data = json.loads(paragraphs.text)
        return data
    else:
        return None

def find_key_in_dict(key, dictionary):
    if isinstance(dictionary,dict)==False or dictionary==None:
        return None
    if key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            return find_key_in_dict(key,dictionary[key])
        return dictionary[key]
    else:
        for value in dictionary.values():
            if isinstance(value, dict):
                result = find_key_in_dict(key, value)
                if result is not None:
                    return result
    return None

#data: JSOn with text, directory: where to replace the new HTML file. title: original title
def JsontoHtml(data,directory,title):
    body=find_key_in_dict('body',data)
    filename=directory+title+".html"
    if (body!=None):
        with open(filename,'w') as file2:
            file2.write(body)
            file2.close()
            print(f"Content in {title}.html has been updated based on application/json. ")
            

    

def findPs(soup):
    paragraphs=soup.findAll('p')
    word=''
    for paragraph in paragraphs:
        word+=paragraph.text.strip()+'\n'
    return word

def findArticles(soup):
    articles=soup.findAll('article')
    word=''
    for article in articles:
        for string in article.stripped_strings:
            word+=string
    return word

def replace(dir,name):
    content=open(dir+name+'.html','r',errors='ignore').read()
    soup=BeautifulSoup(content,'html.parser')
    data=findJSON(soup)
    if (data!=None and data!='' and data!=' ' and data!='   '):
        JsontoHtml(data,dir,name)

def extractText(dir,title):
    replace(dir,title)
    content=open(dir+title+'.html','r',errors='ignore').read()
    soup=BeautifulSoup(content,'html.parser')
    if (findArticles(soup)==''):
        word=findPs(soup)      
    else:
        word=findArticles(soup)
    if (word==''):
        return None
    else:
        return word

if __name__=='__main__':
    dir='ScrapeIndividual/'
    name='title'
    word=extractText(dir,name)
    print(word)




    

