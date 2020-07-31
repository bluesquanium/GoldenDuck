import requests
import json
import pandas as pd
import os
import goldenduck.pkg.config as config

c = config.load(os.getcwd()+"/conf.yaml")

# Get ETF Item List
def getEtfItemList(c):
    target = "etfItemList"
    url = 'https://finance.naver.com/api/sise/etfItemList.nhn'
    json_data = json.loads(requests.get(url).text)

    df = pd.DataFrame(json_data['result'][target])

    xlxs_dir = os.path.join(c.outputDir, target+ ".xlsx")
    df.to_excel(xlxs_dir)
    
#getEtfItemList(c)

# Get 국내증시 - 기업 요약
def getItemSummary(c, companyCode):
    url = 'https://api.finance.naver.com/service/itemSummary.nhn?itemcode=' + companyCode
    json_data = json.loads(requests.get(url).text)
    
    df = pd.Series(json_data, name='Value')
    df.index.name = 'Name'
    df = df.reset_index()

    xlxs_dir = os.path.join(c.outputDir, "item_summary_" + companyCode + ".xlsx")
    df.to_excel(xlxs_dir)

getItemSummary(c, "005930")