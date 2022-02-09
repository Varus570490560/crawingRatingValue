import connect_database
import muti_thread

if __name__ == '__main__':
    apps = connect_database.select_app_id_name_slug()
    app_lst = muti_thread.tuple_cut(apps, 1000)
    muti_thread.muti_thread_craw_at_ign(apps_lst=app_lst)
