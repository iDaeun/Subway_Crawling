import pandas as pd
from bs4 import BeautifulSoup
import requests

startnum = 1
endnum = 10
use_mon = 201501
SubwayInfo = {}

use_mon_list = []
line_num = []
sub_station = []
# 00시승차, 하차인원 (시간단위:1시간)
FOUR_RIDE_NUM = []
FOUR_ALIGHT_NUM = []
FIVE_RIDE_NUM = []
FIVE_ALIGHT_NUM = []
SIX_RIDE_NUM = []
SIX_ALIGHT_NUM = []

if endnum <= 1000:
    url = 'http://openapi.seoul.go.kr:8088/647047637a656b6434385274774659/xml/' \
          'CardSubwayTime/'+str(startnum)+'/'+str(endnum)+'/'+str(use_mon)+'/1호선'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('sub_sta_nm')

    # print(soup) : 파싱한 html
    # print(test) : 해당 태그 내용들 모두 찾기
    # print(test[0].text) : 태그 내용들 중 하나만 찾기
