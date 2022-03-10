from urllib import request as ureq
from datetime import datetime
import json
import time
from bs4 import BeautifulSoup as bs4


url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=TW"


def getGoogleTrend():

    request = ureq.Request(url)

    with ureq.urlopen(request) as response:
        html = response.read().decode("utf-8")

    soupHtml = bs4(html, 'html.parser')
    titles = soupHtml.find_all('title')
    titleArr = []
    traffics = soupHtml.find_all('ht:approx_traffic')
    print(len(traffics), len(titles))
    # print(traffics)
    for i in range(1, len(titles)):
        pureTitle = titles[i].string
        if(pureTitle != 'Daily Search Trends'):
            titleArr.append(
                [int(traffics[i-1].string.replace('+', '').replace(',', '')), titles[i].string])

    titleArr.sort(reverse=True)
    timeNow = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    jsonObj = {timeNow: titleArr}
    print(jsonObj)

    with open('./google_trends.json', 'r', encoding='utf-8') as file:
        jsonFile = json.loads(file.read().encode('utf-8'))
        times = jsonFile['Times']
        times.append(timeNow)
        # print(jsonFile['2021/12/24 02:36:30'][0])

    with open('./google_trends.json', 'w', encoding='utf-8') as file:
        jsonFile.update(jsonObj)
        jsonFile.update({'Times': times})
        file.write(
            json.dumps(jsonFile, indent=2)
        )


while(True):
    getGoogleTrend()
    time.sleep(60*3)
