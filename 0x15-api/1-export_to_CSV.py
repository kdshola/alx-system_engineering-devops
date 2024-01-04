#!/usr/bin/python3
""" uses REST API, for a given employee ID, returns information about his/her
TODO list progress and writes it to a file in csv format
"""

if __name__ == '__main__':
    import requests
    import sys
    import csv

    url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]
    payload = {'userId': employee_id}
    response = requests.get(url + 'todos', params=payload)
    user = requests.get(url + f"users/{employee_id}").json()
    todos = response.json()
    name = user.get('username')
    file = f'{employee_id}.csv'
    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csvwriter.writerow(
            [employee_id, name, todo.get('completed'), todo.get('title')]
            ) for todo in todos]
