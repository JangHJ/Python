import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/content/58396566'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

script = soup.find("script", id="__NEXT_DATA__")
json_data = json.loads(script.contents[0])

title = json_data["props"]["pageProps"]["metaInfo"]["ogTitle"]
# print(title)

print(soup.prettify())

# view_count = soup.find("strong", {"class": "css-1797phs-Text"}).text
# print(view_count)