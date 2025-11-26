import os, sys

class File:
    """The file class represents a single file 
    \nargs:
        name: The direct name of the file instead of a path
        parent: The parent path
        content: The content of the file (type str)"""
    def __init__(self, name: str, parent: str, content: str ="") -> None:
        self.name: str = name
        self.ext: str = name.split('.')[-1]
        self.parent : str = parent 
        self.content = content

    @property 
    def path(self) -> str:
        return os.path.abspath(os.path.join(self.parent, self.name))

    def create(self, print_exception: bool = True):
        try:    
            with open(self.path, 'w') as f: f.write(self.content)
        except Exception as e:
            if print_exception: print(e)


class Folder:
    """The Folder class represents a single folder
    args:
        name: The direct name of the file instead of a path
        parent: The parent path"""

    def __init__(self, name: str, parent: str) -> None:
        self.name = name
        self.parent = parent # should be absolute, relative path might cause weird behaviour :(
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
            if print_exception: print(e)

    def create_child_folder(self, name: str):
        f = Folder(name, self.path)
        f.create(self.print_exception)
        return f

    def create_child_file(self, name: str, content: str = "") -> File:
        f = File(name, self.path, content=content)
        f.create()
        return f
    



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
            if print_exceptions: print(e)


def get_arg(index: int) -> str | None:
    """use to grab an argument from the command line and return line if argument isn't found"""
    try:
        return sys.argv[index]
    except:
        return None
