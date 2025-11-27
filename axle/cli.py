import sys
from .core.project import Project

def main():
    print("Welcome to Axle CLI!")
    # Example: project name from first arg
    project_name = sys.argv[1] if len(sys.argv) > 1 else "default"
    Project(project_name)
