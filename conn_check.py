import pymssql
conn = pymssql.connect(
  "192.168.50.4"
  , "sa"
  , "#SAPassword!"
  , "master"
)
cursor = conn.cursor()
query = "SELECT name FROM master.sys.databases"
cursor.execute(query)
for row in cursor:
  print row

conn.close()
