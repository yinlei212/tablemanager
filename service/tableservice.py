from core.globals import db_manager


class TableService:
    def list_tables(self):
        return db_manager.list_table()

    def show_table_column(self, table_name):
        return db_manager.show_table_columns(table_name)

    def sql_page(self, table_name, page, limit):
        start = (page - 1) * limit
        sql = f"select * from {table_name} limit {start},{limit}"
        return db_manager.query_sql(sql)

    def count(self,table_name):
        sql = f"select count(*) from {table_name}"
        return db_manager.query_sql(sql)[0][0]


if __name__ == '__main__':
    service = TableService()
    # result = service.sql_page('data_wanqu_detail', 1, 20)
    #
    # for result_ in result:
    #     print(result_)
    print(service.count('data_wanqu_detail'))