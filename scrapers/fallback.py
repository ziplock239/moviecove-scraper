from . import fzmovies, h5aoneroom, animepahe

SCRAPERS = [fzmovies, h5aoneroom, animepahe]

def run(method, *args, **kwargs):
    for scraper in SCRAPERS:
        func = getattr(scraper, method, None)
        if callable(func):
            result = func(*args, **kwargs)
            if result:
                return {"source": scraper.__name__, "data": result}
    return {"error": f"No data available for {method}."}
