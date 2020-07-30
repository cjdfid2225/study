import json
import os
import sys
import urllib.request
import re

client_id = "Lwl42tHXk1L5LMaIO9x3"
client_secret = "xJG0dOuOLR"
encText = urllib.parse.quote("여행")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
jsondata=[]
if(rescode==200):
    response_json = json.load(response)
    jsondata.append(response_json)
    with open('navernews/test.json','w',encoding='utf-8') as make_file:
        json.dump(response_json,make_file, indent="\t",ensure_ascii=False)
else:
    print("Error Code:" + rescode)


title = []
for i in range(0,10):
    title = jsondata[0]['items'][i]['title']
    print(title)
    title = re.sub('(<([^>]+)>)','',title,0,re.I|re.S)
    print(title)
