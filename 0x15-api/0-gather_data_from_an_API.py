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
    done_tasks = []
    done = 0
    for task in todo_data:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1
    print("Employee {} is done with tasks {}/{}:"
          .format(employee_name, done, len(todo_data)))
    for tasks in done_tasks:
        print("\t {}".format(tasks.get('title')))
