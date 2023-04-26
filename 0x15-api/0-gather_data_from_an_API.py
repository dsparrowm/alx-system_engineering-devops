#!/usr/bin/python3
"""Returns information about his/her TODO list progress.
   The module Takes in a user id, sends a request to an API
    and displays the response
 """
import requests
import sys


URL = "https://jsonplaceholder.typicode.com"
"""Link to API"""


if __name__ == "__main__":
    if (len(sys.argv) > 1 and
            isinstance(int(sys.argv[1]), int)):
        user_id = int(sys.argv[1])
        user = requests.get("{}/users/{}".format(URL, user_id))
        todos = requests.get("{}/user/{}/todos/".format(URL, user_id))
        if (user.status_code == requests.codes.ok and
                todos.status_code == requests.codes.ok):
            username = user.json().get('name')
            done_tasks = []
            c_tasks = 0
            tasks = 0
            for todo in todos.json():
                task_status = todo.get('completed')
                if task_status is True:
                    c_tasks = c_tasks + 1
                    done_tasks.append(todo)
                tasks = tasks + 1
            print("Employee {} is done with tasks({}/{}):".format(
                   username,
                   c_tasks,
                   tasks))
            for todo in done_tasks:
                print("\t {}".format(todo.get('title')))
