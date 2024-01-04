#!/usr/bin/python3
""" uses REST API, for a given employee ID, returns information about his/her
TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    payload = {'userId': employee_id}
    response = requests.get(url + 'todos', params=payload)
    user = requests.get(url + f"users/{employee_id}").json()
    todos = response.json()
    tsk_done = [td.get('title') for td in todos if td.get('completed') is True]
    name = user.get('name')
    total = len(todos)
    print(f'Employee {name} is done with tasks({len(tsk_done)}/{total})')
    [print(f"\t {task}") for task in tsk_done]
