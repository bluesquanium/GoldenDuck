import requests
import json
import pandas as pd
import os

target = "etfItemList"
url = 'https://finance.naver.com/api/sise/etfItemList.nhn'
json_data = json.loads(requests.get(url).text)

df = pd.DataFrame(json_data['result'][target])

xlxs_dir = os.path.join(os.getcwd(), target+ ".xlsx")
df.to_excel(xlxs_dir)