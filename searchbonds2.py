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
        try:
            base=str(table[i]).replace("\t","").replace("\n",'').split('<a href="/bonds/')[1].split('">')

            name=base[1].split("</a>")[0]
            company=base[2].split("</td>")[0]
            isin=base[3].split("</td>")[0]
            maturitydate=base[0].split("Bond-")[1].split("-")[0]
            try:
                issuedate=base[0].split("notes_")[1]

                print(issuedate)
            except:
                issuedate=""
            
            if(issuedate==""):
                try:
                    issuedate=name.split("Notes ")[1].split("(")[0]
                except:
                    issuedate=""
            
            if (issuedate==""):
                store[base[0]]={"name":name,"issuedate":issuedate,"maturitydate":maturitydate,"issuer":company,"isin":isin}
            else:
                store[base[0]]={"name":name,"issuedate":issuedate[:4],"maturitydate":maturitydate,"issuer":company,"isin":isin}
        except:
            print("That's Enough")
            continue

    return store

#print(binsider("Apple"))

