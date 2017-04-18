#!/usr/bin/python3
"""
Export data to JSON format
"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)
    usr = requests.get(user).json()
    todo = 'https://jsonplaceholder.typicode.com/todos'
    todo_list = requests.get(todo).json()
    data = {}
    new_list = []
    usr_name = usr.get("username")
    with open(emp_id + '.json', 'w') as json_f:
        for i in todo_list:
            my_dict = {}
            usr_id = i.get("userId")
            task_name = i.get("title")
            status = i.get("completed")
            if emp_id == str(usr_id):
                my_dict.update({"task": task_name, "completed": status,
                                "username": usr_name})
                new_list.append(my_dict)
        data[emp_id] = new_list
        json.dump(data, json_f)
