# 기상자료 open API https://data.kma.go.kr/api/selectApiList.do?pgmNo=42

import urllib.request
import json
from xml.dom import minidom

serviceKey = "u1787ibmOGLYJ8lrbxwPk3MauGKscWK%2BYHPhsXnslQqFvGaN67hTnAfYc288yxkVGUdJzw92MvOJ%2BkGuORJBxw%3D%3D"
startDt = "20190101"
endDt = "20191231"
stnIds = "112"  # 지역을 의미(112: 인천)

# url setting (기상청02_지상_종관__ASOS__일자료_조회서비스_오픈API활용가이드.docx)
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey="+serviceKey + \
    "&numOfRows=365&pageNo=1&dataCd=ASOS&dateCd=DAY&startDt=" + \
    startDt+"&endDt="+endDt+"&stnIds="+stnIds

# urllib으로 http 통신 => HTTPResponse
response = urllib.request.urlopen(url)

# minidom을 이용하여 XML 파싱 <-- 코드 전개가 쉽다.
# import xml.etree.ElementTree 이것도 많이 사용 <-- XML 구성 쉽다
dom = minidom.parse(response) #http파일인 response객체를 다루기 쉬운 document로 바꾼다

# 파일 만들기(xml형태)
f = open("myxmlfile.xml", "w")
dom.writexml(f, indent='\t', addindent='\t',  newl='\n')
f.close()

# minidom으로 만든 Document Object로 컨트롤
items = dom.getElementsByTagName("item") #item 태그를 기반으로 elements들을 가져와라

# items에 저장된 Object의 특정 변수를 가져와 보자
print(type(items))
print(items)

print(type(items[0].childNodes[0]))
print(items[0].childNodes[0])
print(items[0].childNodes[0].nodeName)

print(type(items[0].childNodes[0].childNodes[0]))
print(items[0].childNodes[0].childNodes[0])
print(items[0].childNodes[0].firstChild.nodeValue)
print(items[0].childNodes[0].lastChild.nodeValue)
print(items[0].childNodes[0].childNodes[0].nodeValue)

# xml ---> dic 타입으로 변경하고 리스트에 저장
datalist = []
for item in items:
    weatherData = {
        "date": '',
        "location": '',
        "avgTemp": '',
        "minTemp": '',
        "maxTemp": ''
    } #딕셔너리 초기화 방식
    node = item.childNodes
    weatherData["date"] = node[1].childNodes[0].nodeValue
    weatherData["location"] = node[0].childNodes[0].nodeValue
    weatherData["avgTemp"] = node[2].childNodes[0].nodeValue
    weatherData["minTemp"] = node[3].childNodes[0].nodeValue
    weatherData["maxTemp"] = node[5].childNodes[0].nodeValue
    datalist.append(weatherData)
print(datalist)

# 리스트에 저장된 weather data를 Json으로 변경
# json_val = json.dumps(datalist)
json_test_dict = json.dumps(
    datalist, ensure_ascii=False, indent=4).encode('utf-8')
                                  #indent: 들어쓰기
f = open("myjsonfile.json", "wb") #"w"로 하면  binary error 발생
f.write(json_test_dict)
f.close()