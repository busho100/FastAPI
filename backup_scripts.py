import sqlite3


def backup_database(origin_db, backup_db):
    #データベースをバックアップする
    conn = sqlite3.connect(origin_db)
    with open(backup_db, 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
    conn.close()

#メイン処理
if __name__=="__main__":
    origin_db = 'blog.db'
    backup_db = 'backup.db'

    backup_database(origin_db, backup_db)
    print(f'Backup completed: {backup_db}')