#!/usr/bin/python3
"""export data in the JSON format.
   The module sends a request to an API
"""
import json
import requests
import sys


URL = "https://jsonplaceholder.typicode.com"
"""Link to API"""


if __name__ == "__main__":
    users = requests.get("{}/users/".format(URL))
    todos = requests.get("{}/todos/".format(URL))
    if (users.status_code == requests.codes.ok and
            todos.status_code == requests.codes.ok):
        file_name = "todo_all_employees.json"
        all_user_todo = {}
        for user in users.json():
            userid = user.get('id')
            username = user.get('username')
            user_todos = []
            for todo in todos.json():
                if userid == todo.get('userId'):
                    task = {}
                    task['username'] = username
                    task['task'] = todo.get('title')
                    task['completed'] = todo.get('completed')
                    user_todos.append(task)
                    all_user_todo[userid] = user_todos

        with open(file_name, 'w') as fs:
            json.dump(all_user_todo, fs)
