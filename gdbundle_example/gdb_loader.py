import gdb
import os

PACKAGE_DIR = os.path.dirname(__file__)

SCRIPT_PATHS = [
    [PACKAGE_DIR, 'scripts', 'example_gdb.gdb'],
    [PACKAGE_DIR, 'scripts', 'example_gdb.py']
]

def _abs_path(path):
    return os.path.abspath(os.path.join(*path))

def gdbundle_load():
    for script_path in SCRIPT_PATHS:
        gdb.execute("source {}".format(_abs_path(script_path)))
