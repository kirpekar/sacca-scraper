import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
URL = "https://santaclaracycle.com/collections/used-motorcycles-for-sale"

# Headers to mimic a browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Fetch the page
response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all product listings
    motorcycles = soup.find_all("div", class_="grid-product__content")
    
    data = []
    
    for bike in motorcycles:
        title = bike.find("div", class_="grid-product__title").text.strip()
        price = bike.find("div", class_="grid-product__price").text.strip()
        link = "https://santaclaracycle.com" + bike.find("a")["href"]

        data.append({"Title": title, "Price": price, "Link": link})
    
    # Save data to CSV
    df = pd.DataFrame(data)
    df.to_csv("motorcycles.csv", index=False)

    print("Scraping successful! Data saved to motorcycles.csv.")

else:
    print(f"Failed to fetch page. Status Code: {response.status_code}")
