import requests
import string_proc


def search(apps):
    file_name = './response_app_id/app_id2.txt'
    log = open(file_name, 'w')
    for app in apps:
        slug = string_proc.slug_proc(app[2])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get("https://www.metacritic.com/game/ios/" + slug, headers=headers)
        rating = string_proc.find_value_mc(str(response.content))
        if rating == -1:
            rating = string_proc.find_value_mc_2(str(response.content))
        if rating != -1:
            log.write(str(app[0]) + ' ' + app[1] + ' Rating Value = ' + str(rating))
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' Successfully!!! Rating Value = ' + str(rating))
            log.write('\n')
            log.flush()
        else:
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + 'No found rating')
    log.close()
