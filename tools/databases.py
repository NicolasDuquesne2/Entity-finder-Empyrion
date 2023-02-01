import glob
import sqlite3
import re
from tools.configs import ConfigsParams
from tools.apptests import AppTests


class Database():
    """Classe représant une base de donnée"""
    def __init__(self):
        self.name = None

    
    def open(self, db_name):
        path_test = glob.glob(db_name)
        if path_test:
            self.name = db_name
    

    def select(self, sql, db_name):
        """Select commands for sql"""
        try:    
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print("[Erreur]", e)
            conn.rollback()
        finally:
            conn.close()

    def actions(self, sql, db_name):
        """for all other sql commands"""
        try:  
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print("[Erreur]", e)
            conn.rollback()
        finally:
            conn.close()
