# 导入:
from sqlalchemy import Column, String, create_engine, Integer, Text, DateTime, func, Boolean, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()


class DBManager:
    def __init__(self):
        # engine = create_engine('mysql+pymysql://root:root@localhost:3306/cloud_reader', echo=True)
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/spiderflow')
        Base.metadata.create_all(self.engine)

        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=self.engine)

    def add(self, entity):
        try:
            session = self.DBSession()

            session.add(entity)

            session.commit()
            session.refresh(entity)
            session.expunge(entity)
        finally:
            session.close()

    def delete(self, entity, *args):
        try:
            session = self.DBSession()
            q = session.query(entity)
            for arg in args:
                q = q.filter(arg)
            q.delete()
            session.commit()
        finally:
            session.close()

    def query_one_or_none(self, entity, *args):
        try:
            session = self.DBSession()
            q = session.query(entity)
            for arg in args:
                q = q.filter(arg)
            result = q.one_or_none()
            return result
        finally:
            session.close()


    def query_order_by_field(self, entity, order_by, args=[], offset=0, limit=10, ):
        try:
            session = self.DBSession()
            q = session.query(entity)
            for arg in args:
                q = q.filter(arg)
            q = q.order_by(order_by)
            q = q.limit(limit)
            q = q.offset(offset)
            result = q.all()
        finally:
            session.close()
        return result

    def query_sql(self, sql):
        """
        execute sql
        :param sql:
        :return: result
        """
        try:
            session = self.DBSession()

            cursor = session.execute(sql)
            result = cursor.fetchall()
            return result
        finally:
            session.close()

    def execute_sql(self, sql):
        """
        execute sql
        :param sql:
        :return: result
        """
        try:
            session = self.DBSession()

            session.execute(sql)
            session.commit()

        finally:
            session.close()

    def list_table(self):
        result = self.query_sql("show table status;")
        tables = [v[0] for v in result]
        return tables

    def show_table_columns(self, table_name):
        columns = self.query_sql(f"desc {table_name};")

        return [v[0] for v in columns]

    def getPK(self, table_name):
        columns = self.query_sql(f"desc {table_name};")
        for column in columns:
            if column[3] == 'PRI':
                return column[0]


if __name__ == '__main__':
    db = DBManager()
    # print(db.list_table())
    print(db.show_table_columns('data_wanqu'))
#     # a = Article(title='你好111222', title_en='hello111222', link='http://ssssss')
#     # db.add(a)
#     result = db.query_sql(
#         "SELECT s.`subject`,r.book_id from bk_subject s, bk_relationship r WHERE s.id = r.subject_id and s.id =1306")
#     print(result)
