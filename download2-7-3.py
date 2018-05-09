from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌") #유니코드 형태로 변환 시켜줌
print(quote)
url = base + quote

res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

recommand = soup.select("ul.slides")[0]

for i, li in enumerate(recommand, 1):
    print(i, li.select_one('h4.block_title > a').string)
