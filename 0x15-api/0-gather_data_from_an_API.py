#!/usr/bin/python3
"""
   This module defines a function that, using a REST API, for a given
   employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ This is a function definition"""
    # Specify the API endpoint
    api_url = "https://jsonplaceholder.typicode.com/"
    # Specify the API endpoint for users
    api_user = "{}users/{}".format(api_url, employee_id)
    # Specify the API endpoint for the employee's TODO list
    api_user_td = "{}todos".format(api_url)

    u_response = requests.get(api_user)
    td_response = requests.get(api_user_td, params={"userId": sys.argv[1]})
    # Check if the request was successful (status code 200)
    if td_response.status_code == 200:
        # Parse the JSON response
        tds = td_response.json()
        # Extract employee name
        e_name = u_response.json().get("name")
        # Count the number of completed tasks
        cm_tasks = []
        for td in tds:
            if td.get("completed"):
                cm_tasks.append(td.get("title"))
        num_cm_tasks = len(cm_tasks)
        # Calculate the total number of tasks
        num_tasks = len(tds)
        # Display the employee TODO list progress
        print("Employee {} is done with tasks({}/{}):".format(
            e_name, num_cm_tasks, num_tasks))
        # Display the titles of completed tasks
        for task in cm_tasks:
            print("\t{}".format(task))
    else:
        # Display an error message for unsuccessful requests
        print("Error: Unable to fetch TODO list for employee {}".format(
            employee_id))


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        # Get the employee ID from the command-line argument
        employee_id = int(sys.argv[1])
        # Call the function to fetch and display TODO list progress
        get_employee_todo_progress(employee_id)
