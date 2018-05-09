from bs4 import BeautifulSoup
import sys
import io
import re #regex 정규표현식

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
<html><body>
    <ul>
    <li><a id="naver" href="http://www.naver.com">네이버</a></li>
    <li><a href="http://www.daum.net">다음</a></li>
    <li><a href="http://www.daum.com">다음</a></li>
    <li><a href="https://www.google.com">구글</a></li>
    <li><a href="https://www.tistory.com">티스토리</a></li>
  </ul>
<body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
test = soup.find('a', string="네이버")
print(test.string)
print(soup.find(id="naver").string)

#li = soup.find_all(href=re.compile(r"^https://"))
li = soup.find_all(href=re.compile(r"da"))
print(li)
for e in li:
    print(e.attrs["href"])
