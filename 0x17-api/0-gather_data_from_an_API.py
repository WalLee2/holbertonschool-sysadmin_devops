#!/usr/bin/python3
"""
Gather data from an API that uses REST API
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/2'
    usr = requests.get(user).json()
    todo_list = 'https://jsonplaceholder.typicode.com/todos'
    todo = requests.get(todo_list).json()
    count = total = 0
    my_list = []
    for a in todo:
        t = dict(a)
        if str(t.get("userId")) == emp_id:
            if t.get("completed") is True:
                count += 1
                my_list.append(t.get("title"))
            if t.get("completed") is False or\
               t.get("completed") is True:
                total += 1
    print("Employee {} is done with tasks({}/{}):".
          format(str(usr.get("name")), count, total))
    for i in my_list:
        conv = str(i)
        print("\t{}".format(conv))
