import urllib.request
from bs4 import BeautifulSoup
import re

def get_news_title(url):
    url_source = urllib.request.urlopen(url)
    soup = BeautifulSoup(url_source,'html.parser',from_encoding='utf-8')
    text = ''
    for item in soup.find_all('h3',id='articleTitle'):
        text = text + str(item.find_all(text=True))
        text = re.sub(
            '[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', text)
    return text


result = get_news_title('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=028&aid=0002506940&date=20200730&type=1&rankingSeq=2&rankingSectionId=105')
print(result)