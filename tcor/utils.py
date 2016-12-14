"""Utility Functions.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from os.path import isfile
import datetime
import json

from tcor.task import Task
from tcor.tasklist import TaskList
from tcor.group import TaskGroup


def create_new_task_group(task_group_name, task_group_time=None,
                          task_group_id=None, task_lists=[],
                          task_group_notes="", task_group_keys=[]):
    """Create a new task group.

    Parameters
    ----------
    task_group_name : str
        the task group name
    task_group_time : str
        the time that the task group created in format of
        %Y-%m-%d %H:%M:%S (TZ%z)
    task_group_id : str
        The ID of the task group in format of
        task_group_name-task_group_time
    task_lists : list
        The list of task lists
    task_group_notes : str
        the optional notes of task group
    task_group_keys : list
        the optional group keys such as "work", "home", etc

    Returns
    -------
    task_group : tcor.group.TaskGroup
        An empty TaskGroup
    """
    if task_group_time is None:
        task_group_time = datetime.datetime.now().strftime(
            "%Y-%m-%d-%H-%M-%S-TZ%z")

    if task_group_id is None:
        task_group_id = task_group_name+"-"+task_group_time

    if not isinstance(task_group_notes, str):
        task_group_notes = ""

    if not isinstance(task_lists, list):
        task_lists = []

    if not isinstance(task_group_keys, list):
        task_group_keys = []

    return TaskGroup(task_group_dict={
            "task-group-name": task_group_name,
            "task-group-time": task_group_time,
            "task-group-id": task_group_id,
            "task-lists": task_lists,
            "task-group-notes": task_group_notes,
            "task-group-keys": task_group_keys
        })


def load_task_group(file_path):
    """Load a valid task group.

    Parameters
    ----------
    file_path : str
        the absolute path of task group

    Returns
    -------
    task_group : tcor.group.TaskGroup
        An loaded task group
    """
    if not isfile(file_path):
        return None

    with open(file_path, "rb") as f:
        try:
            task_group_data = json.load(f)
        except SyntaxError:
            f.close()
            return None
        f.close()

    return TaskGroup(task_group_dict=task_group_data)


def write_task_group(task_group, task_path):
    """Write a valid task group to a path.

    Parameters
    ----------
    task_group : tcor.group.TaskGroup
        A prepared task group
    """
    with open(task_path, "wb") as f:
        if task_group.valid_group_task is True:
            json.dump(task_group, f)
        f.close()


def create_new_task_list(task_list_name, task_group_name,
                         task_list_time=None, task_list_id=None,
                         task_list=[], task_list_notes="",
                         task_list_keys=[]):
    """Create new empty task list.

    Parameters
    ----------
    task_list_name : str
        the task list name
    task_group_name : str
        the task group name it belongs to
    task_list_time : str
        the time that the task list created in format of
        %Y-%m-%d %H:%M:%S (TZ%z)
    task_list_id : str
        The ID of the task list
        task_list_name-task_group_name-task_list_time
    task_list : list
        The list of tasks
    task_list_notes : str
        The optional task list
    task_list_keys : list
        The optional task keys

    Returns
    -------
    task_list : tcor.tasklist.TaskList
        The empty task list
    """
    if task_list_time is None:
        task_list_time = datetime.datetime.now().strftime(
            "%Y-%m-%d-%H-%M-%S-TZ%z")

    if task_list_id is None:
        task_list_id = task_list_name+"-"+task_group_name + \
                       "-"+task_list_time

    if not isinstance(task_list_notes, str):
        task_list_notes = ""

    if not isinstance(task_list, list):
        task_list = []

    if not isinstance(task_list_keys, list):
        task_list_keys = []

    return TaskList(task_list_dict={
            "task-list-name": task_list_name,
            "task-group-name": task_group_name,
            "task-list-id": task_list_id,
            "task-list-time": task_list_time,
            "task-list": task_list,
            "task-list-notes": task_list_notes,
            "task-list-keys": task_list_keys
        })


def create_new_task(task_name, task_list_name, task_time=None, task_id=None,
                    task_notes="", task_order=9999, task_keys=[]):
    """Create a new task.

    Parameters
    ----------
    task_name : str
        The name of the task.
    task_list_name : str
        The name of the parent task list.
    task_time : str
        The time of the event
        %Y-%m-%d %H:%M:%S (TZ%z)
    task_id : str
        The ID of the task:
        task-task_list_name-task_time
    task_notes : str
        the notes of the task
    task_order : int
        The order of the task
    task_keys : list
        The lsit of keys
    """
    if task_time is None:
        task_time = datetime.datetime.now().strftime(
            "%Y-%m-%d-%H-%M-%S-TZ%z")

    if task_id is None:
        task_id = "task-"+task_list_name+"-"+task_time

    if not isinstance(task_notes, str):
        task_notes = ""

    if not isinstance(task_order, int):
        task_order = 9999

    if not isinstance(task_keys, list):
        task_keys = []

    return Task(task_dict={
            "task-name": task_name,
            "task-list-name": task_list_name,
            "task-id": task_id,
            "task-time": task_time,
            "task-notes": task_notes,
            "task-order": task_order,
            "task-keys": task_keys
        })
