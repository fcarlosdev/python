import time
import sys
import os
import requests
from bs4 import BeautifulSoup

links = []
count = 1
progress = ""
progress_msg = ""
for page in range(1, 19):
    url = "https://www.mairovergara.com/category/como-se-diz-em-ingles/page/" + str(page) + "/"
    print ("Extracting content from %s " % url)
    progress_msg = "Extracting => ["
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    search_result = soup.find_all('a',{"rel": "bookmark"})
    # search_result = soup.find_all('h3',class_={'entry-title td-module-title'})
    total = len(search_result)

    for item in search_result:
        links.append(item)
        progress = (progress_msg + (u'\u002D' * count) + (' ' * (total - count) + ']') + "("+str(((count*100)/total))+"%)")
        # progress = (progress_msg + (u'\u2584' * count) + (' ' * (total - count) + ']') + "("+str(((count*100)/total))+"%)")
        sys.stdout.write('\r'+progress)
        time.sleep(.02)
        count += 1
    print("\n")
    progress = ""
    count = 1

files = ['extracted_info.txt', 'final_file.txt']

for myfile in files:
    if os.path.isfile(myfile):
        os.remove(myfile)
        print("File %s deleted" % myfile)
    else:
        print("Error: %s file not found" % myfile)

with open('extracted_info.txt', 'w') as f:
    for item in links:
        if (item.text.find('Como se diz')) > -1:
            f.write(str(item) +'\n')
    f.close()


with open('final_file.txt','w') as f:
    file = open('extracted_info.txt','r')
    for line in file:
        link = line[line.index('https'):line.index('rel=')-2]
        sentence = line[line.index('>')+1:line.index('<')-5]
        final_line = link + ' => ' + sentence
        f.write(final_line + '\n')
    file.close()
    f.close()


os.remove(files[0])
