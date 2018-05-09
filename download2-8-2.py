from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os
print(hi)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

base = "https://www.inflearn.com/"
quote = rep.quote_plus("추천-강좌") #유니코드 형태로 변환 시켜줌
url = base + quote

print(url)

res = req.urlopen(url)
savePath = "E:\\acuyo\\python\\inflearn\\resource\\imageDown2\\" #E:/acuyo/python/inflearn/resource/imageDown

try:
    if not (os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 만들기 실패")
        raise #파이썬 에러를 강제적으로 발생

soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("ul.slides")[0]

for i, list in enumerate(img_list, 1):
    with open(savePath+"text_"+str(i)+".txt", 'wt') as f:
        f.write(list.select_one("h4.block_title > a").string)
    fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
    req.urlretrieve(list.select_one("div.block_media > a > img")['src'], fullFileName)

print('다운로드 완료')
