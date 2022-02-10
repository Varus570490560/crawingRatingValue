import requests
import string_proc
import connect_database


def search(apps):
    db = connect_database.open_database_jojoy()
    for app in apps:
        slug = string_proc.slug_proc(app[2])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get("https://www.ign.com/games/" + slug, headers=headers)
        rating = string_proc.find_value(str(response.content))
        if rating != -1:
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' Successfully!!! Rating Value = ' + str(rating))
            connect_database.update_app_set_ign_star(db=db, app_id=app[0], star=rating)
        else:
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' No found rating')
            failed_log = open('./ign_app_craw_failed/'+str(app[0]) + ' ' + app[1], 'w')
            failed_log.write(str(response.content))
            failed_log.flush()
            failed_log.close()
    connect_database.close_database(db)
