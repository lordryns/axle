import axle

project = axle.Project("test")

project.create_child_file("main.py")

website_folder = project.create_child_folder("website")


website_folder.create_child_file("views.py")

templates_folder = project.create_child_folder("templates")
templates_folder.create_child_file("index.html")
