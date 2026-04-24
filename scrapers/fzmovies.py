import requests
from bs4 import BeautifulSoup

BASE_URL = "[fzmovies.net](https://fzmovies.net)"


def homepage():
    """Fetch homepage highlights (featured movies)."""
    try:
        resp = requests.get(BASE_URL, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        items = []
        for movie in soup.select("a[href*='movie.php']")[:10]:
            title = movie.get_text(strip=True)
            link = movie["href"]
            if title:
                items.append({"title": title, "url": BASE_URL + "/" + link})
        return items or None
    except Exception:
        return None


def search(query: str):
    """Search movies by name."""
    try:
        url = f"{BASE_URL}/search.php?catID=1&searchname={query}"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for movie_div in soup.select("div.movie_overlay"):
            title = movie_div.select_one("b")
            if not title:
                continue
            title = title.text.strip()
            link = movie_div.find("a")["href"]
            results.append({"title": title, "url": BASE_URL + "/" + link})
        return results or None
    except Exception:
        return None


def info(url: str):
    """Extract movie info (title, image, description, download page)."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.select_one("h1, h2, h3")
        description = soup.get_text(" ", strip=True)[:400]
        return {"title": title.text.strip() if title else None,
                "description": description,
                "download_page": url}
    except Exception:
        return None


def download(url: str):
    """Attempt to extract download links."""
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "download" in href.lower() or href.endswith((".mp4", ".mkv")):
                links.append({"quality": a.text.strip(), "url": href})
        return links or None
    except Exception:
        return None


def subtitle(url: str):
    """FzMovies doesn’t normally provide subtitles; placeholder."""
    return None
