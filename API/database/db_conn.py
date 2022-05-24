from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json


DB = {
        "user" : "root",
        "password" : "Sunjung0821!",
        "host" : "localhost",
        "port" : 3306,
        "database" : "test"
    }

db_url = f"mysql+pymysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

class engineconn:
    def __init__(self):
        self.engine = create_engine(db_url, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn