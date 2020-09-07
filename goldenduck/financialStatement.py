#-*- coding:utf-8 -*-
import dart_fss as dart
import pathlib
import os
import pymysql
import goldenduck.pkg.config as config
import pandas as pd

label_ko = {
    '유동자산': "totalCurrentAssets",
    '현금및현금성자산': "cashAndCashEquivalent",
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

label_id = {
    'ifrs-full_CurrentAssets': "totalCurrentAssets",
    'ifrs-full_CashAndCashEquivalents': "cashAndCashEquivalent",
    'dart_ShortTermDepositsNotClassifiedAsCashEquivalents': "shortTermFinancialInstruments",
    'entity00126380_udf_BS_2020210113420730_CurrentAssets': "availableForSaleFinancialAsset",
    'entity00126380_udf_BS_201851017339116_CurrentAssets': "shortTermAfterDepreciationCapitalAsset",
    'ifrs-full_CurrentFinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue': "currentFinancialAssetsAtFairValueThroughProfitOrLoss",
    'dart_ShortTermTradeReceivable': "shortTermTradeReceivable",
    'entity00126380_udf_BS_201710182279121_CurrentAssets': "otherAccountReceivable",
    'entity00126380_udf_BS_20171018221011173_CurrentAssets': "advancePayment",
    'entity00126380_udf_BS_2017101822109437_CurrentAssets': "prepaidExpense",
    'ifrs-full_Inventories': "inventory",
    'dart_OtherCurrentAssets': "otherCurrentAsset",
    'ifrs-full_NoncurrentAssets': "totalNonCurrentAssets",
    'entity00126380_udf_BS_2020210113513266_NoncurrentAssets': "longTermDepositsNotClassified",
    'entity00126380_udf_BS_2020210113515706_NoncurrentAssets': "heldToMaturity",
    'entity00126380_udf_BS_20185101782898_NoncurrentAssets': "afterDepreciationCapitalAsset",
    'entity00126380_udf_BS_201851017830322_NoncurrentAssets': "ociFairValueCapitalAsset",
    'entity00126380_udf_BS_201851017832579_NoncurrentAssets': "incomeFairValueCapitalAsset",
    'entity00126380_udf_BS_20171018221637438_NoncurrentAssets': "availableForSaleFinancialAssetAssociatesAndJointVentures",
    'ifrs-full_PropertyPlantAndEquipment': "propertyAndPlantAndEquipment",
    'ifrs-full_IntangibleAssetsOtherThanGoodwill': "intangibleAssets",
    'dart_DepositsForSeveranceInsurance': "depositsForSeveranceInsurance",
    'ifrs-full_DeferredTaxAssets': "deferredTasAssets",
    'dart_OtherNonCurrentAssets': "otherNonCurrentAssets",
    'ifrs-full_Assets': "totalAssets",
    'ifrs-full_CurrentLiabilities': "totalCurrentLiabilities",
    'entity00126380_udf_BS_20171018222617796_CurrentLiabilities': "accountPayableTrade",
    'ifrs-full_ShorttermBorrowings': "shortTermBorrowings",
    'entity00126380_udf_BS_20171018222642264_CurrentLiabilities': "otherPayble",
    'entity00126380_udf_BS_20171018222640707_CurrentLiabilities': "advanceReceived",
    'entity00126380_udf_BS_20171018222637261_CurrentLiabilities': "withholdings",
    'entity00126380_udf_BS_20171018222635206_CurrentLiabilities': "accruedExpense",
    'ifrs-full_CurrentTaxLiabilities': "currentTaxLiabilities",
    'entity00126380_udf_BS_20171024141934989_CurrentLiabilities': "currentPortionOfLongTermBorrowingsAndDebentures",
    'ifrs-full_CurrentProvisions': "currentProvisions",
    'dart_OtherCurrentLiabilities': "otherCurrentLiabilities",
    'ifrs-full_NoncurrentLiabilities': "totalNonCurrentLiabilities",
    'dart_BondsIssued': "bondsIssued",
    'dart_LongTermBorrowingsGross': "longTermBorrowingsAndGross",
    'dart_LongTermOtherPayablesGross': "longTermOtherPayablesAndGross",
    'dart_PostemploymentBenefitObligations': "postEmploymentBenefitObligations",
    'ifrs-full_DeferredTaxLiabilities': "deferredTaxLiabilities",
    'ifrs-full_NoncurrentProvisions': "nonCurrentProvisions",
    'dart_OtherNonCurrentLiabilities': "otherNonCurrentLiabilities",
    'ifrs-full_Liabilities': "totalLiabilities",
    'ifrs-full_EquityAttributableToOwnersOfParent': "totalEquityAttributableToOwnersOfParent",
    'ifrs-full_IssuedCapital': "totalIssuedCapital",
    'dart_IssuedCapitalOfPreferredStock': "issuedCapitalOfPreferredStock",
    'dart_IssuedCapitalOfCommonStock': "issuedCapitalOfCommonStock",
    'ifrs-full_SharePremium': "sharePremium",
    'ifrs-full_RetainedEarnings': "retainedEarnings",
    'dart_ElementsOfOtherStockholdersEquity': "elementsOfOtherStockholdersEquity",
    'ifrs-full_NoncontrollingInterests': "nonControllingInterests",
    'ifrs-full_Equity': "totalEquity",
    'ifrs-full_EquityAndLiabilities': "totalEquityAndLiabilities",
}

# Load config
c = config.load(str(pathlib.Path(os.getcwd())) + "/fs-conf.yaml")

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

    print(row[0])
    corpCode = row[0] # row['corpCode']
    fs = dart.fs.extract(corp_code=corpCode, bgn_de='20190101', lang='en', separator=False)
    df_fs = fs['bs'].iloc[:,[0, 1, 2, 8]]
    df_fs = df_fs.fillna(DEFAULT_VALUE)
    print(df_fs.head())

    sqlForm = 'insert into {table} ({list}) values ({values})'
    listArr = []
    valuesArr = []
    listArr.append("corpCode")
    valuesArr.append('"' + row[0] + '"')
    listArr.append("date")
    valuesArr.append(df_fs.columns[3][0])
    for label in label_id:
        if len(df_fs[df_fs.iloc[:,0] == label]) != 0:
            listArr.append(label_id[label])
            valuesArr.append(df_fs[df_fs.iloc[:,0] == label].iloc[0,3])
        else:
            print(label + "was empty!")
    # Execute the SQL command
    curs.execute( sqlForm.format(table=table, list=", ".join(listArr), values=", ".join(map(str, valuesArr))) )
    # Commit changes
    conn.commit()

# Test
sql = 'select * from FinancialStatement where corpCode=005930'
curs.execute(sql)
rows = curs.fetchall()
print(rows)