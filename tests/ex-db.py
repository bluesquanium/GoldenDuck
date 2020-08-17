import pymysql

# connect to db
conn = pymysql.connect(host='172.17.0.2', port=3306, user='root', password='password', db='test', charset='utf8')
curs = conn.cursor()

#sql = "select * from table1"
#curs.execute(sql)
#rows = curs.fetchall()
#print(rows)

try:
  # Execute the SQL command
  sql = 'insert into table1 values(5, "k")'
  curs.execute(sql)
  # Commit changes
  conn.commit()
except Exception as e:
  print(str(e))
  # Rollback
  conn.rollback()
  
# Print all of the elements in the table
sql = 'select * from table1'
curs.execute(sql)
rows = curs.fetchall()
print(rows)

#while True:
#  True
