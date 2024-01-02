#!/usr/bin/python3
"""
   This module defines a function that, using a REST API, for a given
   employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
       This defines the function that interacts with the API to
       retrieve the todo list fot the specified employee_id
    """
    # Specify the API endpoint for the employee's TODO list
    api_url = f'https://jsonplaceholder.typicode.com/todos/1'

    # Send a GET request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        todos = response.json()

        # Extract employee name
        employee_name = todos[0]['username']

        # Count the number of completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_tasks = len(todos)

        # Display the employee TODO list progress
        print("Employee {} is done with tasks ({}/{}):".format(
            employee_name, num_completed_tasks, total_tasks))
        print(f"\t{employee_name}: {num_completed_tasks}/{total_tasks}")

        # Display the titles of completed tasks
        for task in completed_tasks:
            print(f"\t\t{task['title']}")
    else:
        # Display an error message for unsuccessful requests
        print(f"Error: Unable to fetch TODO list for employee {employee_id}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        # Get the employee ID from the command-line argument
        employee_id = int(sys.argv[1])
        # Call the function to fetch and display TODO list progress
        get_employee_todo_progress(employee_id)
