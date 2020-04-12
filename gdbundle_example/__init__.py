import gdb
import os

ROOT_DIR = os.path.dirname(__file__)

SCRIPT_PATHS = [
    [ROOT_DIR, 'scripts', 'example.gdb'],
    [ROOT_DIR, 'scripts', 'example.py']
]

def _abs_path(path):
    return os.path.abspath(os.path.join(*path))

def gdbundle_load():
    for script_path in SCRIPT_PATHS:
        gdb.execute("source {}".format(_abs_path(script_path)))
