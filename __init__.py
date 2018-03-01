import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.feedwm.org/findfood/').content
soup = BeautifulSoup(html, 'html.parser')

