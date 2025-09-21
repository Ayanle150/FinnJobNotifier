# filepath: /Users/ayanlemohamed/Documents/Jobbvarsling System/finn_scrapper.py

import requests
from bs4 import BeautifulSoup
from config import KEYWORDS
from send_email import send_job_email

def finn_job_search():
    """
    Skraper finn.no etter stillinger som matcher søkeordene mine.
    Sender e-post når jeg finner relevante annonser.
    """

    url = "https://www.finn.no/job/search?q=student+data"

    try:
        # Jeg legger på en User-Agent så det ser ut som en vanlig nettleser
        headers = {"User-Agent": "Mozilla/5.0 (jobbvarsler)"}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Klarte ikke å hente data fra FINN: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Henter alle annonser
    articles = soup.find_all("article", class_="sf-search-ad")

    relevante_stillinger = []

    for article in articles:
        link_tag = article.find("a", class_="sf-search-ad-link")
        if not link_tag:
            continue

        title = link_tag.get_text().strip()
        link = link_tag["href"]

        # Sjekker om stillingstittelen inneholder et av søkeordene
        if any(keyword.lower() in title.lower() for keyword in KEYWORDS):
            print(f"Fant relevant stilling: {title}")
            relevante_stillinger.append({"tittel": title, "lenke": link, "kilde": "Finn.no"})

    # Når du finner en relevant stilling:
    for jobb in relevante_stillinger:
        send_job_email(jobb['tittel'], jobb['lenke'], jobb['kilde'])


if __name__ == "__main__":
    finn_job_search()
