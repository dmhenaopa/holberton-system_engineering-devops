#!/usr/bin/python3
"""
   Python script that export data in the JSON format
"""
import csv
import json
import requests

if __name__ == '__main__':

    url_all_users = "https://jsonplaceholder.typicode.com/users/"
    response_all_users = requests.get(url_all_users)
    if response_all_users.status_code == 200:
        json_dict_all_users = json.loads(response_all_users.text)
        json_dict = {}
        for user in json_dict_all_users:
            user_id_param = user.get('id')
            username = user.get('username')

            url_todos = ("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(user_id_param))
            response_todos = requests.get(url_todos)

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
            json_dict.update({user_id_param: json_list})

            json_string = json.dumps(json_dict)
            json_file = open('todo_all_employees.json', mode='a')
            json_file.write(json_string)
        json_file.close()
