#!/usr/bin/python3
"""This module works on Api calls"""

import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    user_id = sys.argv[1]
    api = "https://jsonplaceholder.typicode.com/users"
    base_url = api + "/" + user_id
    response = urllib.request.urlopen(base_url)
    data = json.loads(response.read().decode())
    employee_name = data.get('name')
    todo_url = base_url + "/todos"
    todo_res = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_res.read().decode())
    filename = "{}.csv".format(user_id)
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([user_id, data.get('username'), task.get('completed'), task.get('title')])
