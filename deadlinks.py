import requests
from bs4 import BeautifulSoup

visited_links = set()  # set to keep track of visited links

def check_links(url, depth=0):
    if depth >= 5:  # maximum depth reached
        return

    if url in visited_links:  # link already visited, skip
        return
    visited_links.add(url)

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return

    if response.status_code == 404:
        print(f"Broken link: {url}")

    soup = BeautifulSoup(response.content, "html.parser")

    for link in soup.find_all("a"):
        href = link.get("href")
        if href and href.startswith("http"):
            check_links(href, depth + 1)



