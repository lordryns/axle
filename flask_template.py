import axle

project_name = input("Enter project name: ")

project = axle.Project(project_name)
project.create_child_file("main.py")

website = project.create_child_folder("website")
website.create_child_file("views.py")
website.create_child_file("auth.py")

templates = website.create_child_folder("templates")
templates.create_child_file("base.html")
templates.create_child_file("index.html")
templates.create_child_file("login.html")
templates.create_child_file("register.html")

static = website.create_child_folder("static")
static.create_child_file("style.css")

print("Done!")
