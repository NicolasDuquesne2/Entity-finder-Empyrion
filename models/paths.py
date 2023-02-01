from glob import glob
from tools.databases import Database
from tools.apptests import AppTests

class PathModel():
    def __init__(self):
        self.database = Database()
        self.database.open("db/configs.db")
        self.app_tests = AppTests()
        self.config_db_query_all_db_paths = "SELECT db_path FROM configs"
        self.config_db_query_all_db_paths_desc = "SELECT db_path FROM configs ORDER BY last_modif DESC"
        self.config_db_query_last_db_path = "SELECT db_path, MAX(last_modif) FROM configs"


    def get_all_paths(self):
        return self.database.select(self.config_db_query_all_db_paths_desc, self.database.name)


    def get_one_db_path_sql(self, db_path):
        return "SELECT db_path FROM configs WHERE db_path='"+ db_path +"'"
    
    def add_to_config_db_sql(self, db_path):
        return "INSERT INTO configs (db_path, last_modif) VALUES ('"+db_path+"', datetime('now'))"


    def check_paths(self):
        sql = self.config_db_query_all_db_paths
        rows = self.database.select(sql, self.database.name)
        if rows:
            for row in rows:
                db_path = row[0]
                path_test = glob(db_path)
                if not path_test :
                    sql="DELETE FROM configs WHERE db_path='"+db_path+"'"
                    self.database.actions(sql, self.database.name)


    def set_last_db_path(self, db):
        row = self.database.select(self.config_db_query_last_db_path, self.database.name)
        if row and row[0][0]:
            db_path = row[0][0]
            path_test = glob(db_path)
            is_sqlite3 = self.app_tests.is_SQLite3(db_path)
            if path_test and is_sqlite3: 
                db.name = db_path
    
    """ adds path in the config db if only path do not exit"""
    def add_in_config_db(self, db_name):
        path_test = glob(db_name)
        if path_test:
            row = self.database.select(self.get_one_db_path_sql(db_name), self.database.name)
            if not row:
                sql = self.add_to_config_db_sql(db_name)
                self.database.actions(sql, self.database.name)

    """ is_in_db checks if an element is in a database """
    def is_in_db(self, db_name):
        row = self.database.select(self.get_one_db_path_sql(db_name), self.name)
        if row:
            return True
    