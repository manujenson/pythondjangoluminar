#import mysql.connecter
#establish a connector with mysql

import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password@123',
    auth_plugin='mysql_native_password'

)

#create a cursor objct

cursor=db.cursor()

sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()