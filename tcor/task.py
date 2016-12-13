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
            The task dictionary.
        """
        self.task_dict = task_dict
        self.task_json = task_json

        if self.task_dict is None and self.task_json is not None:
            self.task_dict = self._parse_task_json(self.task_json)
            self.valid_task = True

        if self.task_dict is None: 
            self.valid_task = False
        else:
            self.valid_task =True

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
        return json.loads(task_json)

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
