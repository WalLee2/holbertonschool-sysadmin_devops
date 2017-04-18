#!/usr/bin/python3
"""
Gather data from an API that uses REST API
"""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1])
    usr = requests.get(user).json()
    todo_list = 'https://jsonplaceholder.typicode.com/todos'
    todo = requests.get(todo_list).json()
    csv_file = open(sys.argv[1] + '.csv', 'w')
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    USERNAME = usr.get("username")
    for a in todo:
        if emp_id == str(a.get("userId")):
            T_C_S = a.get("completed")
            T_Title = a.get("title")
            wr.writerow([emp_id, USERNAME, T_C_S, T_Title])
