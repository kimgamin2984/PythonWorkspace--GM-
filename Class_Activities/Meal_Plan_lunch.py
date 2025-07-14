import requests
import datetime
from pytz import timezone

API_KEY = 'a674e173d3784aac9f10e73862de6dfb'

ATPT_OFCDC_SC_CODE = 'D10'
SD_SCHUL_CODE = '7240082'

today = datetime.datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d")

url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
params = {
    'KEY': API_KEY,
    'Type': 'json',
    'ATPT_OFCDC_SC_CODE': ATPT_OFCDC_SC_CODE,
    'SD_SCHUL_CODE': SD_SCHUL_CODE,
    'MLSV_YMD': today
}

response = requests.get(url, params=params)
data = response.json()

try:
    meals = data['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
    cleaned_meals = meals.replace('<br/>', '\n')
    print(f"[오늘 점심 메뉴]\n{cleaned_meals}")
except:
    print("오늘은 급식 정보가 없거나 오류가 발생했어요.")