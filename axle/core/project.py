import os

from .folder import Folder


class Project(Folder):
    """The Project class represents the project and every other class is supposed to be used as a child of it.

    args:
        path: project path
        print_exceptions: this argument is passed to all the children of this class"""

    def __init__(self, path: str, print_exceptions: bool = True) -> None:
        self.print_exceptions = print_exceptions
        self.parent = ""
        self.name = path
        self.print_exception = print_exceptions
        try:
            os.mkdir(path)
        except Exception as e:
            if print_exceptions:
                print(e)
