# 练习python从网页抓取数据

from bs4 import BeautifulSoup
import urllib.request
import csv
urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, 'html.parser')

table = soup.find('table', attrs={'class': 'tableSorter2'})
results = table.find_all('tr')
print('Number of results', len(results))
print(results,111)