import requests
from bs4 import BeautifulSoup

def businessi(term):
    store={}

    URL="https://markets.businessinsider.com/bonds/"+term
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    #print(page)
    #print(soup)

    table=soup.find_all(class_="table__tr")
    #print(table)

    scripts=soup.find_all("script")
    #print(scripts[25])

    st=str(scripts[25]).replace("<script>","").replace("</script>","")
    print(st)
    
    graphdata=st.split("detailChartViewmodel")[1].split(";")[0].replace("=","").replace(" ","").replace("null","None").replace("false","False").replace("true","True")

    graph=eval(graphdata)
    #print()
    
    tabledata=[]

    for i in table:
        if('class="table__td">' in str(i)):
            tabledata.append(str(i))

    #print("tabledata",tabledata)

    for i in range(0,len(tabledata)-5):
        base=str(tabledata[i]).replace("\t","").replace("\n",'')
        name=base.split('class="table__td">')[1].split('</td>')[0]
        data=base.split('class="table__td">')[1].split('</td>')[1].split('<td class="table__td text-right">')[1]

        store[name]=data

    #print(store["Issuer"])

    Issue=str(store["Issuer"]).split('">')[1].split("</a>")[0]

    store["Issuer"]=Issue
    store["graph"]=graph["TKData"]

    store["PreviousClose"]=graph["PreviousClose"]

    #print(graph)

    #print(store)
    return store

#print(businessi("apple_incad-notes_201626-Bond-2026-au3cb0237881"))
