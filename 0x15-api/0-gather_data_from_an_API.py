#!/usr/bin/python3
"""
   Python script that returns information about
   his/her TODO list progress
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    user_id_param = argv[1]
    url_user = ("https://jsonplaceholder.typicode.com/users/{}"
                .format(user_id_param))
    url_todos = ("https://jsonplaceholder.typicode.com/users/{}/todos"
                 .format(user_id_param))

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    if response_user.status_code == 200:
        json_dict_user = json.loads(response_user.text)
        user_name = json_dict_user.get('name')

    if response_todos.status_code == 200:
        completed_tasks = 0
        total_tasks = 0
        json_dict_todos = json.loads(response_todos.text)
        for element in json_dict_todos:
            if element.get('completed'):
                completed_tasks += 1
                total_tasks += 1
            else:
                total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user_name, completed_tasks, total_tasks))

    for element in json_dict_todos:
        if element.get('completed'):
            print("\t {}".format(element.get('title')))
