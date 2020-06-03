import lldb

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f plot_lldb.plot plot')

def plot(debugger, command, result, internal_dict):
    print('Work in progress')
