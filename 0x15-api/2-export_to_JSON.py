#!/usr/bin/python3
"""
   This module defines a function that, using a REST API, for a given
   employee ID, returns information about his/her TODO list progress.
"""
import csv
import json
import requests
import sys


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
                cm_tasks.append(td.get("title"))
        num_cm_tasks = len(cm_tasks)
        num_tasks = len(tds)
        print("Employee {} is done with tasks({}/{}):".format(
            e_name, num_cm_tasks, num_tasks))
        for task in cm_tasks:
            print("\t {}".format(task))
    else:
        print("Error: Unable to fetch TODO list for employee {}".format(
            employee_id))


def write_to_csv(employee_id):
    """ This is a function definition"""
    api_url = "https://jsonplaceholder.typicode.com/"
    api_user = "{}users/{}".format(api_url, employee_id)
    api_user_td = "{}todos".format(api_url)
    u_response = requests.get(api_user)
    td_response = requests.get(api_user_td, params={"userId": employee_id})
    if td_response.status_code == 200:
        tds = td_response.json()
        e_name = u_response.json().get("username")
        with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            [writer.writerow(
                [employee_id, e_name, td.get("completed"), td.get("title")]
             ) for td in tds]

    else:
        print("Error: Unable to fetch TODO list for employee {}".format(
            employee_id))

def write_to_json(employee_id):
    """ This is a function definition"""
    api_url = "https://jsonplaceholder.typicode.com/"
    api_user = "{}users/{}".format(api_url, employee_id)
    api_user_td = "{}todos".format(api_url)
    u_response = requests.get(api_user)
    td_response = requests.get(api_user_td, params={"userId": employee_id})
    if td_response.status_code == 200:
        tds = td_response.json()
        e_name = u_response.json().get("username")
        with open("{}.json".format(employee_id), "w") as jsonfile:
            json.dump({employee_id: [{
                "task": td.get("title"),
                "completed": td.get("completed"),
                "username": e_name
            } for td in tds]}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        e_id = int(sys.argv[1])
        write_to_json(e_id)
