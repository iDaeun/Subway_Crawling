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

    # 1. 총 데이터 건수
    listNum = soup.find('list_total_count')
    print('총 데이터 건수: '+listNum.text)

    # 2. 데이터 수집
    sub_sta_nm = soup.find_all('sub_sta_nm')

    four_ride_num = soup.find_all('four_ride_num')
    four_alight_num = soup.find_all('four_alight_num')
    five_ride_num = soup.find_all('five_ride_num')
    five_alight_num = soup.find_all('five_alight_num')
    six_ride_num = soup.find_all('six_ride_num')
    six_alight_num = soup.find_all('six_alight_num')

    # 3. 데이터 가공
    # 직전 전동차에 있던 사람의 수 + (승차인원 - 하차인원) = 해당 전동차 안에 있는 사람의 수
    # **주의 : 한 노선만 보고 계산하면 안되고, 다른 호선과 연결되어있는 역을 파악해서 직전 역이 무엇인지 알아야함!
    # **예시 : 1호선 서울역 -> 직전역은 9호선 노량진역으로 검색 가능
    
    # 0 ~ 총 데이터 건수

    # (승차인원-하차인원) <- 이부분
    # 직전 역의 사람수를 더하지 않았기 때문에 음수값이 나오는 경우도 있음
    # 04~05시
    for i in range(0, int(listNum.text)):
            print(str(i) + sub_sta_nm[i].text + ":" + str(int(four_ride_num[i].text) - int(four_alight_num[i].text)))
    # 05~06시
    for i in range(0, int(listNum.text)):
            print(str(i) + sub_sta_nm[i].text + ":" + str(int(five_ride_num[i].text) - int(five_alight_num[i].text)))
    # 06~07시
    for i in range(0, int(listNum.text)):
            print(str(i) + sub_sta_nm[i].text + ":" + str(int(six_ride_num[i].text) - int(six_alight_num[i].text)))
    # 07~08시
    # 08~09시
    # 09~10시
    # 10~11시
    # 11~12시
    # 12~13시
    # 13~14시
    # 14~15시
    # 15~16시
    # 16~17시
    # 17~18시
    # 18~19시
    # 19~20시
    # 20~21시
    # 21~22시
    # 22~23시
    # 23~24시
    # 00~01시
    # 01~02시
    # 02~03시
    # 03~04시


    # 4. 수집한 데이터 -> list에 append
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

    # 5. 수집한 list -> SubwayInfo에 통합
    SubwayInfo['SubwayName'] = sub_sta_nm_list
    SubwayInfo['04시-05시 승차인원'] = four_ride_num_list
    SubwayInfo['04시-05시 하차인원'] = four_alight_num_list
    SubwayInfo['05시-06시 승차인원'] = five_ride_num_list
    SubwayInfo['05시-06시 하차인원'] = five_alight_num_list
    SubwayInfo['06시-07시 승차인원'] = six_ride_num_list
    SubwayInfo['06시-07시 하차인원'] = six_alight_num_list

    # 6. pandas dataframe 사용
    df = pd.DataFrame(SubwayInfo)

    # print(df)

    # ++ 추가해야하는 내용
    # 1. 또 다른 API사용 : 역코드로 검색 → 출발시간으로 시간대별 몇량의 지하철이 운행하는지 계산
    # 2. 1~4호선은 10량(정원-160*10), 기타 노선은 6~8량(정원-160*6~8)으로 기준 → 혼잡도 계산
    # 3. 직전 역의 사람 수와 더해서 순수 그 역에서 전동차에 있는 사람의 수를 구함
