import lldb

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f example_lldb.hello_world hello_py')

def hello_world(debugger, command, result, internal_dict):
    print('Hello, world!')
