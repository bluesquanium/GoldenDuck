#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import pathlib
import pandas as pd
import pymysql

# config
host = '172.17.0.2'
port = 3306
user = 'root'
password = 'password'
db = 'test'
table = 'Company'

# connect to db
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
curs = conn.cursor()

# read the excel file
df = pd.read_excel(str(pathlib.Path(os.getcwd()))+"/상장법인목록.xlsx", dtype=str)

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
