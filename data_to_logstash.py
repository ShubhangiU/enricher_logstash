import json
from datetime import datetime, timedelta
from random import randrange
import requests

"""This function will return a random datetime between two datetime
    objects."""


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


"""For Elastic to be able to perform right functions there has to be the datetime field associated with every record, 
so the belove function takes care of that. """


def format_data(file, d):
    d = {"@timestamp": str(d)}
    format_data = []
    for v in file:
        v.update(d)
        format_data.append(v)
    return format_data


"""The post_data function is basically working to fetch all the data in the json object and posting it to elastic."""


def post_data(d, url):
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8'}
    for i in range(len(d)):
        resp = requests.post(url, data=json.dumps(d[i]),
                             headers=headers)
        print(resp.text)
    pass


if __name__ == "__main__":
    d1 = datetime.strptime('11/23/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('11/25/2020 4:50 AM', '%m/%d/%Y %I:%M %p')
    file = json.load(open('data/file_complete.json'))
    _list = file["data"]
    cred = json.load(open('config/cred.json'))
    url = cred["url_post"]
    d = random_date(d1, d2).strftime('%Y-%m-%dT%H:%M:%SZ')
    data = format_data(_list, d)
    post_data(data, url)
