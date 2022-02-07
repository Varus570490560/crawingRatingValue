import pymysql


def select_app_id_name_slug():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT `id`,`title`,`slug` from `app`")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res
