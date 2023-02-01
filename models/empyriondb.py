from tools.apptests import AppTests
from tools.databases import Database

class DataBaseModel():

    def __init__(self):
        self.app_test = AppTests()
        self.database = Database().open("db/configs.db")
        self.db_query_tables = ""


    def is_empyrion_db(self, db_name):

        sqlite_schema = self.database.select(self.db_query_tables, db_name)
        is_empyrion_db = self.app_test.is_empyrion_db_file(sqlite_schema)
        if is_empyrion_db:
            return True
        else:
            return False
