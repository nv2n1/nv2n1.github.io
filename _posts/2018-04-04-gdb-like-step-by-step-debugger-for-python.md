---
title: "Python Debugging with pdb: A Step-by-Step Command Guide"
date: 2018-04-04 07:36:03 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/gdb-like-step-by-step-debugger-for-python/
---

The built-in pdb module is Python’s equivalent to gdb — a command-line debugger that lets you step through code, set breakpoints, inspect variables, and control execution flow. It’s essential for server-side debugging and situations where IDE graphical debuggers aren’t available.

## Starting a pdb Session

Run a script through pdb directly:

``` bash
python -m pdb prog.py arg1 arg2
```

Or insert a breakpoint within your code:

``` python
def my_function():
    x = 10
    breakpoint()  # execution pauses here
    return x * 2
```

The `breakpoint()` call (Python 3.7+) is the modern standard. Older code uses `import pdb; pdb.set_trace()`, which still works but is less readable.

## Essential Commands

Type `help` at the pdb prompt to list all commands. Here are the ones you’ll use constantly:

| Command | Shortcut | Purpose |
|----|----|----|
| `next` | `n` | Execute current line without entering functions |
| `step` | `s` | Execute current line, step into function calls |
| `continue` | `c` | Resume execution until next breakpoint or exit |
| `break <lineno>` | `b <lineno>` | Set breakpoint at specified line number |
| `break <funcname>` | `b <funcname>` | Set breakpoint at function entry |
| `list` | `l` | Display source code around current position |
| `print <var>` | `p <var>` | Print variable value |
| `pp <var>` | `pp <var>` | Pretty-print complex objects (dicts, lists) |
| `where` | `w` | Show full stack trace |
| `up` | `u` | Move up one frame in the stack |
| `down` | `d` | Move down one frame in the stack |
| `return` | `r` | Execute until current function returns |
| `until <lineno>` | `unt <lineno>` | Execute until reaching a specific line |
| `whatis <var>` | — | Display variable type |
| `condition <bp> <expr>` | — | Break only when expression evaluates true |
| `commands <bp>` | — | Attach commands to run automatically at breakpoint |

## Working Through a Practical Example

Consider this function with a logic issue:

``` python
def process_data(items):
    result = []
    for item in items:
        value = item * 2
        result.append(value)
    return result

process_data([1, 2, 3])
```

Run it with pdb:

``` bash
$ python -m pdb script.py
> /path/to/script.py(1)<module>()
-> def process_data(items):
(Pdb)
```

Set a breakpoint at line 4 (the calculation) and continue:

    (Pdb) b 4
    Breakpoint 1 at /path/to/script.py:4
    (Pdb) c
    > /path/to/script.py(4)process_data()
    -> value = item * 2

Inspect variables at this point:

    (Pdb) p item
    1
    (Pdb) p result
    []
    (Pdb) p value
    NameError: name 'value' is not defined

The variable `value` doesn’t exist yet because we haven’t executed the assignment. Step forward:

    (Pdb) n
    > /path/to/script.py(5)process_data()
    -> result.append(value)
    (Pdb) p value
    2

Continue stepping to see the entire first iteration complete:

    (Pdb) n
    > /path/to/script.py(3)process_data()
    -> for item in items:
    (Pdb) p result
    [2]

## Using Conditional Breakpoints

Instead of pausing on every iteration, break only when a condition is true:

    (Pdb) b 4, item > 1
    Breakpoint 1 at /path/to/script.py:4
    (Pdb) c

Now execution pauses only when `item` exceeds 1. This saves time when debugging loops over large datasets.

## Post-mortem Debugging

Debug an exception after it crashes by catching it and entering pdb at the failure point:

``` python
import pdb
import traceback

try:
    some_function()
except Exception:
    traceback.print_exc()
    pdb.post_mortem()
```

This drops you into pdb at the exact location where the exception occurred, with the full stack intact. You can inspect variables, move up and down the stack with `up`/`down`, and understand what went wrong.

Alternatively, run a script and let pdb handle uncaught exceptions automatically:

``` bash
python -m pdb -c continue prog.py
```

## Enhancing pdb with pdbpp

The standard pdb is functional but minimal. For a significantly better experience, install pdbpp:

``` bash
pip install pdbpp
```

pdbpp provides:

- Syntax highlighting in source listings
- Smart command completion
- Better pretty-printing of complex objects
- Automatic activation when using `breakpoint()` or `python -m pdb`

Once installed, it activates automatically with no additional configuration needed.

## Automating Debugging Tasks

You can automate repetitive debugging steps using command scripts. Create a file with pdb commands:

    b myfunction
    commands 1
    p var1
    p var2
    p var3
    continue
    end
    c

Then run pdb with the script:

``` bash
python -m pdb -c "source /path/to/commands.txt" prog.py
```

## Remote and Headless Debugging

On servers without graphical access, pdb is your primary tool. Connect via SSH and debug normally:

``` bash
ssh user@server
python -m pdb /path/to/script.py
```

For long-running processes, add breakpoints in code rather than starting under pdb, since you need an interactive terminal to control execution.

## Common Workflow Tips

- Use `l` frequently to see where you are in the code
- Combine `where` with `up`/`down` to navigate complex call stacks
- Use `pp` for dictionaries and lists instead of `p` for cleaner output
- Set multiple breakpoints before running (`b 10`, `b 20`, `b my_func`) rather than setting them interactively
- Use `until` to skip over loops when you only care about the next line after the loop exits
- Leverage `condition` to avoid manually resuming past breakpoints you don’t need

pdb is straightforward but powerful. Mastery of these commands makes debugging Python far faster than adding print statements and re-running code repeatedly.
