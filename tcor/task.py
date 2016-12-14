"""Central Task class.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

import json


class Task(object):
    """Describe a task object."""

    def __init__(self, task_dict=None, task_json=None):
        """Initialize task.

        Parameters
        ----------
        task_dict : dict
            The task dictionary
        task_json : str
            The task string
        """
        self.task_dict = task_dict
        self.task_json = task_json
        self.man_fields = ["task-name", "task-time", "task-id",
                           "task-list-name"]
        self.opt_fields = ["task-notes", "task-order", "task-keys"]

        if self.task_dict is None and self.task_json is not None:
            self.task_dict = self._parse_task_json(self.task_json)
            self.valid_task = self.is_valid()

        if self.task_dict is None: 
            self.valid_task = False
        else:
            self.valid_task = self.is_valid()

        if self.valid_task is False:
            self.task_dict = {
                "task-name": "",
                "task-list-name": "",
                "task-id": "0",
                "task-time": "0000-00-00"
            }
            self.valid_task = self.is_valid(self.task_dict)

    def _parse_task_json(self, task_json):
        """Parse task json string.

        Parameters
        ----------
        task_json : str
            the task json string

        Returns
        -------
        task_dict : dict
            the task dictionary object
        """
        try:
            return json.loads(task_json)
        except SyntaxError:
            return None

    def _check_task(self, task_dict):
        """Check if task is valid.

        Parameters
        ----------
        task_dict : dict
            the task dictionay

        Returns
        -------
        valid_flag : bool
            flag that indicates if the task is valid
        """
        if task_dict is None:
            return False
        
        for field in self.man_fields:
            if field not in task_dict:
                return False

        return True

    def is_valid(self):
        """check class task list."""
        return self._check_task(self.task_dict)

    def set_task_dict(self, task_dict):
        """Set task dictionary.

        Parameters
        ----------
        task_dict : dict
            task dictionary
        """
        if task_dict is not None:
            self.task_dict = task_dict
        else:
            self.task_dict = None

    def get_task_dict(self):
        """Get task dictionary.

        Returns
        -------
        task_dict : dict
            return a task dictionary
        """
        if self.task_dict is not None:
            return self.task_dict 
        else:
            return None

    def set_task_json(self, task_json):
        """Set task json.

        Parameters
        ----------
        task_json : str
            task json string
        """
        try:
            self.task_dict = json.loads(task_json)
            self.task_json = task_json
        except SyntaxError:
            self.task_json = None

        if task_json is None:
            self.task_json = task_json

    def get_task_json(self):
        """Get task json.

        Returns
        -------
        task_json : str
            task json string
        """
        if self.task_json is None:
            if self.task_dict is None:
                return None
            else:
                return json.dumps(self.task_dict)
        else:
            return self.task_json
