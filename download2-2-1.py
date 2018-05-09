import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('hi')
print('한글')

imgUrl ="http://cafefiles.naver.net/20100819_215/dgt0406_1282207207754SMdsO_jpg/2010-08-19_17%3B37%3B07_dgt0406.jpg"
htmlUrl = "http://google.com"
savePath1 = "E:/acuyo/python/inflearn/Section2/test1.jpg"
savePath2 = "E:/acuyo/python/inflearn/Section2/index.html"

# 저장 -> open('r') -> 변수에  할당 -> 파싱 -> DB 저장
# 한번에 이미지, 파일을 저장하기 위해서 사용
dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)


print("다운로드 완료!!")
