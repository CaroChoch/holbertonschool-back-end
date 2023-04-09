#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'


def api():
    """
    Return API data
    """
    USER_ID = argv[1]

    # User information
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    # Todo list for the given user
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    # Create a list of dictionary
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_response['username']
            }
            for task in todo_response
        ]
    }

    # Write to JSON file
    with open("{}.json".format(USER_ID), 'w') as jsonfile:
        jsonfile.write(json.dumps(data))
        jsonfile.close()


if __name__ == "__main__":
    api()
