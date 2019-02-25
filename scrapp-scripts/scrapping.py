import time
import sys
import requests
from bs4 import BeautifulSoup

links = []
count = 1
progress = ""
progress_msg = ""
for page in range(1, 18):
    url = "https://www.mairovergara.com/category/como-se-diz-em-ingles/page/" + str(page) + "/"
    print "Extracting content from %s " % url
    progress_msg = "Extracting => ["
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    search_result = soup.find_all('a')
    total = len(search_result)

    for item in search_result:
        if (item.text.find('Como se diz')) > -1:
            links.append(item)
        progress = (progress_msg + ('.' * count) + (' ' * (total - count) + ']') + "("+str(((count*100)/total))+"%)")
        sys.stdout.write('\r'+progress)
        time.sleep(.05)
        count += 1
    print "\n"
    progress = ""
    count = 1

# print links


with open('extracted_info.txt', 'w') as f:
    for item in links:
        if (item.text.find('Como se diz')) > -1:
            f.write(str(item))
    f.close()
