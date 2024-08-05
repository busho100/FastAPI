import sqlite3

def restore_database(backup_db, restored_db):
    #データベースをリストアする
    conn = sqlite3.connect(restored_db)
    with open(backup_db, 'r') as f:
        sql = f.read()
        conn.executescript(sql)
    conn.close()

#メイン処理
if __name__ == "__main__":
    backup_db = 'backup.db'
    restored_db = 'restored_blog.db'

    restore_database(backup_db, restored_db)
    print(f'Restore completed: {restored_db}')