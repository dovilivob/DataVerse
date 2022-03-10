import requests as req
from urllib import request as ureq
from bs4 import BeautifulSoup as bs4
import json


def getSubStr(startCode, endCode, html):
    content = str(html)
    start = content.find(startCode)
    string = content[start:-1]
    end = string.find(endCode)
    string = string[0:end]
    return string


imgNum = input("input: ")
num = 4 - len(imgNum)

imgStr = "0" * num + str(imgNum) + ".png"

url = "https://b10862032.newmedia.tw/sbi/" + imgStr

print(url)

google_url = "https://www.google.com/searchbyimage?image_url=" + url

# https://www.google.com/searchbyimage?image_url=https://b10862032.newmedia.tw/sbi/0001.png


request = ureq.Request(
    google_url,
    headers={
        "content-type": "text/html; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
    },
    method="GET",
)
with ureq.urlopen(request) as response:
    html = response.read().decode("utf-8")

soupHtml = bs4(html, 'html.parser')
newUrl = soupHtml.find('title-with-lhs-icon')
newUrl = 'https://www.google.com' + \
    getSubStr('/search?', '">', newUrl).replace('">', '').replace("amp;", "")
print(newUrl)

request = ureq.Request(
    newUrl,
    headers={
        "content-type": "text/html; charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
        "cookie": "OTZ=6277734_24_24__24_; NID=511=SyED1MloqIhwx0mkj0XyF2uIZnxxoIsxL2RB7bgfGY9dR55HMar9vsd0pQQfhQ5Ke3IM0HHLz42nbh9jAwhkg8BtyX2X3SA3yHjEsQd-kPJLYXppYT_VumC3A6OotrkJt2HC5__SaDq7E_90CX-lfOaTYtFx7GetskfZc0fUj30; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjM4OTY4Nzg3ODcyMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDI1MTU2MDYxMAogIGxvbmdpdHVkZV9lNzogMTIxNDYzMTQyMAp9CnJhZGl1czogNjY5NjAKcHJvdmVuYW5jZTogNgo=; OGPC=19010599-1:; OGP=-19010599:; 1P_JAR=2021-12-08-13",
    },
    method="GET",
)
with ureq.urlopen(request) as response:
    html = response.read().decode("utf-8")

soupHtml = bs4(html, 'html.parser')

div = soupHtml.find('div', {"class": "bRMDJf islir"})
print(div)

print(soupHtml.find_all('div', {'class': 'gb_Cd'}))
with open('record.html', 'w', encoding='utf-8') as file:
    # file.write(str(soupHtml.find_all('div', {'data-cb': '9'})))
    # file.write(str(soupHtml.find_all('div', {'data-hveid': 'CAEQjAE'})))
    file.write(soupHtml.prettify())


# data = soupHtml.find_all('div', {'data-hveid': 'CAEQjAE'})
# imgrc = getSubStr('data-id', 'data-oh', str(data)).replace('data-id', '')

# string = getSubStr("bRMDJf islir", '" data-deferred', html)
# print(string)

