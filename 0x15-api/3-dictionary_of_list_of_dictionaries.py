#!/usr/bin/python3
""" uses REST API, for all employees, returns information about all their
TODO list progress and writes it to a file in json format
"""

if __name__ == '__main__':
    import requests
    import json

    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()
    file = 'todo_all_employees.json'
    with open(file, 'w', ) as jsonfile:
        json.dump({user.get('id'): [{
            "username": user.get('username'),
            "task": todo.get('title'),
            "completed": todo.get("completed")
            } for todo in requests.get(
                url + 'todos', params={'userId': user.get('id')}).json()]
            for user in users}, jsonfile)
