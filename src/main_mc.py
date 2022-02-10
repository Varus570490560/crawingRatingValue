import connect_database
import muti_thread

if __name__ == '__main__':
    db = connect_database.open_database_jojoy()
    apps = connect_database.select_app_id_name_slug(db=db)
    connect_database.close_database(db=db)
    app_lst = muti_thread.tuple_cut(apps, 1000)
    muti_thread.muti_thread_craw_at_mc(apps_lst=app_lst)
