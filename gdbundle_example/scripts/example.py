import gdb


class HelloPy(gdb.Command):
    """Prints Hello"""

    def __init__(self):
        super(HelloPy, self).__init__('hello_py', gdb.COMMAND_USER)

    def invoke(self, _unicode_args, _from_tty):
        print("Hello from gdbundle Python")

HelloPy()
