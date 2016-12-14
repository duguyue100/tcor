"""GUI Related functions.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from PyQt5 import QtCore, QtWidgets


class TodoWidget(QtWidgets.QWidget):
    """A Todo List Widget."""

    def __init__(self, label_name):
        """Init a todo widget."""
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.list_name = QtWidgets.QLabel(label_name)
        self.todo_list = QtWidgets.QTableWidget()

        self.layout.addWidget(self.list_name)
        self.layout.addWidget(self.todo_list)


class TaskCard(QtWidgets.QWidget):
    """A Task Card."""

    def __init__(self, task):
        """Init a task widget.

        Parameters
        ----------
        task : tcor.task.Task
            A Task Object.
        """
        self.task = task

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.task_name = QtWidgets.QLabel(self.task["task-name"])

        self.layout.addWidget(self.task_name)
