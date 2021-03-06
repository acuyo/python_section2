from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.naver.com/sise/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")

top10 = soup.select("#siselist_tab_0 > tr")

i = 1
for i, tr in enumerate(top10):
    if tr.find("a") is not None:
        print(tr.find("a"))
        print(tr.select_one('.tltle'))
        print(i, tr.select_one('.tltle').string)
        i += 1
