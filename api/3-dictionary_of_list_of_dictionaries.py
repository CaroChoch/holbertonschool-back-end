#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the JSON format.
Records all tasks from all employees
"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


def api():
    """
    Return API data
    """

    # User information
    user_response = requests.get(f"{API_URL}/users/").json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos").json()
    
    # Create a dictionary for all users
    dictionary_user = {}

    for task in todo_response:
        user_id = task['userId']
 
        if user_id not in dictionary_user:
            dictionary_user[user_id] = []
        dictionary_user[user_id].append({
            "username": next(user[
                'username'] for user in user_response if user['id'] == user_id),
            "task": task['title'],
            "completed": task['completed']
        })

    # Write to JSON file
    with open("todo_all_employees.json", 'w') as jsonfile:
        jsonfile.write(json.dumps(dictionary_user))
        jsonfile.close()


if __name__ == "__main__":
    api()
