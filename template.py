import axle

project = axle.Project(
    str(axle.get_arg(1)) if axle.get_arg(1) is not None else "default"
)

project.create_child_file("main.py")
website_folder = project.create_child_folder("website")
website_folder.create_child_file("views.py", content="import time")

templates_folder = project.create_child_folder("templates")
templates_folder.create_child_file("index.html")
