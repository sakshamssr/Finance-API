import asyncio
from pyppeteer import launch

from bs4 import BeautifulSoup
from mdate import convertdate,convertepoch,today,tillmaturity,daystillmaturity

store={}

async def scrape_website(term):
    path=".\chrome-win\chrome.exe"
    browser = await launch(headless=True,executablePath=path,args=['--no-sandbox', '--disable-gpu'])
    page = await browser.newPage()

    try:

        url="https://www.bondsupermart.com/bsm/general-search/"+str(term)
        
        await page.setViewport({'width': 1920, 'height': 1080})
        await page.setExtraHTTPHeaders({'Accept-Encoding': 'gzip, deflate, br'})
        await page.goto(url, {'waitUntil': 'networkidle0'})
        
        content = await page.evaluate("document.querySelector('.ant-table').outerHTML")
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
        await browser.close()

async def intercept_request(req):
    if req.resourceType in ['image', 'stylesheet']:
        await req.abort()
    else:
        await req.continue_()




#asyncio.run(scrape_website("Apple"))
