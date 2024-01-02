#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    # Fetching the list of users from the API
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    # Fetching the list of TODOs from the API
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    # Dictionary to store TODO information for all employees
    todoAll = {}
    # Iterating through each user to compile their TODO list
    for user in users:
        # List to store tasks for a specific user
        taskList = []
        # Iterating through all TODOs to find tasks associated with the user
        for task in todos:
            if task.get('userId') == user.get('id'):
                # Creating a dictionary for each task
                taskDict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                # Appending task dictionary to the user's task list
                taskList.append(taskDict)
        # Adding the user's task list to the overall dictionary
        todoAll[user.get('id')] = taskList
    # Writing the compiled TODO information for all employees to a JSON file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
