from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = rep.quote_plus("아깽이")
url = base + quote

print(url)

res = req.urlopen(url)
savePath = "E:\\acuyo\\python\\inflearn\\resource\\imageDown\\" #E:/acuyo/python/inflearn/resource/imageDown

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise #파이썬 에러를 강제적으로 발생

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, list in enumerate(img_list, 1):
    print(list['data-source'])
    fullFileName = os.path.join(savePath, savePath + str(i) + '.jpg')
    print(fullFileName)
    req.urlretrieve(list["data-source"], fullFileName)


print('다운로드 완료')
