import uvicorn
from fastapi import FastAPI

from searchbonds import scrape_website

app = FastAPI()

@app.get("/search/{inpu}")
async def run_scraping(inpu: str):
    result = await scrape_website(inpu)
    return result

@app.get("/search/")
async def root():
    return {"Message":"Pleaase specify a search query."}
@app.get("/")
async def root():
    return {"Message":"Hello From SSR!"},{"Correct Way":r"http://127.0.0.1:8000/search/{query}"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
    #asyncio.run(scrape_website('Apple'))
