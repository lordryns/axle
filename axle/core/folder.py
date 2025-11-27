import os

from .file import File


class Folder:
    """The Folder class represents a single folder
    args:
        name: The direct name of the file instead of a path
        parent: The parent path"""

    def __init__(self, name: str, parent: str) -> None:
        self.name = name
        self.parent = (
            parent  # should be absolute, relative path might cause weird behaviour :(
        )
        self.children: list[Folder | File] = []

        self.print_exception = False

    @property
    def path(self) -> str:
        return os.path.abspath(os.path.join(self.parent, self.name))

    def create(self, print_exception: bool = True):
        self.print_exception = print_exception
        try:
            os.mkdir(self.path)
        except Exception as e:
            if print_exception:
                print(e)

    def create_child_folder(self, name: str):
        f = Folder(name, self.path)
        f.create(self.print_exception)
        return f

    def create_child_file(self, name: str, content: str = "") -> File:
        f = File(name, self.path, content=content)
        f.create()
        return f
