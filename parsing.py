import requests
from bs4 import BeautifulSoup as bs

response = requests.get('https://rutracker.org/forum/viewforum.php?f=635')
html = response.text
soup = bs(html, 'lxml')
for i in soup.find_all('div class="torTopic"'):
        print(i)
