import pandas as pd
from bs4 import BeautifulSoup
import requests

startnum = 1
endnum = 10
use_mon = 201501
subway_name = '1호선'
SubwayInfo = {}

sub_sta_nm_list = []
# 00시승차, 하차인원 (시간단위:1시간)
four_ride_num_list = []
four_alight_num_list = []
five_ride_num_list = []
five_alight_num_list = []
six_ride_num_list = []
six_alight_num_list = []

if endnum <= 600:
    url = 'http://openapi.seoul.go.kr:8088/647047637a656b6434385274774659/xml/' \
          'CardSubwayTime/'+str(startnum)+'/'+str(endnum)+'/'+str(use_mon)+'/'+subway_name
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    sub_sta_nm = soup.find_all('sub_sta_nm')

    four_ride_num = soup.find_all('four_ride_num')
    four_alight_num = soup.find_all('four_alight_num')
    five_ride_num = soup.find_all('five_ride_num')
    five_alight_num = soup.find_all('five_alight_num')
    six_ride_num = soup.find_all('six_ride_num')
    six_alight_num = soup.find_all('six_alight_num')

    for code in sub_sta_nm:
        sub_sta_nm_list.append(code.text)
    for code in four_ride_num:
        four_ride_num_list.append(code.text)
    for code in four_alight_num:
        four_alight_num_list.append(code.text)
    for code in five_ride_num:
        five_ride_num_list.append(code.text)
    for code in five_alight_num:
        five_alight_num_list.append(code.text)
    for code in six_ride_num:
        six_ride_num_list.append(code.text)
    for code in six_alight_num:
        six_alight_num_list.append(code.text)

    print(sub_sta_nm_list)
    print(four_ride_num_list)

