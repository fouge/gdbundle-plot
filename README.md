# gdbundle-plot

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin used to plot 1-D arrays in a graph.

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
(gdb) plot var_name
```
