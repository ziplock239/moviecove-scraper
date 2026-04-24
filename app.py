from fastapi import FastAPI, Query
from scrapers.fallback import run

app = FastAPI(title="Universal Movie Scraper API", version="2.0")

@app.get("/")
def root():
    return {"message": "Welcome to the Universal Movie Scraper API"}

@app.get("/homepage")
def homepage():
    return run("homepage")

@app.get("/search")
def search(query: str = Query(...)):
    return run("search", query)

@app.get("/info")
def info(url: str = Query(...)):
    return run("info", url)

@app.get("/download")
def download(url: str = Query(...)):
    return run("download", url)

@app.get("/subtitle")
def subtitle(url: str = Query(...)):
    return run("subtitle", url)
