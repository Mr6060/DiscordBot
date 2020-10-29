from db import open_db

db = open_db.DB()
print(db.create_table(table_name="test", colonna1="TEXT", colonna2="INT"))
db.db_commit()
db.db_close()