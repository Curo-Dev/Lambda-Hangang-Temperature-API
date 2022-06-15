import datetime
import requests
from bs4 import BeautifulSoup
from pytz import timezone



def getDate(dt):
  return dt.strftime('%Y-%m-%d')

def getTemp(date):
  url = "http://water.nier.go.kr/web/waterMeasure/toastList"

  params = {
    'dFielNm': '자료 조회',
    'excelSnsNos': '',
    'pMENU_NO': 571,
    'page': '',
    'type_date': 9,
    'ATTR_2': 202204, # LAST DATE
    'ATTR_3': date, # NOW DATE 
    'ATTR_7': 'DAY',
    'querySn': 9,
    'gubun': 'Search2',
    'befor': 9,
    'query': 'SELECT WQMN_CODE, WQMN_NM, CHCK_DE, TME, IEM_WTRTP FROM V_MSR_WQMN_DAY A',
    'excelQuery': 'SELECT WQMN_CODE, WQMN_NM, CHCK_DE, TME, IEM_WTRTP FROM V_MSR_WQMN_DAY A',
    'queryHeader': '',
    'code': 'S001',
    'station_code': '1018A50',
    'serchRadio': 'A',
    'station_codes': '1018A50',
    'station_iem': 'IEM_WTRTP',
    'station_iem': 'IEM_DPWT',
    'station_iem': 'IEM_WTRTP',
    'station_iem': 'IEM_DOC',
    'station_iem': 'IEM_BOD',
    'station_iem': 'IEM_COD',
    'station_iem': 'IEM_SS',
    'station_iem': 'IEM_TN',
    'station_iem': 'IEM_TP',
    'station_iem': 'IEM_TOC',
    'station_iem': 'IEM_WTRTP',
    'station_iem': 'IEM_WTRTP',
    'pageSize': 10
  }

  headers = {
    'User-Agent' : 'HT-API/1.0',
    'Content-Type' : 'application/x-www-form-urlencoded',
  }

  data = requests.post(
    url, params=params, headers=headers
  )

  return data.json()['list'][0]

def lambda_handler(event, context):
  dt = datetime.datetime.now(timezone("Asia/Seoul"))
  now_date = dt.strftime('%Y%m')  
  result = getTemp(now_date)

  result_json = {
    'result' : 'OK',
    'temperature' : result['IEM_WTRTP'],
    'target_date' : result['CHCK_DE'],
    'now_date' : dt.strftime('%Y/%m/%d %H:%M:%S'),
  }

  return result_json

print (lambda_handler(0, 0))
        
