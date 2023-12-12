import uvicorn
from fastapi import FastAPI
from pyputteer import scrape_website
from searchbonds2 import binsider
from businessinsider import businessi,topchart,topbonds

app = FastAPI()

@app.get("/top")
async def run_scraping():
    result = topchart()
    return result

@app.get("/topbonds")
async def run_scraping():
    result = topbonds()
    return result

@app.get("/search/{inpu}")
async def run_scraping(inpu: str):
    result = await scrape_website(inpu)
    return result

@app.get("/search2/{inpu}")
async def run_scraping(inpu: str):
    result = binsider(inpu)
    return result

@app.get("/search2/details/{inpu}")
async def run_scraping(inpu: str):
    result = businessi(inpu)
    return result

@app.get("/search/")
async def root():
    return {"Message":"Pleaase specify a search query."}
@app.get("/")
async def root():
    return {"Message":"Hello From SSR!"},{"Correct Way":r"https://bonds-terminal.vercel.app/search2/{query}"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=4000, reload=True)
    #asyncio.run(scrape_website('Apple'))
