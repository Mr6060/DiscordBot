import sqlite3


class DB:

    def __init__(self):
        with sqlite3.connect("main.db") as self.db:
            self.cursor = self.db.cursor()

    def db_commit(self):
        self.db.commit()

    def db_close(self):
        self.db.close()

    def db_execute(self, sql_command):
        return self.cursor.execute(sql_command)

    def create_table(self, table_name, **kwargs):

        columns = ", ".join([f"{key} {value}" for key, value in kwargs.items()])
        sql_command = f"CREATE TABLE {table_name}({columns})"

        return self.db_execute(sql_command)







