"""Test Task.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""
from __future__ import print_function
from tcor.task import Task

task_dict = {
    "task_name": "test task",
    "task_notes": "This is a test task"
}

task_json = ('{'
             '"task_name": "test task",'
             '"task_notes": "This is a test json"'
             '}')

task = Task()

print (type(task.task_dict))
print (task.task_dict)
