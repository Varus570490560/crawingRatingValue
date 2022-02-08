import pymysql


def export_to_database(game_id, value):
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy', autocommit=True)
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    try:
        cur.execute("UPDATE `app` SET `game_rating` = %s WHERE `id` = %s", (value, game_id))
        print(game_id, " ", value, " to database Successful")
    except pymysql.Error as e:
        print(e)
    cur.close()
    db.close()


def deal_data():
    with open('./response_app_id/app_id2.txt', 'r') as f2:
        for data in f2.readlines():
            id_str = ""
            id_begin_index = 0
            end_index = data.find(' ') - 1
            i = id_begin_index
            while i <= end_index:
                id_str += data[i]
                i += 1
            rating_str = ""
            rating_str += str(data[len(data) - 4])
            rating_str += str(data[len(data) - 3])
            rating_str += str(data[len(data) - 2])
            export_to_database(int(id_str), float(rating_str))
    with open('./response_app_id/app_id.txt', 'r') as f2:
        for data in f2.readlines():
            id_str = ""
            id_begin_index = 0
            end_index = data.find(' ') - 1
            i = id_begin_index
            while i <= end_index:
                id_str += data[i]
                i += 1
            rating_str = ""
            rating_str += str(data[len(data) - 4])
            rating_str += str(data[len(data) - 3])
            rating_str += str(data[len(data) - 2])
            export_to_database(int(id_str), float(rating_str))
