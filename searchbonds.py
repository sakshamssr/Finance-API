import requests
from datetime import datetime
from bs4 import BeautifulSoup
from mdate import convertdate,convertepoch,today,tillmaturity,daystillmaturity

def scrape_website(term):
    try:
        store={}

        url="https://bondsterminal.onrender.com/scrape?term="+str(term)
        page=requests.get(url)

        content=page.content
        soup = BeautifulSoup(content, "html.parser")

        #print(soup)

        name=soup.find_all(class_="link-primary")
        sector=soup.find_all(class_="text-black-7 font-semibold ant-table-cell")

        #print(name)

        #print(sector)

        for i in range(0,len(name)):
            isin=str(name[i]).split('href="/bsm/bond-factsheet/')[1].split('"><strong')[0]
            #sectorname=sector[i]
            #print(sectorname.text)
            #print(isin)
            bondname=str(name[i]).split('="">')[1].split('</strong>')[0]
            n=str(sector[0].text)
            cr=str(sector[1].text)
            md=str(sector[2].text)
            ap=str(sector[3].text)
            ytm=str(sector[4].text)

            epoch=convertepoch(convertdate(md))
            tillm=tillmaturity(epoch,today())

            try:
                for j in range(0,5):
                    sector.pop(0)
            except:
                print("List Length:",len(sector))
            
            store[isin]={"bondname":bondname,"sector":n,"couponrate":cr,"maturitydate":md,"maturitydateepoch":epoch,"tillmaturityepoch":tillm,"daystillmaturity":daystillmaturity(tillm),"askprice":ap,"ytm":ytm}

        for i in range(0,len(sector)):
            sectorname=sector[i]

        print(store)
        return store

    finally:
        #time.sleep(7)
        print("Done!")

#scrape_website("Apple")
