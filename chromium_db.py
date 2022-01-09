import os
import shutil
import sqlite3
from chromium_util import DEFAULT_PATH

class ChromeDB():
    def __init__(self, db_name):
        self.db_path = os.path.join(DEFAULT_PATH, db_name)

    def __enter__(self):
        self.filename = "TempChromeData.db"
        shutil.copyfile(self.db_path, self.filename)

        self.db = sqlite3.connect(self.filename)
        self.cursor = self.db.cursor()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.db.close()

        try:
            os.remove(self.filename)
            print("Success removing temp db file")
        except:
            print("Failed removing temp db file")

    def get_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return self.cursor.fetchall()

    def get_column_names(self, table):
        self.cursor.execute(f"PRAGMA table_info({table})")
        return [i[1] for i in self.cursor.fetchall()]
    

