#-*- coding:utf-8 -*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import os
import pathlib
import pandas as pd
import pymysql
import goldenduck.pkg.config as config

# TODO:
# It can't update datas. Only can add new data.
# So I have to change the logic like below:
# When a data already exists, do update. Otherwise, do create.

# TODO:
# Job -> CronJob


# config 불러오기
c = config.load(str(pathlib.Path(os.getcwd())) + "/conf.yaml")

# config
host = c.mysqlHost
port = c.mysqlPort
user = c.mysqlUser
password = c.mysqlPassword
db = c.mysqlDatabase
table = c.mysqlTable

# connect to db
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
curs = conn.cursor()

# read the excel file (You have to store the target excel file in the outputs folder)
df = pd.read_excel(c.outputDir+"/상장법인목록.xlsx", dtype=str)

try:
	for i in range(0, len(df)) :
		row = df.iloc[i]

		# Preprocessing
		df = df.fillna('')

		# Execute the SQL command
		sql = 'insert into ' + table + ' (corpCode, koreanName, country, province, listingDate, settlementMonth, ceo, url) values ("' \
		+ row['종목코드'] + '", "' \
		+ row['회사명'] + '", "' \
		+ 'Republic of Korea' + '", "' \
		+ row['지역'] + '", "' \
		+ row['상장일'] + '", ' \
		+ row['결산월'].replace("월", "") + ', "' \
		+ row['대표자명'] + '", "' \
		+ row['홈페이지'] + '")'
		curs.execute(sql)
		# Commit changes
		conn.commit()
except Exception as e:
	print("err: " + str(e))
	# Rollback
	conn.rollback()

# Print the number of elements in the table
sql = 'select count(*) from Company'
curs.execute(sql)
rows = curs.fetchall()
print(rows[0][0])

# Test
sql = 'select * from Company where corpCode=005930'
curs.execute(sql)
rows = curs.fetchall()
print(rows)