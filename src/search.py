import requests
import urllib
import json


def search(apps):
    file_name = '../response_app_id/app_id.txt'
    log = open(file_name, 'w')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 ',
        'authority': 'mollusk.apis.ign.com',
        'method': 'GET',
        'path': '/graphql?operationName=SearchObjectsByName&variables=%7B%22term%22%3A%22456%22%2C%22count%22%3A20%2C%22sortBy%22%3A%22updatedAt%22%2C%22sortOrder%22%3A%22desc%22%2C%22region%22%3A%22us%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22a44ef5a9532d087ac58e59c5c6a4d3f1f219550c88c86d3b16998973f293f123%22%7D%7D',
        'scheme': 'https',
        'accept': '* / *',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'apollographql-client-name': 'kraken'
    }
    for app in apps:
        variables = urllib.parse.quote(app[1])
        params = {
            "operationName": "SearchObjectsByName",
            "variables": variables,
            "extensions": '%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22a44ef5a9532d087ac58e59c5c6a4d3f1f219550c88c86d3b16998973f293f123%22%7D%7D'
        }
        # response = requests.get(headers=headers, params=params, url='https://mollusk.apis.ign.com/graphql')
        url = 'https://mollusk.apis.ign.com/graphql?operationName=SearchObjectsByName&variables=%7B%22term%22%3A%22' + variables + '%22%2C%22count%22%3A20%2C%22sortBy%22%3A%22updatedAt%22%2C%22sortOrder%22%3A%22desc%22%2C%22region%22%3A%22us%22%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22a44ef5a9532d087ac58e59c5c6a4d3f1f219550c88c86d3b16998973f293f123%22%7D%7D'
        response = requests.get(headers=headers,
                                url=url)
        if response is None:
            continue
        response_json = response.json()
        if len(response_json['data']['searchObjectsByName']['objects']) > 0:
            log.write(str(app[0]) + ' ' + app[1] + ' ' + app[2])
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' Successfully')
            log.write('\n')
            log.flush()
        else:
            print(str(app[0]) + ' ' + app[1] + ' ' + app[2] + ' Failed')
    log.close()
