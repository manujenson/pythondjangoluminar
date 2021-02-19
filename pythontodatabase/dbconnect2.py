import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password@123',
    database='pythondecember',
    auth_plugin = 'mysql_native_password'
)
cursor=db.cursor()

sql="create table movie(id int,name varchar(50),year varchar(50),rating int)"
cursor.execute(sql)
print("table created")
db.close()