#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


def api():
    """
    Return API data
    """
    # User information
    user_response = requests.get(f"{API_URL}/users/{argv[1]}").json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={argv[1]}").json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_response if task["completed"]]

    # Display progress
    employee_name = user_response["name"]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_response)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    api()
