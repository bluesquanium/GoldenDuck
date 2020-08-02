import os
import pathlib
import pandas as pd
import json
import requests
import goldenduck.pkg.config as config

c = config.load(str(pathlib.Path(os.getcwd()).parent.parent) + "/conf.yaml")

print(c)

dartApiKey = c.dartApiKey
companyCode = "005930"
startDate = "19990101"

url = "http://dart.fss.or.kr/api/search.json?auth=" + dartApiKey + "&crp_cd=" + companyCode + "&start_dt=" + startDate + "&bsn_tp=A001&bsn_tp=A002&bsn_tp=A003"

json_data = json.loads(requests.get(url).text)
print(json_data)

df = pd.DataFrame(json_data['list'])

xlxs_dir = os.path.join(c.outputDir, "test" + ".xlsx")
df.to_excel(xlxs_dir)

## 작성하다 말음