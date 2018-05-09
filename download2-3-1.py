import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.encar.com"

mem = req.urlopen(url)

print(type(mem))
print(type({}))
print(type([]))
print(type(()))

print("geturl", mem.geturl())
print("status", mem.status) #200(정상), 404(요청페이지 없음), 403(리젝트=내부방 요청), 500(서버 컴파일 오류)
print("headers", mem.getheaders())

print("info", mem.info())
print("code", mem.getcode())
print("read", mem.read(50)) #해당 숫자 만큼 가져 온다. 공백이면 전체
print("read", mem.read(50).decode("utf-8")) #eue-kr

print(urlparse("http://www.encar.com?test=test"))
