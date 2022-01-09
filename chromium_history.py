from chromium_db import ChromeDB

def get_table_restricted(cursor, table, limit):
    cursor.execute(f"SELECT * FROM {table} LIMIT {limit}")
    return cursor.fetchall()

def main():
    db_name = "History"
    with ChromeDB(db_name) as db:
        print(db.get_column_names("downloads"))
        results = get_table_restricted(db.cursor, "urls", 2)
        results2 = get_table_restricted(db.cursor, "keyword_search_terms", 2)
        results3 = get_table_restricted(db.cursor, "downloads", 1)
        print(results, results2, results3)
        
if __name__ == "__main__":
    main()

# urls: (36, 'http://www.hotmail.com/', 'Doorgaan', 3, 3, 13284735067318727, 0)
# keyword_search_terms : (11, 2688, 'stolichnaya', 'stolichnaya')
# downloads : (1, '6d255418-fc86-4f98-be53-9f14b86a715e', 'C:\\Users\\mickl\\Downloads\\VSCodeUserSetup-x64-1.60.2.exe', 'C:\\Users\\mickl\\Downloads\\VSCodeUserSetup-x64-1.60.2.exe', 13277163360970292, 79573720, 79573720, 1, 0, 0, b'', 13277163377949243, 1, 13277163455035178, 0, 'https://code.visualstudio.com/docs/?dv=win', '', 'https://code.visualstudio.com/docs/?dv=win', 'https://code.visualstudio.com/', '', '', '', '"0x8D97DC6685CA594"', 'Wed, 22 Sep 2021 12:42:15 GMT', 'application/octet-stream', 'application/octet-stream')
