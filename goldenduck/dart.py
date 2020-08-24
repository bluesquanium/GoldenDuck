import dart_fss as dart
import pathlib
import os
import goldenduck.pkg.config as config

# config 불러오기
c = config.load(str(pathlib.Path(os.getcwd())) + "/conf.yaml")
api_key=c.dartApiKey
dart.set_api_key(api_key=api_key)

# 삼성전자 code
corp_code = '00126380'

# 모든 상장된 기업 리스트 불러오기
corp_list = dart.get_corp_list()

# 삼성전자
samsung = corp_list.find_by_corp_name(corp_name=corp_code)

# 2012년 01월 01일 부터 연결재무제표 검색
# fs = samsung.extract_fs(bgn_de='20120101') 와 동일
fs = dart.fs.extract(corp_code=corp_code, bgn_de='20120101')

# 연결재무상태표
df_fs = fs['bs'] # 또는 df = fs[0] 또는 df = fs.show('bs')
# 연결재무상태표 추출에 사용된 Label 정보
labels_fs = fs.labels['bs']

# 연결손익계산서
df_is = fs['is'] # 또는 df = fs[1] 또는 df = fs.show('is')
# 연결손익계산서 추출에 사용된 Label 정보
labels_is = fs.labels['is']

# 연결포괄손익계산서
df_ci = fs['cis'] # 또는 df = fs[2] 또는 df = fs.show('cis')
# 연결포괄손익계산서 추출에 사용된 Label 정보
labels_ci = fs.labels['cis']

# 현금흐름표
df_cf = fs['cf'] # 또는 df = fs[3] 또는 df = fs.show('cf')
# 현금흐름표 추출에 사용된 Label 정보
labels_cf = fs.labels['cf']

# 재무제표 일괄저장 (default: 실행폴더/fsdata/{corp_code}_{report_tp}.xlsx)
#fs.save()

# 재무제표 일괄저장
fs.save(path=c.outputDir)
