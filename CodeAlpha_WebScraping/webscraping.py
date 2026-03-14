import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

df = pd.DataFrame(data)
df.to_csv("quotes_dataset.csv", index=False)

print("CSV file created successfully")
