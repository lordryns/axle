import os 


class File:
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
    def __init__(self, path: str, print_exceptions: bool = True) -> None:
        self.print_exceptions = print_exceptions
        self.parent = ""
        self.name = path
        self.print_exception = print_exceptions
        try:
            os.mkdir(path)
        except Exception as e:
            if print_exceptions: print(e)

        
