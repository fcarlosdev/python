# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.mairovergara.com/como-se-diz-pelo-o-que-eu-vi-em-ingles/")
soup = BeautifulSoup(resp.content, "html.parser")

# print(soup.decode('utf-8').encode('cp850','replace').decode('cp850'))
# sentences = soup.find_all('span',style="text-decoration: underline;")
# sentences = soup.find_all('h3', class_={'entry-title td-module-title'})

sentences = soup.find_all('em')

for x in sentences:
  print x.text.encode('utf-8')

  # html = soup.prettify("utf-8")
  #
  # type(html)

  # with open('data.txt', 'w') as f:
  #     f.write(html)
