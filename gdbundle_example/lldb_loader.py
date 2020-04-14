import lldb
import os

PACKAGE_DIR = os.path.dirname(__file__)

SCRIPT_PATH = [PACKAGE_DIR, 'scripts', 'example_lldb.py']


def _abs_path(path):
    return os.path.abspath(os.path.join(*path))

def gdbundle_load():
    lldb.debugger.HandleCommand('command script import {}'.format(_abs_path(SCRIPT_PATH)))
