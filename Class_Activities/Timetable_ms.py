import requests
import datetime
from pytz import timezone

API_KEY = "a674e173d3784aac9f10e73862de6dfb"
BASE_URL = "https://open.neis.go.kr/hub/hisTimetable"

today = datetime.datetime.now(timezone('Asia/Seoul'))

params = {
    "KEY": API_KEY,
    "Type": "json",
    "ATPT_OFCDC_SC_CODE": "D10",
    "SD_SCHUL_CODE": "7251083",
    "AY": str(today.year),
    "SEM": "1",
    "ALL_TI_YMD": 20250411, #today.strftime("%Y%m%d"),
    "GRADE": "1",
    "CLASS_NM": "1"
}

res = requests.get(BASE_URL, params=params)
data = res.json()

if "hisTimetable" in data:
    periods = data["hisTimetable"][1]["row"]
    print("[오늘 시간표]")
    for p in periods:
        print(f"{p['PERIO']}교시: {p['ITRT_CNTNT']}")
else:
    print("오늘의 시간표를 찾을 수 없습니다.")