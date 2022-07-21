import requests
import bs4
import csv
from bs4 import BeautifulSoup

url = 'https://www.census.gov/programs-surveys/popest.html'
r = requests.get(url)
raw_html = r.text
soup = BeautifulSoup(raw_html, 'html.parser')

all_links = soup.find_all('a')

unique_links = set()

for link in all_links:
    link = str(link.get('href'))
    if link.startswith('https'):
        unique_links.add(link)
    elif link.startswith('/'):
        unique_links.add('https://www.census.gov' + link)


#borrrowed code from:
#https://stackoverflow.com/questions/8199041/writing-a-python-list-into-a-single-csv-column
with open('unique_links.csv', 'w') as f:
    cw = csv.writer(f)
    for val in unique_links:
        cw.writerow([val])
f.close()
