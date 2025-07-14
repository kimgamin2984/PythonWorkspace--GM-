import requests
import datetime
from pytz import timezone

API_KEY = 'a674e173d3784aac9f10e73862de6dfb'
ATPT_OFCDC_SC_CODE = 'D10'
SD_SCHUL_CODE = '7240082'
GRADE = '1'
CLASS_NM = '3'
ALL_TI_YMD = datetime.datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")

url = 'https://open.neis.go.kr/hub/hisTimetable'
params = {
    'KEY': API_KEY,
    'Type': 'json',
    'ATPT_OFCDC_SC_CODE': ATPT_OFCDC_SC_CODE,
    'SD_SCHUL_CODE': SD_SCHUL_CODE,
    'GRADE': GRADE,
    'CLASS_NM': CLASS_NM,
    'ALL_TI_YMD': ALL_TI_YMD
}

res = requests.get(url, params=params)
data = res.json()

try:
    timetable = data['hisTimetable'][1]['row']
    print(f"[{(int(ALL_TI_YMD)%10000-int(ALL_TI_YMD)%100)//100}월 {int(ALL_TI_YMD)%100}일 시간표 - {GRADE}학년 {CLASS_NM}반]")
    for period in timetable:
        print(f"{period['PERIO']}교시: {period['ITRT_CNTNT']}")
except:
    print("시간표 정보를 불러올 수 없어요.")