import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Password@123',
    database='pythondecember',
    auth_plugin = 'mysql_native_password'
)
def get_data():
    cursor=db.cursor()
    sql="select * from movie"

    cursor.execute(sql)
    yield cursor.fetchall()


movies=get_data()
print(movies.__next__())