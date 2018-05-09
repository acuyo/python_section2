import sys
import io
import urllib.request as dw


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

print('hi')
print('한글')

imgUrl ="http://cafefiles.naver.net/20100819_215/dgt0406_1282207207754SMdsO_jpg/2010-08-19_17%3B37%3B07_dgt0406.jpg"
htmlUrl = "http://google.com"
savePath1 = "E:/acuyo/python/inflearn/Section2/test2.jpg"
savePath2 = "E:/acuyo/python/inflearn/Section2/index2.html"

# 변수 할당 -> 할당 -> DB 저장
# 데이터 다운 받은 후, 필터 후 저장 시 (메모리에 할당)
f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add, b : binary
saveFile1.write(f)
saveFile1.close()

# with 스스로 close를 내부적으로 실행이 됨
with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)


print("다운로드 완료!!")
