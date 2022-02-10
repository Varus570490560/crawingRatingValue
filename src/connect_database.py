import pymysql


def select_app_id_name_slug(db):
    cur = db.cursor()
    cur.execute(
        "SELECT `id`,`title`,`slug` from `app`")
    res = cur.fetchall()
    cur.close()
    return res


def open_database_jojoy():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy', autocommit=True)
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    return db


def close_database(db):
    db.close()


def update_app_set_ign_star(db, app_id, star):
    cur = db.cursor()
    try:
        cur.execute('UPDATE `app` SET `ign_star` = %s WHERE `id` = %s', (star, app_id))
        print('id = ', app_id, ' star = ', star)
        print('database update successfully!!!')
    except pymysql.Error as e:
        print(e)
    cur.close()


def update_app_set_mc_star(db, app_id, star):
    cur = db.cursor()
    try:
        cur.execute('UPDATE `app` SET `mc_star` = %s WHERE `id` = %s', (star, app_id))
        print('id = ', app_id, ' star = ', star)
        print('database update successfully!!!')
    except pymysql.Error as e:
        print(e)
    cur.close()


def update_app_set_mc_user_star(db, app_id, star):
    cur = db.cursor()
    try:
        cur.execute('UPDATE `app` SET `mc_user_star` = %s WHERE `id` = %s', (star, app_id))
        print('id = ', app_id, ' star = ', star)
        print('database update successfully!!!')
    except pymysql.Error as e:
        print(e)
    cur.close()
