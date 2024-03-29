import urllib.request
import urllib.parse  # 검색어 자동변환
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요. >> ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)

print()

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

for i in title:
    print(i.attrs['title'])  # 속성을 찾음
    print(i.attrs['href'])
    print()
