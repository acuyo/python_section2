from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"

print('>>', urljoin(baseUrl, "b.html"))
print('>>', urljoin(baseUrl, "sub/b.html"))
print('>>', urljoin(baseUrl, "../index.html"))
print('>>', urljoin(baseUrl, "../image/img.jpg"))
#urljoin 경로에 대한 치환 작업
