import requests
import csv
import json
import pandas

'''The csv file is formatted to the expected csv format be worked on.
    -The fields are mapped to the right ecs fields'''

def HandlingFile(csvfile, jsonfile, fieldnames):
    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile, indent=4)
        jsonfile.write(',\n')
    pass


if __name__ == "__main__":
    # wine_data = pandas.read_csv('data/files.csv', sep=';', header=None)
    # wine_data.to_csv("data/files.csv", index=False, header=False)
    csvfile = open('data/files.csv', 'r')
    jsonfile = open('data/file.json', 'w')
    fieldnames = (
        "[id]", "[source][ip]", "[host][ip]", "[host][id]", "[network][protocol]", "[source]", "[depth]", "[analyzers]",
        "[http][resopnse][mime_type]", "[file][name]",
        "[event][duration]", "[local_orig]", "[is_orig]", "[seen_bytes]", "[total_bytes]", "[missing_bytes]",
        "[overflow_bytes]", "[timedout]",
        "[parent_uid]", "[file][hash][md5]", "[file][hash][sha1]", "[file][hash][sha256]", "[labels][extracted]")

    HandlingFile(csvfile, jsonfile, fieldnames)
