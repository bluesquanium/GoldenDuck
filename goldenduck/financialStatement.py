#-*- coding:utf-8 -*-
import dart_fss as dart
import pathlib
import os
import pymysql
import goldenduck.pkg.config as config
import pandas as pd

label_ko = {
    '유동자산': "totalCurrentAssets",
    '현금및현금성자산': "cashAndCashEquivalent float",
    '단기금융상품': "shortTermFinancialInstruments",
    '단기매도가능금융자산': "availableForSaleFinancialAsset",
    '단기상각후원가금융자산': "shortTermAfterDepreciationCapitalAsset",
    '단기당기손익-공정가치금융자산': "currentFinancialAssetsAtFairValueThroughProfitOrLoss",
    '매출채권': "shortTermTradeReceivable",
    '미수금': "otherAccountReceivable",
    '선급금': "advancePayment",
    '선급비용': "prepaidExpense",
    '재고자산': "inventory",
    '기타유동자산': "otherCurrentAsset",
    '비유동자산': "totalNonCurrentAssets",
    '장기매도가능금융자산': "longTermDepositsNotClassified",
    '만기보유금융자산': "heldToMaturity",
    '상각후원가금융자산': "afterDepreciationCapitalAsset",
    '기타포괄손익-공정가치금융자산': "ociFairValueCapitalAsset",
    '당기손익-공정가치금융자산': "incomeFairValueCapitalAsset",
    '관계기업 및 공동기업 투자': "availableForSaleFinancialAssetAssociatesAndJointVentures",
    '유형자산': "propertyAndPlantAndEquipment",
    '무형자산': "intangibleAssets",
    '순확정급여자산': "depositsForSeveranceInsurance",
    '이연법인세자산': "deferredTasAssets",
    '기타비유동자산': "otherNonCurrentAssets",
    '자산총계': "totalAssets",
    '유동부채': "totalCurrentLiabilities",
    '매입채무': "accountPayableTrade",
    '단기차입금': "shortTermBorrowings",
    '미지급금': "otherPayble",
    '선수금': "advanceReceived",
    '예수금': "withholdings",
    '미지급비용': "accruedExpense",
    '당기법인세부채': "currentTaxLiabilities",
    '유동성장기부채': "currentPortionOfLongTermBorrowingsAndDebentures",
    '충당부채': "currentProvisions",
    '기타유동부채': "otherCurrentLiabilities",
    '비유동부채': "totalNonCurrentLiabilities",
    '사채': "bondsIssued",
    '장기차입금': "longTermBorrowingsAndGross",
    '장기미지급금': "longTermOtherPayablesAndGross",
    '순확정급여부채': "postEmploymentBenefitObligations",
    '이연법인세부채': "deferredTaxLiabilities",
    '장기충당부채': "nonCurrentProvisions",
    '기타비유동부채': "otherNonCurrentLiabilities",
    '부채총계': "totalLiabilities",
    '지배기업 소유주지분': "totalEquityAttributableToOwnersOfParent",
    '자본금': "totalIssuedCapital",
    '우선주자본금': "issuedCapitalOfPreferredStock",
    '보통주자본금': "issuedCapitalOfCommonStock",
    '주식발행초과금': "sharePremium",
    '이익잉여금(결손금)': "retainedEarnings",
    '기타자본항목': "elementsOfOtherStockholdersEquity",
    '비지배지분': "nonControllingInterests",
    '자본총계': "totalEquity",
    '자본과부채총계': "totalEquityAndLiabilities",
}

# Load config
c = config.load(str(pathlib.Path(os.getcwd()).parent) + "/fs-conf.yaml")

# config
host = c.mysqlHost
port = c.mysqlPort
user = c.mysqlUser
password = c.mysqlPassword
db = c.mysqlDatabase
table = c.mysqlTable
corplist_table = c.mysqlCorplistTable
api_key = c.dartApiKey
dart.set_api_key(api_key=api_key)

# connect to db
conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
curs = conn.cursor()

# Get all Company list from DB
try:
    sql = 'select corpCode from {table}'.format(table=corplist_table)

    curs.execute(sql)
    rows = curs.fetchall()
except Exception as e:
	print("err: " + str(e))
	# Rollback
	conn.rollback()

DEFAULT_VALUE = -1
# Save FinancialStatement to DB
cnt = 0
total = len(rows)
for row in rows:
    # Print the current progress
    cnt += 1
    if cnt % 10 == 0 :
        print('Current Progress : {cnt} / {total} ')
        # Temp for test
        break

    corpCode = row['corpCode']
    fs = dart.fs.extract(corp_code=corpCode, bgn_de='20190101', lang='en', separator=False)
    df_fs = fs['bs'].iloc[:,[0, 1, 2, 8]]
    df_fs = df_fs.fillna(DEFAULT_VALUE)

    sqlForm = 'insert into {table} ({list}) values ({values})'
    listArr = []
    valuesArr = []
    for label in label_ko:
        listArr.append(label_ko[label])
        valuesArr.append(df_fs[df_fs.iloc[:,1] == label].iloc[0,3])
    
    # Execute the SQL command
    curs.execute( sqlForm.format(table=table, list=", ".join(listArr), values=", ".join(map(str, valuesArr))) )
    # Commit changes
    conn.commit()

# Test
sql = 'select * from FinancialStatement where corpCode=005930'
curs.execute(sql)
rows = curs.fetchall()
print(rows)