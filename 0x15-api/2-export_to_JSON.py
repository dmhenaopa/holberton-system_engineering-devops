#!/usr/bin/python3
"""
   Python script that export data in the CSV format
"""
import csv
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
        username = json_dict_user.get('username')

    if response_todos.status_code == 200:
        json_dict_todos = json.loads(response_todos.text)

        inner_dict = {}
        json_list = []

        for element in json_dict_todos:
            completed_status = element.get('completed')
            task_title = element.get('title')

            inner_dict = {"task": task_title,
                          "completed": completed_status,
                          "username": username}

            json_list.append(inner_dict)

        json_dict = {user_id_param: json_list}
        filename = '{}.json'.format(user_id_param)
        json_string = json.dumps(json_dict)
        json_file = open(filename, mode='w')
        json_file.write(json_string)
        json_file.close()
