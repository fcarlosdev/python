import re
# import sys
# import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.mairovergara.com/"
print("Accessing the document at "  +URL)
doc = requests.get(URL)
print("Done")
soup = BeautifulSoup(doc.content,"html.parser")

# Pulling out the links of this page that has the text "como-se-diz-em-ingles (meaning "How to say in English" in portuguse)"

#Way One
# print("Searching the wanted value using get and find methods of the links returned by de find_all method")
# print("=================================================================================================")
# allLinks = soup.find_all("a")
# for link in allLinks:
#     if (link.get("href").find("como-se-diz-em-ingles") > -1):
#         print(href)

#Way Two
print("Searching the value \"como-se-diz-em-ingles\" using Regular Expression")
# print("=================================================================================================")
hrefLink = ""
allLinks = soup.find_all(href=re.compile("como-se-diz-em-ingles"))
for link in allLinks:
    if (len(hrefLink) == 0):
        hrefLink += link.get("href")
print ("Returning document at " + hrefLink)
print("Done")
# Navigating and extracting data from the links found above
print("Accessing " + str(hrefLink) + "...")
# print("=================================================================================================")
newDoc = requests.get(hrefLink)
print("Done")
print("Getting number of pages from page-nav element...")
soup = BeautifulSoup(newDoc.content, "html.parser")
# pages = soup.find("div",class_="page-nav")
pages = soup.find("span",class_="pages")
# interval = ""
for page in pages:
    numbers = re.findall(r'\d+',page)
print(numbers)
