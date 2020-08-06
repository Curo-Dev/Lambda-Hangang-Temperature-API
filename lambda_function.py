import datetime
import requests
from bs4 import BeautifulSoup

dt = datetime.datetime.now()
now_date = dt.strftime('%Y-%m-%d %H:%M')

def getDate(dt):
  return dt.strftime('%Y-%m-%d')

def getTemp(date):
  url = "http://www.koreawqi.go.kr/wQDDRealTotalDataList_D.wq"

  params = {
    'item_id' : 'M69',
    'action_type' : 'L',
    'action_type_seq' : '1',
    'auto_flag' : '',
    'auto_site_id' : 'S01007',
    'search_data_type' : '1',
    'search_flag2' : '1',
    'river_id' : 'R01',
    'site_id' : '\'S01004\'',
    'site_name' : '구리',
    'search_interval' : 'HOUR',
    'search_date_from' : date,
    'search_date_to' : date,
    'order_type_1' : 'MSR_DATE',
    'order_type_2' : 'ASC',
  }

  headers = {
    'User-Agent' : 'HT-API/1.0',
    'Content-Type' : 'application/x-www-form-urlencoded',
  }

  data = requests.get(
    url, params=params, headers=headers
  )

  soup = BeautifulSoup(
    data.text,
    'html.parser'
  )

  result = soup.find('table', { 'class', 'table_04'}).find_all_next('td')

  return result[-1].text.strip()
  
def lambda_handler(event, context):
  result = getTemp(getDate(dt))

  if result == '':
    if dt.hour <= 1:
      result = getTemp(getDate(dt - datetime.timedelta(days = 1)))
      if result == '':      
        result_json = {
          'result' : 'OK',
          'tem' : result,
          'date' : now_date,
        }
      else:
        result_json = {
          'result' : 'NO_CONTENT',    
          'date' : now_date,
        }    
    else:
      result_json = {
        'result' : 'NO_CONTENT',    
        'date' : now_date,
      }
  else:
    result_json = {
      'result' : 'OK',
      'tem' : result,
      'date' : now_date,
    }

  print(result_json);