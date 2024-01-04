#!/usr/bin/python3
""" uses REST API, for a given employee ID, returns information about his/her
TODO list progress and writes it to a file in json format
"""

if __name__ == '__main__':
    import requests
    import sys
    import json

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    payload = {'userId': employee_id}
    response = requests.get(url + 'todos', params=payload)
    user = requests.get(url + f"users/{employee_id}").json()
    todos = response.json()
    name = user.get('username')
    file = f'{employee_id}.json'
    with open(file, 'w', ) as jsonfile:
        json.dump({employee_id: [{
            "task": todo.get('title'),
            "completed": todo.get("completed"),
            "username": name
            } for todo in todos]}, jsonfile)
