# gdbundle-example

This is a [gdbundle](https://github.com/memfault/gdbundle) plugin example. It is not meant to be useful, but to serve as a reference for gdbundle plugin creators and curious individuals.

## Compatibility

- GDB
- LLDB

## Installation

After setting up [gdbundle](https://github.com/memfault/gdbundle), install the package from PyPi. 

```
$ pip install gdbundle-example
```

If you've decided to manually manage your packages using the `gdbundle(include=[])` argument,
add it to the list of plugins.

```
# .gdbinit

[...]
import gdbundle
plugins = ["example"]
gdbundle.init(include=plugins)
```

## Building

```
$ poetry build
$ poetry publish
```
