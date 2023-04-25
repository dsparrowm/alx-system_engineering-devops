#!/usr/bin/python3
"""This module works on Api calls"""

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
    user_info = {}
    filename = "{}.json".format(user_id)
    tasks = []
    for todo in todo_data:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = data.get('username')
        tasks.append(task)
    user_info[user_id] = tasks
    with open(filename, 'w') as jsonfile:
        json.dump(user_info, jsonfile)
