#!/usr/bin/python3
"""
   This module defines a function that, using a REST API, for a given
   employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys
import csv


def get_employee_todo_progress(employee_id):
    """ This is a function definition"""
    api_url = "https://jsonplaceholder.typicode.com/"
    api_user = "{}users/{}".format(api_url, employee_id)
    api_user_td = "{}todos".format(api_url)

    u_response = requests.get(api_user)
    td_response = requests.get(api_user_td, params={"userId": sys.argv[1]})
    if td_response.status_code == 200:
        tds = td_response.json()
        e_name = u_response.json().get("name")
        cm_tasks = []
        for td in tds:
            if td.get("completed"):
                cm_tasks.append(td)
        num_cm_tasks = len(cm_tasks)
        num_tasks = len(tds)

        csv_filename = "{}.csv".format(employee_id)
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in cm_tasks:
                writer.writerow({
                    'USER_ID': employee_id,
                    'USERNAME': e_name,
                    'TASK_COMPLETED_STATUS': task.get("completed"),
                    'TASK_TITLE': task.get("title")
                })

        print("Employee {} is done with tasks({}/{}):".format(
            e_name, num_cm_tasks, num_tasks))
        for task in cm_tasks:
            print("\t {}".format(task.get("title")))
        print("Data exported to {}".format(csv_filename))
    else:
        print("Error: Unable to fetch TODO list for employee {}".format(
            employee_id))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
