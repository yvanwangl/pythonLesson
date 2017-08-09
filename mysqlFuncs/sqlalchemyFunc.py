from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # 表名
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:wangyafei@localhost:3306/test')
# 创建DBsession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
# 新创建一个user对象
new_user = User(id='1', name='wangyafei')
# 添加到session
session.add(new_user)
# 提交事务
session.commit()
# 关闭session
session.close()

# 创建session
session = DBSession()
# 创建Query查询，返回一个User对象实例
user = session.query(User).filter(User.id == '1').one()

# 打印查询结果实例
print(type(user))
print(user.name)
# 关闭session
session.close()
