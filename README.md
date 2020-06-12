# gdbundle-plot

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin used to plot 1-D arrays in a graph.

C and Rust types can be parsed using the plugin.

One or several arrays can be plotted on the same graph.

## Compatibility

- GDB
- LLDB: Not yet

## Installation

### From source

After setting up [gdbundle](https://github.com/memfault/gdbundle), install the package using:

```
$ poetry install
```

If you've decided to manually manage your packages using the `gdbundle(include=[])` argument,
add it to the list of plugins.

```
# .gdbinit

[...]
import gdbundle
plugins = ["plot"]
gdbundle.init(include=plugins)
```

## Usage

```
(gdb) plot var1_name [var2_name ...]
```
