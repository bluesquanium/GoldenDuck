#-*- coding:utf-8 -*-
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import os
import xml.etree.ElementTree as elemTree
import pandas as pd
import pathlib
import pymysql
import goldenduck.pkg.config as config

# Load config
c = config.load(str(pathlib.Path(os.getcwd())) + "/conf.yaml")

api_key = c.dartApiKey
host = c.mysqlHost
port = c.mysqlPort
user = c.mysqlUser
password = c.mysqlPassword
db = c.mysqlDatabase
table = c.mysqlTable

### API call for corpCode
url = 'https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=' + api_key
res = urlopen(url)
zfile = ZipFile(BytesIO(res.read()))

### Read xml file from received zip file
tree = elemTree.parse(zfile.open('CORPCODE.xml'))
root = tree.getroot()

### Find corpCode by stockCode function
def findCorpCode(stockCode):
    for country in root.iter("list"):
        if country.findtext("stock_code") == stockCode:
            return country.findtext("corp_code")

### Find corpCode by corpName function
def findCorpCodeByName(name):
    for country in root.iter("list"):
        if country.findtext("corp_name") == name:
            return country.findtext("corp_code")

# connect to db
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
curs = conn.cursor()

# Update DB
try:
    sqlForm = 'update {table} set corpCode="{corpCode}" where koreanName="{koreanName}"'
    for corp in root.iter("list"):
        if corp.findtext("stock_code") != " " :
            sql = sqlForm.format(table=table, corpCode=corp.findtext("corp_code"), koreanName=corp.findtext("corp_name"))
            curs.execute(sql)
            conn.commit()
except Exception as e:
	print("err: " + str(e))
	# Rollback
	conn.rollback()

print("Job Finished.")