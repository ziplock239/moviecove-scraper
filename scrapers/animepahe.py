import requests

BASE_URL = "[animepahe.com](https://animepahe.com)"


def homepage():
    try:
        resp = requests.get(f"{BASE_URL}/api?m=airing", timeout=10)
        data = resp.json()
        return [
            {"title": x["anime_title"], "url": f"{BASE_URL}/anime/{x['anime_slug']}"}
            for x in data.get("data", [])[:10]
        ] or None
    except Exception:
        return None


def search(query: str):
    try:
        resp = requests.get(f"{BASE_URL}/api?m=search&q={query}", timeout=10)
        data = resp.json()
        return [
            {"title": x["title"], "url": f"{BASE_URL}/anime/{x['slug']}"}
            for x in data.get("data", [])
        ] or None
    except Exception:
        return None


def info(url: str):
    try:
        slug = url.rstrip("/").split("/")[-1]
        api_url = f"{BASE_URL}/api?m=release&id={slug}&sort=episode_asc"
        data = requests.get(api_url, timeout=10).json()
        return {
            "title": data.get("release", {}).get("title"),
            "episodes": data.get("data"),
            "url": url
        }
    except Exception:
        return None


def download(url: str):
    # AnimePahe uses JS‑generated links; not directly accessible w/o cookies.
    return None


def subtitle(url: str):
    # Subs come inside the video stream, not as .srt files.
    return None
