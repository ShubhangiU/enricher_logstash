import requests
import json
from urllib.parse import urljoin
from itertools import chain


def greynoise_ip_enrichment(v, k):
    url = urljoin("https://api.greynoise.io/v3/community/", v)

    headers = {
        'key': '{{' + k + '}}'
    }
    return requests.request("GET", url, headers=headers).json()


if __name__ == "__main__":
    cred = open('config/cred.json')
    file = open('data/file.json')
    json_data = json.load(file)
    cred_ = json.load(cred)
    greynoise_data = []
    _list = json_data['data']
    api_key = cred_['api_key']
    for var in _list:
        for k, v in var.items():
            if k == "[source][ip]":
                greynoise_data.append(greynoise_ip_enrichment(v, api_key))

    for i in range(len(_list)):
        z = _list[i]
        x = greynoise_data[i]
        y = dict(chain.from_iterable(d.items() for d in (z, x)))
        with open('data/file_complete.json', 'a') as fc:
            json.dump(y, fc, indent=4)
            fc.write(',\n')
