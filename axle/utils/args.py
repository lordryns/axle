import sys


def get_arg(index: int) -> str | None:
    """use to grab an argument from the command line and return line if argument isn't found"""
    try:
        return sys.argv[index]
    except:
        return None
