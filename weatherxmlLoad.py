#url로 접근할 수는 없고, xml데이터만 있을 때 그걸 어떻게 읽어와서 내가 원하는 방식으로 바꿀것인가에 대한 활용법
from bs4 import BeautifulSoup

xstring = open("myxmlfile.xml", "r")
soup = BeautifulSoup(xstring, 'xml')
# print(soup.text)

items = soup.find_all('item')
# print(items)

datalist = []
for item in items:
    weatherData = {
        "date": '',
        "location": '',
        "avgTemp": '',
        "minTemp": '',
        "maxTemp": ''
    }
    weatherData["date"] = item.find("tm").text
    weatherData["location"] = item.find("stnId").text
    weatherData["avgTemp"] = item.find("avgTa").text
    weatherData["minTemp"] = item.find("minTa").text
    weatherData["maxTemp"] = item.find("maxTa").text
    datalist.append(weatherData)
print(datalist)

# xstring = re.sub(r"\s+", "", xstring)
# dom = minidom.parseString(xstring)
# items = dom.getElementsByTagName("item")