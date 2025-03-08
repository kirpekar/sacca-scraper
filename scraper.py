import requests
from bs4 import BeautifulSoup

URL = "https://example.com"  # Change to the website you want to scrape
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.text if soup.title else "No title found"
    
    with open("output.txt", "w") as f:
        f.write(f"Page Title: {title}\n")

    print("Scraping successful. Data saved to output.txt.")
else:
    print("Failed to fetch page.")
