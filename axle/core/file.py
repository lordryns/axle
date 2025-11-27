import os


class File:
    """The file class represents a single file
    \nargs:
        name: The direct name of the file instead of a path
        parent: The parent path
        content: The content of the file (type str)"""

    def __init__(self, name: str, parent: str, content: str = "") -> None:
        self.name: str = name
        self.ext: str = name.split(".")[-1]
        self.parent: str = parent
        self.content = content

    @property
    def path(self) -> str:
        return os.path.abspath(os.path.join(self.parent, self.name))

    def create(self, print_exception: bool = True):
        try:
            with open(self.path, "w") as f:
                f.write(self.content)
        except Exception as e:
            if print_exception:
                print(e)
