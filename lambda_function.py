from datetime import timedelta, datetime
import requests
from bs4 import BeautifulSoup
from pytz import timezone

dt = datetime.now(timezone("Asia/Seoul"))
now = dt.strftime('%Y/%m/%d %H:%M:%S')
year = dt.strftime('%Y')
month = dt.strftime('%m')
day = (dt - timedelta(days=1)).strftime('%d')
dateFormat = year +'-' + month + '-' + str(day)
date = year + month + day

def getTemp():


  return data.json()['list'][0]

def lambda_handler(event, context):
  url = "http://water.nier.go.kr/web/autoMeasure/noConfirm/toastList"

  params = {
    'dFielNm': '%EC%9E%90%EB%A3%8C+%EC%A1%B0%ED%9A%8C',
    'excelSnsNos': '',
    'pMENU_NO': 574,
    'page': 1,
    'ATTR_2': date,
    'ATTR_3': date,
    'querySn': 60,
    'queryTp': 'autoMe',
    'confirmNum': 2,
    'station_code': 'S01004',
    'pStartDay': dateFormat,
    'pEndDay': dateFormat,
    'pageSize': 10
  }

  headers = {
    'User-Agent' : 'HT-API/1.0',
    'Content-Type' : 'application/x-www-form-urlencoded',
  }

  result = requests.post(
    url, params=params, headers=headers
  ).json()['list'][0]

  result_json = {
    'result' : 'OK',
    'temperature' : result['IEM_WTRTP'],
    'target_date' : result['MESURE_DT'],
    'now_date' : now,
  }

  return result_json

print (lambda_handler(0, 0))

        
