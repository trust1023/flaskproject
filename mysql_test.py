import pymysql

conn = pymysql.connect(host='47.99.42.184',user='dlw',password='Mysql123456@',db='project')
cursor = conn.cursor()
sql = 'update users_verifycode set code=%s where mobile=%s'%('2345','123')
try:
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e.args)

