from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
    <li><a href="http://www.naver.com">네이버</a></li>
    <li><a href="http://www.daum.net">다음</a></li>
    <li><a href="http://www.daum.com">다음</a></li>
    <li><a href="http://www.google.com">구글</a></li>
    <li><a href="http://www.tistory.com">티스토리</a></li>
  </ul>
<body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
print('links', type(links))
a = soup.find_all("a", string="다음")
print('a type -->', type(a))
print('a--> ', a)
b = soup.find("a")
print('b type -->', type(b))
print('b--> ', b)
c = soup.find_all("a", limit=3)  #limit=0 전체를 가져온다.
print('c type -->', type(c))
print('c--> ', c)
d = soup.find_all(string=["네이버", "구글"]) #정규식으로 문자열 찾는걸로 처리
print('d type -->', type(d))
print('d--> ', d)

for a in links:
    print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('href : ', href, ' | text : ', txt)