# https://www.google.com/search?tbs=simg:CAES-QEJE_1sq-9edNeoa7QELELCMpwgaOgo4CAQSFMQY3gv2GIALoT-sKfw--yCIEcQCGhqoLPa00NYLVW5vCIzJAJn8aEu_1P6vZnRt4LyAFMAQMCxCOrv4IGgoKCAgBEgSyZfu7DAsQne3BCRqNAQodCglsYXZhIGFyZWHapYj2AwwKCi9tLzBjbm1kNHIKGQoHdm9sY2Fub9qliPYDCgoIL20vMDdfOV8KGgoIbW91bnRhaW7apYj2AwoKCC9tLzA5ZF9yChQKA2FydNqliPYDCQoHL20vMGpqdwofCgxpbGx1c3RyYXRpb27apYj2AwsKCS9tLzAxa3I4Zgw&q=lava+area&tbm=isch&sa=X&ved=2ahUKEwj0joCE1vr0AhWLMpQKHe7cDlkQjJkEegQIHhAC
# https://www.google.com/search?tbs=simg:CAES-QEJE_1sq-9edNeoa7QELELCMpwgaOgo4CAQSFMQY3gv2GIALoT-sKfw--yCIEcQCGhqoLPa00NYLVW5vCIzJAJn8aEu_1P6vZnRt4LyAFMAQMCxCOrv4IGgoKCAgBEgSyZfu7DAsQne3BCRqNAQodCglsYXZhIGFyZWHapYj2AwwKCi9tLzBjbm1kNHIKGQoHdm9sY2Fub9qliPYDCgoIL20vMDdfOV8KGgoIbW91bnRhaW7apYj2AwoKCC9tLzA5ZF9yChQKA2FydNqliPYDCQoHL20vMGpqdwofCgxpbGx1c3RyYXRpb27apYj2AwsKCS9tLzAxa3I4Zgw&q=lava+area&tbm=isch&sa=X&ved=2ahUKEwj0joCE1vr0AhWLMpQKHe7cDlkQjJkEegQIHhAC
# https://www.google.com/search?tbs=simg:CAES-QEJE_1sq-9edNeoa7QELELCMpwgaOgo4CAQSFMQY3gv2GIALoT-sKfw--yCIEcQCGhqoLPa00NYLVW5vCIzJAJn8aEu_1P6vZnRt4LyAFMAQMCxCOrv4IGgoKCAgBEgSyZfu7DAsQne3BCRqNAQodCglsYXZhIGFyZWHapYj2AwwKCi9tLzBjbm1kNHIKGQoHdm9sY2Fub9qliPYDCgoIL20vMDdfOV8KGgoIbW91bnRhaW7apYj2AwoKCC9tLzA5ZF9yChQKA2FydNqliPYDCQoHL20vMGpqdwofCgxpbGx1c3RyYXRpb27apYj2AwsKCS9tLzAxa3I4Zgw&q=lava+area&tbm=isch&sa=X&ved=2ahUKEwj0joCE1vr0AhWLMpQKHe7cDlkQjJkEegQIHhAC#imgrc=Nn51jFU8Ty1Y4M

# https://www.google.com/search?tbs=simg:CAES9QEJ_1PxHSrB219Ea6QELELCMpwgaOgo4CAQSFMQY3gv8PvkuqCPBHoQ05R20CsQCGhp5fDOtdX4P2y0Sosqo5TJLtEChpgDmdDkUQCAFMAQMCxCOrv4IGgoKCAgBEgSvE5KKDAsQne3BCRqJAQodCgpob3Jpem9udGFs2qWI9gMLCgkvYS8ybXF2emMKGQoGc3VtbWl02qWI9gMLCgkvbS8wMzg4c24KFgoEc25vd9qliPYDCgoIL20vMDZfZG4KGQoHZ2xhY2llctqliPYDCgoIL20vMDM4anoKGgoHbnVuYXRha9qliPYDCwoJL20vMDJ6NDdtDA&q=horizontal&tbm=isch&sa=X&ved=2ahUKEwjk_cqY2fr0AhXD7WEKHUt2AngQjJkEegQIAhAC
# https://www.google.com/search?tbs=simg:CAES9QEJ_1PxHSrB219Ea6QELELCMpwgaOgo4CAQSFMQY3gv8PvkuqCPBHoQ05R20CsQCGhp5fDOtdX4P2y0Sosqo5TJLtEChpgDmdDkUQCAFMAQMCxCOrv4IGgoKCAgBEgSvE5KKDAsQne3BCRqJAQodCgpob3Jpem9udGFs2qWI9gMLCgkvYS8ybXF2emMKGQoGc3VtbWl02qWI9gMLCgkvbS8wMzg4c24KFgoEc25vd9qliPYDCgoIL20vMDZfZG4KGQoHZ2xhY2llctqliPYDCgoIL20vMDM4anoKGgoHbnVuYXRha9qliPYDCwoJL20vMDJ6NDdtDA&q=horizontal&tbm=isch&sa=X&ved=2ahUKEwjk_cqY2fr0AhXD7WEKHUt2AngQjJkEegQIAhAC#imgrc=No3MJEqerUwceM

