import requests
from bs4 import BeautifulSoup

links = []
for page in range(1,19):
    url = "https://www.mairovergara.com/category/como-se-diz-em-ingles/page/" + str(page) + "/"
    print "Extracting content from the url => %s" % url
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for item in soup.find_all('a'):
        if (item.text.find('Como se diz')) > -1:
            links.append(item)
    # print "\n"

print links

# resp = requests.get("https://www.mairovergara.com/category/como-se-diz-em-ingles/")
# soup = BeautifulSoup(resp.text, "html.parser")

# sentences = soup.find_all('a')

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
