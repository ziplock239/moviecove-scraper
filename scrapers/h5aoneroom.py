import requests
from bs4 import BeautifulSoup

BASE_URL = "[h5aoneroom.com](https://h5aoneroom.com)"


def homepage():
    try:
        resp = requests.get(BASE_URL, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for item in soup.select("article")[:10]:
            a = item.select_one("h2 a")
            if a:
                results.append({"title": a.text.strip(), "url": a["href"]})
        return results or None
    except Exception:
        return None


def search(query: str):
    try:
        url = f"{BASE_URL}/?s={query.replace(' ', '+')}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for item in soup.select("article"):
            a = item.select_one("h2 a")
            if a:
                results.append({"title": a.text.strip(), "url": a["href"]})
        return results or None
    except Exception:
        return None


def info(url: str):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.select_one("h1.entry-title")
        description = soup.select_one("div.entry-content")
        return {"title": title.text if title else "", "description": description.text[:300] if description else ""}
    except Exception:
        return None


def download(url: str):
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        links = []
        for a in soup.select("a[href]"):
            href = a["href"]
            if any(x in href.lower() for x in ["download", ".mp4", ".mkv"]):
                links.append({"text": a.text.strip(), "url": href})
        return links or None
    except Exception:
        return None


def subtitle(url: str):
    return None
