import shutil

def copy_database(source_db, destination_db):
    #データベースをコピーする
    shutil.copyfile(source_db, destination_db)

#メイン処理
if __name__ == "__main__":
    source_db = 'restored_blog.db'
    destination_db = 'blog.db'

    copy_database(source_db, destination_db)
    print(f'Restore completed: {destination_db}')