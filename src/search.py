import requests
import urllib
import string_proc
import json


def search(apps):
    file_name = '../response_app_id/app_id.txt'
    log = open(file_name, 'w')
    for app in apps:
        slug = string_proc.slug_proc(app[2])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get("https://www.ign.com/games/"+slug, headers=headers)
        rating=string_proc.find_value(str(response.content))
        if rating!=-1:
            log.write(str(app[0]) + ' ' + app[1] + ' ' + app[2] + str(rating))
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' Successfully!!! Rating Value = '+str(rating))
            log.write('\n')
            log.flush()
        else:
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2]+'No found rating')
    log.close()
