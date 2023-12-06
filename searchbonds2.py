import requests
from bs4 import BeautifulSoup

def binsider(term):
    store={}

    URL="https://markets.businessinsider.com/searchresults?_type=anleihen&_search="+term
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    #print(page)
    #print(soup)

    table=soup.find_all(class_="table__tr")
    #print(table)

    for i in range(1,len(table)):
        base=str(table[i]).replace("\t","").replace("\n",'').split('<a href="/bonds/')[1].split('">')

        name=base[1].split("</a>")[0]
        company=base[2].split("</td>")[0]
        isin=base[3].split("</td>")[0]
        maturitydate=base.split("Base-")[1].split("-")[0]

        store[base[0]]={"name":name,"maturitydate":maturitydate,"issuer":company,"isin":isin}

    return store

#print(binsider("Apple"))

