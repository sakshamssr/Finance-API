import requests
from bs4 import BeautifulSoup

def businessi(term):
    store={}

    URL="https://markets.businessinsider.com/bonds/"+term
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    table=soup.find_all(class_="table__tr")
    scripts=soup.find_all("script")

    st=[]
    rating=soup.find(class_="moodys-rating__rating")

    rating=rating.text

    for i in range(0,len(scripts)):
        st.append(str(scripts[i]))
        
    tabledata=[]

    for i in table:
        if('class="table__td">' in str(i)):
            tabledata.append(str(i))

    for i in range(0,len(tabledata)-5):
        base=str(tabledata[i]).replace("\t","").replace("\n",'')
        name=base.split('class="table__td">')[1].split('</td>')[0]
        data=base.split('class="table__td">')[1].split('</td>')[1].split('<td class="table__td text-right">')[1]

        store[name]=data

    Issue=str(store["Issuer"]).split('">')[1].split("</a>")[0]
    store["Issuer"]=Issue
    
    try:
        store["rating"]=100-int(rating)
        if (int(rating)<33):
            store["color"]="green"
        elif(int(rating)>33 and int(rating)<66):
            store["color"]="orange"
        else:
            store["color"]="red"
    except:
        store["rating"]="-"
    store["graphdata"]=st[26].replace("<script>","").replace("</script>","").replace("=","").replace(" ","").replace("null","None").replace("false","False").replace("true","True").replace("\n","").replace("\t","").replace('/','')

    return store

def topchart():
    store={}

    URL="https://markets.businessinsider.com/ajax/finanzen/api/commodities?urls=gold-price,oil-price"
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    data = page.json()

    return data

def topbonds():
    store=[]

    URL="https://markets.businessinsider.com/bonds"
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    table=soup.find_all(class_="table__tr")
    topb=[]

    for i in table:
        if ("/bonds" in str(i)):
            topb.append(str(i).replace("\n","").replace("\t","").split("/bonds/"))

    for i in range(0,len(topb)):
        linkisin=topb[i][2].split('<td class="table__td text-right">')[0].split('">')
        name=topb[i][1].split('<td class="table__td text-right">')[0].split('">')[1].split("</a>")[0]

        permod=topb[i][2].split('<td class="table__td text-right">')

        link=linkisin[0]
        isin=linkisin[1].split("</a>")[0]

        d=[]

        for k in range(1,len(permod)):
            d.append(permod[k].split("</td>")[0])

        di={"name":name,"isin":isin,"yield":d[0],"moodys":d[1],"date":d[2],"link":link,}

        store.append(di)

    return store

#print(businessi("apple_incad-notes_201626-Bond-2026-au3cb0237881"))

#topbonds()
