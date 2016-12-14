"""Task Group.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import json

from tcor.task import Task
from tcor.tasklist import TaskList


class TaskGroup(object):
    """Task Group."""

    def __init__(self, task_group_dict=None, task_group_json=None):
        """Initialize TaskGroup.

        Parameters
        ----------
        task_group_dict : dict
            The task group dictionary
        task_group_json : str
            The task group string
        """
        self.task_group_dict = task_group_dict
        self.task_group_json = task_group_json
        self.man_fields = ["task-group-name", "task-group-time",
                           "task-group-id", "task-lists"]
        self.opt_fields = ["task-group-notes", "task-group-keys"]

        if self.task_group_dict is None and self.task_group_json is not None:
            self.task_group_dict = self._parse_task_group_json(
                self.task_group_json)
            self.valid_group_task = self.is_group_valid()

        if self.task_group_dict is None:
            self.valid_group_task = False
        else:
            self.valid_group_task = self.is_group_valid()

        if self.valid_group_task is False:
            self.task_group_dict = {
                "task-group-name": "",
                "task-group-id": "0",
                "task-group-time": "0000-00-00",
                "task-lists": []
            }
            self.valid_group_task = self.is_group_valid(self.task_group_dict)

    def _parse_task_group_json(self, task_group_json):
        """Parse task json group string.

        Parameters
        ----------
        task_group_json : str
            the task group json string

        Returns
        -------
        task_group_dict : dict
            the task group dictionary object
        """
        try:
            return json.loads(task_group_json)
        except SyntaxError:
            return None

    def _check_group_task(self, task_group_dict):
        """Check if task group is valid.

        Parameters
        ----------
        task_group_dict : dict
            the task group dictionay

        Returns
        -------
        valid_group_flag : bool
            flag that indicates if the task group is valid
        """
        if task_group_dict is None:
            return False

        for field in self.man_fields:
            if field not in task_group_dict:
                return False

        return True

    def is_group_valid(self):
        """check class task group list."""
        return self._check_group_task(self.task_group_dict)

    def add_task_list(self, task_list):
        """Add a task list.

        Parameters
        ----------
        task_list : tcor.tasklist.TaskList
            the task list
        """
        if task_list.valid_task_list is True:
            self.task_group_dict["task-lists"].append(task_list)

    def set_task_group_dict(self, task_group_dict):
        """Set task group dictionary.

        Parameters
        ----------
        task_group_dict : dict
            task group dictionary
        """
        if task_group_dict is not None:
            self.task_group_dict = task_group_dict
        else:
            self.task_group_dict = None

    def get_task_group_dict(self):
        """Get task group dictionary.

        Returns
        -------
        task_group_dict : dict
            return a task group dictionary
        """
        if self.task_group_dict is not None:
            return self.task_group_dict
        else:
            return None

    def set_task_group_json(self, task_group_json):
        """Set task group json.

        Parameters
        ----------
        task_group_json : str
            task json group string
        """
        try:
            self.task_group_dict = json.loads(task_group_json)
            self.task_group_json = task_group_json
        except SyntaxError:
            self.task_group_json = None

        if self.task_json is None:
            self.task_group_json = task_group_json

    def get_task_group_json(self):
        """Get task group json.

        Returns
        -------
        task_group_json : str
            task json group string
        """
        if self.task_group_json is None:
            if self.task_group_dict is None:
                return None
            else:
                return json.dumps(self.task_group_dict)
        else:
            return self.task_group_json
