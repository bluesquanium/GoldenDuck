import os
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import goldenduck.pkg.config as config

c = config.load(os.getcwd()+"/conf.yaml")

stockCode = "005930"
df = web.DataReader(stockCode+".KS", "yahoo")

xlxs_dir = os.path.join(c.outputDir, "stock" + stockCode + ".xlsx")
df.to_excel(xlxs_dir)

plt.plot(df.index, df['Adj Close'])
plt.show()