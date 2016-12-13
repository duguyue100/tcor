"""Test Task.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""
from __future__ import print_function
from tcor.task import Task

task_dict = {
    "name": "test task",
    "time": "2016-12-13",
    "id" : "1"
}

task_json = ('{'
             '"task_name": "test task",'
             '"task_notes": "This is a test json"'
             '}')

task = Task(task_dict=task_dict)

print (task.valid_task)
print (type(task.task_dict))
print (task.task_dict)
print (task.get_task_json())
