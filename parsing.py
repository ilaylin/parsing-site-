import requests 
from lxml import etree 
import lxml.html 
import csv 
def parse(url): 
    try:
        api = requests.get(url) 
    except:
        return 
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath()        #ВСТАВИТЬ КУСОК html КОДА СО СТРАНИЦЫ САЙТА. 
    with open("text.csv", "w", newline='') as csv_file: 
        write = csv.writer(csv_file)
        for i in range(len(text_original)): #ВСТАВИТЬ ЭЛЕМЕНТ ИЗ html
            write.writerow(text_original[i])#ВСТАВИТЬ ЭЛЕМЕНТ ИЗ html
            

def main(): 
    parse("url") # ВСТАВИТЬ ССЫЛКУ НА СТАРНИЦУ КОТОРУЮ НУЖНО ПРОПАРИСРИТЬ. 
    if __name__ == "__main__": 
        main() 