#!/usr/bin/python3
"""
Export data to JSON format
"""
import json
import requests

if __name__ == "__main__":
    user = 'https://jsonplaceholder.typicode.com/users'
    usr = requests.get(user).json()
    todo = 'https://jsonplaceholder.typicode.com/todos'
    todo_list = requests.get(todo).json()
    with open('todo_all_employees.json', 'w') as json_f:
        data = {}
        new_list = []
        usr_nameId = {}
        for a in usr:
            usr_nameId.update({a.get("id"): a.get("username")})
        for i in todo_list:
            my_dict = {}
            todo_id = i.get("userId")
            task_name = i.get("title")
            status = i.get("completed")
            if todo_id in usr_nameId.keys():
                my_dict.update({"task": task_name, "completed": status,
                                "username": usr_nameId[todo_id]})
            new_list.append(my_dict)
            data[todo_id] = new_list
        json.dump(data, json_f)
