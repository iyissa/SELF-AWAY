import pandas as pd
from bs4 import BeautifulSoup
import requests
page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(page.content, 'lxml')
match  = soup.find_all('a',class_='title')
titles = [title.text for title in match]
print(titles)
match = soup.find_all('p', class_='description')
descriptions = [description.text for description in match]
print(descriptions)
match = soup.find_all('h4',class_='pull-right')
prices = [price.text for price in match]
print(prices)
review_counts = soup.find_all('p', class_='pull-right')
counts = [count.text.strip('reviews') for count in review_counts]
print(counts)
scrape_dictionary = dict(zip(['name', 'description', 'prices', 'review_counts'], [titles, descriptions, prices, counts]))
scrape_dictionary
df = pd.DataFrame(scrape_dictionary)
df.to_csv('Scrape.csv',index=False)