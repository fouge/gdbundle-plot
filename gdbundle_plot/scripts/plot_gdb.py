import gdb
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing as mp

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

class ProcessPlotter(object):
    def __init__(self):
        pass

    def terminate(self):
        plt.close('all')

    def call_back(self):
        has_data = False
        while self.pipe.poll():
            axis = self.pipe.recv()
            has_data = True
            if axis is None:
                self.ax.cla()
            else:
                self.ax.plot(range(0, len(axis[0])), axis[0], axis[1], label=axis[2])

        if has_data:
            self.ax.legend()
            self.fig.canvas.draw()
        return True

    def __call__(self, pipe):
        print('starting plotter...')

        self.pipe = pipe
        self.fig, self.ax = plt.subplots()

        timer = self.fig.canvas.new_timer(interval=1000)
        timer.add_callback(self.call_back)
        timer.start()

        plt.show()


class Plot(gdb.Command):
    """Plots array passed as argument (variable name)"""

    def __init__(self):
        super(Plot, self).__init__('plot', gdb.COMMAND_USER)
        self.plot_pipe, self.plotter_pipe = mp.Pipe()
        self.plotter = None
        self.plot_process = None

    def invoke(self, _unicode_args, _from_tty):
        # Check args
        if len(_unicode_args) == 0:
            print("Wrong arguments, pass one or several variables")
            return -1

        # Start one side process (and only one) to display data
        if self.plotter == None:
            self.plotter = ProcessPlotter()
            self.plot_process = mp.Process(
                target=self.plotter, args=(self.plotter_pipe,), daemon=True)
            self.plot_process.start()
        elif not self.plot_process.is_alive():
            self.plotter = ProcessPlotter()
            self.plot_process = mp.Process(
                target=self.plotter, args=(self.plotter_pipe,), daemon=True)
            self.plot_process.start()

        # Parse arguments
        args = _unicode_args.split(' ')

        # Reset the current graph by sending a None message to subprocess
        self.plot_pipe.send(None)

        for i in range(0, len(args)):
            val = gdb.parse_and_eval(args[i])
            val_type = str(val.type)

            # Init variables for each new variables
            array = []
            array_size = None
            array_type = None

            # If variable is reference to array
            #  - dereference it first
            #  - get type and size
            if "*" in val_type:
                val = val.dereference()
                val_type = val_type.replace('*', '')
            elif "&" in val_type:
                array_size = int(val["length"])
                val = val["data_ptr"]
                array_type = val_type.replace('[', '').replace(']', '').replace('&', '')

            # If variable is an array,
            #  - val_type will be formatted: "[type; size]",
            #  - parse it to get type and size
            if '[' in val_type and ']' in val_type and "; " in val_type:
                array_type_size = val_type.replace('[', '').replace(']', '').split("; ")
                array_size = int(array_type_size[1])
                array_type = array_type_size[0]

                # For Rust, remove 'mut' in type
                if 'mut' in array_type:
                    array_type = array_type.split(' ')[1];

            # If everything went well and the variable can be parsed
            #  - parse it
            if array_size and array_type:
                print("Parsing {}; array of size {}, type {}".format(args[i], array_size, array_type))

                for j in range(0, array_size):
                    array.append(_type_list[array_type](val[j]))

                # Send to subprocess :
                #  - array data
                #  - color for pretty printing
                #  - variable name for caption
                self.plot_pipe.send([array, _colors[i % len(_colors)], args[i]])
            else:
                print("Variable \'{}\' is not an array or cannot be parsed currently".format(args[i]))

Plot()
