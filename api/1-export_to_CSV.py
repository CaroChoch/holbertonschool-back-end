#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the CSV format.
"""
import csv
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

    # Write to CSV file
    with open(f"{USER_ID}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_response:
            writer.writerow([
                user_response['id'],
                user_response['username'],
                task['completed'],
                task['title']
            ])


if __name__ == "__main__":
    api()
