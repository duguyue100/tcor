"""Task List.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from tcor.task import Task


class TaskList(object):
    """Task List."""
    
    def __init__(self, task_list_dict=None, task_list_json=None):
        """Initialize TaskList Object.

        Parameters
        ----------
        task_list_dict : dict
            task list dictionary
        task_list_json : str
            task list json string
        """
        self.task_list_dict = task_list_dict        
        self.task_list_json = task_list_json

        self.man_fields = ["task-list", "task-list-name",
                           "task-group-name", "task-list-id",
                           "task-list-time"]
        self.opt_fields = ["task-list-keys", "task-list-order",
                           "task-list-notes"]

        if self.task_list_dict is None and self.task_list_json is not None:
            self.task_list_dict = self._parse_task_list_json(task_list_json)
            self.valid_task_list = self.is_valid()

        if self.task_list_dict is None:
            self.valid_task_list = False
        else:
            self.valid_task_list = self.is_valid()

        if self.valid_task_list is False:
            self.task_list_dict = {
                "task-list-name": "",
                "task-group-name": "",
                "task-list-id": "0",
                "task-list-time": "0000-00-00",
                "task-list": []
            }
            self.valid_task_list = self.is_valid()

    def _parse_task_list_json(self, task_list_json):
        """Parse task list json string.

        Parameters
        ----------
        task_list_json : str
            the task list json string

        Returns
        -------
        task_list_dict : dict
            the task list dictionary object
        """
        try:
            return json.loads(task_list_json)
        except SyntaxError:
            return None

    def _check_task(self, task_list_dict):
        """Check if task list is valid.

        Parameters
        ----------
        task_list_dict : dict
            the task list dictionay

        Returns
        -------
        valid_flag : bool
            flag that indicates if the task list is valid
        """
        if task_list_dict is None:
            return False
        
        for field in self.man_fields:
            if field not in task_list_dict:
                return False

        return True

    def is_valid(self):
        """check class task list."""
        return self._check_task(self.task_list_dict)

    def set_task_list_dict(self, task_list_dict):
        """Set task list dictionary.

        Parameters
        ----------
        task_list_dict : dict
            task list dictionary
        """
        if task_list_dict is not None:
            self.task_list_dict = task_list_dict
        else:
            self.task_list_dict = None

    def get_task_dict(self):
        """Get task list dictionary.

        Returns
        -------
        task_list_dict : dict
            return a task list dictionary
        """
        if self.task_list_dict is not None:
            return self.task_list_dict 
        else:
            return None

    def set_task_list_json(self, task_list_json):
        """Set task list json.

        Parameters
        ----------
        task_list_json : str
            task json list string
        """
        try:
            self.task_list_dict = json.loads(task_list_json)
            self.task_list_json = task_list_json
        except SyntaxError:
            self.task_list_json = None

        if task_list_json is None:
            self.task_list_json = task_list_json

    def get_task_list_json(self):
        """Get task list json.

        Returns
        -------
        task_list_json : str
            task json list string
        """
        if self.task_list_json is None:
            if self.task_list_dict is None:
                return None
            else:
                return json.dumps(self.task_list_dict)
        else:
            return self.task_list_json
