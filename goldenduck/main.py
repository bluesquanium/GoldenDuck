import os
import goldenduck.pkg.config as config
import pandas as pd
import json
import requests

c = config.load(os.getcwd()+"/conf.yaml")

print(c)

dartApiKey = c.dartApiKey
companyCode = "024110"
startDate = "19990101"

url = "http://dart.fss.or.kr/api/search.json?auth=" + dartApiKey + "&crp_cd=" + companyCode + "&start_dt=" + startDate + "&bsn_tp=A001&bsn_tp=A002&bsn_tp=A003"

json_data = json.loads(requests.get(url).text)
print(json_data)

df = pd.DataFrame(json_data['list'])

xlxs_dir = os.path.join(os.getcwd(), "test" + ".xlsx")
df.to_excel(xlxs_dir)