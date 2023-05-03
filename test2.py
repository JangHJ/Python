import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver

# webdriver 설정
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# webdriver 객체 생성
driver = webdriver.Chrome(options=options)

# 페이지 접근
url = "https://page.kakao.com/content/58396566"
response = requests.get(url)
driver.get(url)

# BeautifulSoup으로 html 파싱
soup1 = BeautifulSoup(response.content, 'html.parser') # html
soup2 = BeautifulSoup(driver.page_source, "html.parser")  # web driver

# json data 가져오기
script = soup1.find("script", id="__NEXT_DATA__")
json_data = json.loads(script.contents[0])

# 제목 가져오기
title = json_data["props"]["pageProps"]["metaInfo"]["ogTitle"]

# 조회수 가져오기
view_count = soup2.select_one('div.flex.items-center.justify-center.mt-16pxr.text-el-60.all-child\:font-small2 span.css-1797ph-Text').text

# 결과 출력
print("제목:", title)
print("조회수:", view_count)

# webdriver 종료
driver.quit()