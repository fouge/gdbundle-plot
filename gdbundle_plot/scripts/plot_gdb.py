import gdb
import matplotlib.pyplot as plt
import numpy as np

_type_list = {
            # C types
            'char': np.int8, 
            'unsigned char': np.uint8, 
            'short': np.int16,
            'unsigned short': np.uint16,
            'int': np.int32, 
            'unsigned int': np.uint32,
            'float': np.float32,
            'double': np.float64,
            # Rust types
            'u8': np.uint8,
            'i8': np.int8, 
            'i16': np.int16,
            'u16': np.uint16,
            'i32': np.int32, 
            'u32': np.uint32, 
            'usize': np.uint32, 
            'f32': np.float32,
            'f64': np.float64,
            }

_colors = ['r', 'b', 'g', 'c', 'm', 'y']

class Plot(gdb.Command):
    """Plots array passed as argument (variable name)"""

    def __init__(self):
        super(Plot, self).__init__('plot', gdb.COMMAND_USER)

    def invoke(self, _unicode_args, _from_tty):


        if len(_unicode_args) == 0:
            print("Wrong arguments, pass variable name.")
            return -1

        args = _unicode_args.split(' ')

        for i in range(0, len(args)):
            val = gdb.parse_and_eval(args[i])
            val_type = str(val.type)

            array = []

            # Make sure we are plotting an array; type must be a string like: "[type; size]"
            if '[' in val_type and ']' in val_type:
                array_type = val_type.replace('[', '').replace(']', '').split("; ")

                print("Parsing array of size {}".format(int(array_type[1])))
                for j in range(0, int(array_type[1])):
                    value = _type_list[array_type[0]](val[j])
                    array.append(_type_list[array_type[0]](val[j]))

                print(array)
                plt.plot(array, _colors[i % len(_colors)],label=args[i])
            else:
                print("Variable \'{}\' is not an array".format(args[i]))

        plt.legend(loc='upper right')
        plt.show()

Plot()
