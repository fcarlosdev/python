import time
import sys
import requests
from bs4 import BeautifulSoup

links = []
count = 1
progress = ""
progress_msg = ""
for page in range(1,3):
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
        progress = (progress_msg+ "." * count) + "]("+str(((count*100)/total))+"%)"
        sys.stdout.write('\r'+progress)
        time.sleep(.2)
        count += 1
    print "\n"
    progress = ""
    count = 1

print links



# output = []
# for item in sentences:
#   output.append(str(item))

# with open('scrapp.txt', 'w') as f:
#     for item in sentences:
#         if (item.text.find('Como se diz')) > -1:
#             f.write(str(item))


# for x in sentences:
#   # print x.text.encode('utf-8')
#   if (x.text.find('Como se diz')) > -1:
#     print x

# links = soup.find_all('a', class_='page')
#
# print links
