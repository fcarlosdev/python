# This Python file uses the following encoding: utf-8
import requests
import re
import time
import sys
import os
from bs4 import BeautifulSoup

base_url = "https://www.mairovergara.com/category/como-se-diz-em-ingles/"
# pages = range(1,5)
# filterValues = ["Colocar as Mãos"]

def getHtmlDoc(url):
    print("Connection to url "+ url)
    response = requests.get(url)
    print("Returning Html content...")
    return BeautifulSoup(response.content, "html.parser")

def getTag(tag, withOptions, htmlDoc):
    if (len(withOptions) > 0):
        return htmlDoc.find_all(tag,withOptions)
    else:
        return htmlDoc.find_all(tag)

def showProgress(count, total):
    progress = ("[" + (u'\u002D' * count) + (' ' * (total - count) + ']') + "("+str(((count*100)/total))+"%)")
    sys.stdout.write('\r'+progress)
    time.sleep(.02)


def extractUrlFomLinks(links, withValue):
    filteredLinks = []
    for link in links:
        if (len(withValue) > 0):
            if (withValue in link.getText()):
                lk = str(link)
                filteredLinks.append(lk[lk.index('http' or 'https'):lk.index('rel=')-2])
        else:
            lk = str(link)
            filteredLinks.append(lk[lk.index('http' or 'https'):lk.index('rel=')-2])
    return filteredLinks


sentences = []
for page_number in range(1,2):
    url   = base_url + "page/"+str(page_number)
    links = getTag("a", {"rel": "bookmark"}, getHtmlDoc(url))
    urls  = extractUrlFomLinks(links,"Como se diz")
    for _url in urls:
        doc = getHtmlDoc(_url)
        contents = getTag("p",{},doc)
        count = 1
        total = len(contents)
        for content in contents:
            sentences.append(content.text)
            showProgress(count,total)
            count += 1
        print("\r")
    url = ""

with open('extracted_info.txt', 'w') as f:
    for sentence in sentences:
        f.write(str(sentence.replace(".",".\n").encode('utf-8')) +'\n')
    f.close()
