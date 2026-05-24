from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 数据库连接地址（改成你自己的账号密码）
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/medicine?charset=utf8mb4"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
