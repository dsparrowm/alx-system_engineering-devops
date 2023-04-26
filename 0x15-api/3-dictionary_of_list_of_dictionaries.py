#!/usr/bin/python3
"""This module works on Api calls"""

import json
import sys
import urllib.request


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    api = "https://jsonplaceholder.typicode.com"
    users_api = api + "/users"
    response = urllib.request.urlopen(users_api)
    data = json.loads(response.read().decode())
    todo_url = api + "/todos"
    todo_res = urllib.request.urlopen(todo_url)
    todo_data = json.loads(todo_res.read().decode())
    users_todo = {}
    for user in data:
        user_id = user.get('id')
        user_name = user.get('username')
        all_user = []
        for todo in todo_data:
            if user_id == todo.get('userId'):
                task = {}
                task['username'] = user_name
                task['task'] = todo.get('title')
                task['completed'] = todo.get('completed')
                all_user.append(task)
        users_todo[user_id] = all_user
    with open(filename, 'w') as jsonfile:
        json.dump(users_todo, jsonfile)
