import requests
from bs4 import BeautifulSoup

store={}

URL="https://markets.businessinsider.com/bonds/apple_incad-notes_201626-bond-2026-au3cb0237881?miRedirects=1"
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

print(page)
#print(soup)

table=soup.find_all(class_="table__tr")
print(table)

for i in range(0,len(table)):
    base=str(table[i]).replace("\t","").replace("\n",'')
    print(base)

print(store)

