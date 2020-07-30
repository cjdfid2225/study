import urllib.request
from bs4 import BeautifulSoup
import re

def get_text(url):
    url_source = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_source,'html.parser',from_encoding='utf-8')
    text = soup.select('#articleBody')[0].get_text().replace('\n','')
    text = text.replace(
        "// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", '')
    text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)
    text = re.sub('\▲','',text)
    text = re.sub('\▶.*$','',text)
    text = re.sub(' +',' ',text) #여러 개의 공백을 하나의 공백으로 줄여준다.
    return text
# 내가 없애고 싶은 특정문자를 알고 있다 > replace 이용
# 정확히 뭐뭐가 있는지는 모르지만 특수기호들을 없애고 싶다 > re.sub 이용

result = get_text('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=028&aid=0002506940&date=20200730&type=1&rankingSeq=2&rankingSectionId=105')
print(result)