import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

book_articles = soup.find_all("article", class_="product_pod")

# Create a list to store the data
data = []

for book in book_articles:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    link = url + book.h3.a["href"]
    
    # Append the data to the list
    data.append([title, price, link])

# Specify the filename for the CSV file
filename = "book_data.csv"

# Write the data to the CSV file
with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Price", "Link"])  # Write header row
    writer.writerows(data)  # Write data rows

print("Data exported to", filename)
