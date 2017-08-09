import mysql.connector

# 执行INSERT等操作后要调用commit()提交事务；
# MySQL的SQL占位符是%s。

conn = mysql.connector.connect(user='root', password='wangyafei', database='test')
cursor = conn.cursor()
cursor.execute('create table user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
cursor.execute('insert into user(id, name) VALUES (%a, %s)', ['1', 'wangyafei'])
print(cursor.rowcount)
# 提交事物
conn.commit()
cursor.close()
# 运行查询
cursor = conn.cursor()
cursor.execute('select * from user where id=%s', ('1',))
result = cursor.fetchall()
print(result)
# 关闭cursor和connect
cursor.close()
conn.close()
