---
title: "Debugging C/C++ with GDB on Linux"
date: 2013-07-12 16:47:45 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/gdb-cheat-sheet/
---

GDB is the standard debugger for C/C++ development on Linux. This reference covers essential commands for breakpoints, execution control, inspection, and troubleshooting common debugging scenarios.

## Starting GDB

``` bash
gdb ./program
gdb ./program core.dump           # Debug with core file
gdb -p <pid>                      # Attach to running process
gdb --args ./program arg1 arg2    # Pass arguments to program
gdb -tui ./program                # Text UI mode (split screen with source)
```

## Execution Control

| Command       | Shortcut    | Purpose                                 |
|---------------|-------------|-----------------------------------------|
| run           | r           | Start program execution                 |
| run arg1 arg2 | r arg1 arg2 | Run with arguments                      |
| continue      | c           | Resume after breakpoint                 |
| next          | n           | Execute next line (step over functions) |
| step          | s           | Execute next line (step into functions) |
| finish        | fin         | Run until current function returns      |
| until         | u           | Run until line number (avoid loops)     |
| nexti         | ni          | Execute next machine instruction        |
| stepi         | si          | Step one machine instruction            |

## Breakpoints

### Setting Breakpoints

``` bash
break main                        # Break at function
break file.c:42                   # Break at line 42 in file.c
break file.c:main                 # Break at main in specific file
tbreak file.c:100                 # Temporary breakpoint (cleared after hit)
rbreak regex                      # Break on all functions matching regex
break my_function if count > 100  # Conditional breakpoint
break parse.c:234 if strlen(buf) == 0
```

### Managing Breakpoints

``` bash
info breakpoints                  # List all breakpoints
delete 1                          # Remove breakpoint 1
delete                            # Remove all breakpoints
disable 2                         # Disable breakpoint 2 (keep for later)
enable 2                          # Re-enable breakpoint 2
clear file.c:50                   # Clear all breakpoints at line 50
condition 1 count > 50            # Add/modify condition on breakpoint 1
```

## Inspection and Variables

### Printing Values

``` bash
print variable                    # Print variable value
print variable@10                 # Print first 10 elements of array
print *pointer                    # Dereference pointer
print &variable                   # Print address of variable
print variable.field              # Access struct field
print variable->field             # Access struct via pointer
print ((type *)address)->field     # Cast and dereference
print $variable                   # Print convenience variable
```

### Memory Examination

The `x` command examines memory at an address with format specifiers:

``` bash
x/fmt address
```

Format: `count type format`

- **Type**: `b` (byte), `h` (halfword/2 bytes), `w` (word/4 bytes), `g` (giant/8 bytes)
- **Format**: `x` (hex), `d` (decimal), `u` (unsigned), `o` (octal), `s` (string), `i` (instruction), `a` (address), `c` (char)

Examples:

``` bash
x/10xb 0x7fff0000                # 10 bytes in hex
x/20xw $sp                       # 20 words in hex starting at stack pointer
x/5s 0x7fff0000                  # 5 strings
x/10i main                       # 10 instructions from main (disassembly)
```

## Stack and Frames

``` bash
backtrace                         # Show call stack
backtrace full                    # Show call stack with local variables
backtrace 5                       # Show last 5 frames
frame 2                           # Switch to frame 2
up                                # Move to calling frame
down                              # Move to called frame
info locals                       # List local variables in current frame
info args                         # List function arguments
```

## Watchpoints

Watchpoints stop execution when a variable changes:

``` bash
watch variable                    # Stop when variable is written
watch variable if condition       # Conditional watchpoint
rwatch variable                   # Stop when variable is read
awatch variable                   # Stop on read or write
info watchpoints                  # List all watchpoints
delete watch 1                    # Remove watchpoint 1
```

## Disassembly and Registers

``` bash
disassemble main                  # Show assembly for function
disassemble /m main               # Assembly with source code interleaved
disassemble 0x7fff0000 0x7fff0100 # Assembly in address range
info registers                    # Show all register contents
info all-registers                # Show all registers including FP/vector
print $rax                        # Print specific register (x86-64)
print $rbp                        # Print base pointer
```

## Source Code Navigation

``` bash
list                              # Show source around current location
list file.c:50                    # Show source at line 50
list -                            # Show previous 10 lines
list +                            # Show next 10 lines
directory /path/to/source         # Add source directory to search path
```

## Advanced Techniques

### Automation with Commands

Execute commands automatically at breakpoints:

``` bash
commands 1
silent
print variable
print another_var
continue
end
```

The `silent` keyword suppresses standard breakpoint messages. This is useful for logging variable values without manual inspection.

### Custom Functions

Define reusable debugging commands:

``` bash
define print_struct
print $arg0
print $arg0->field1
print $arg0->field2
end

# Usage:
print_struct my_struct_ptr
```

### Reverse Debugging

Some builds of GDB support reverse execution (requires Intel Processor Trace or rr):

``` bash
set record full insn-number-max unlimited
record
# ... run program
reverse-continue                  # Go backward
reverse-step                      # Step backward
```

Note: Reverse debugging requires compilation with debug symbols and works best with the `rr` tool for Linux process recording.

### Expression Evaluation

Evaluate complex expressions in the program’s context:

``` bash
print array[index]
print sizeof(type)
print (int)pointer_var            # Cast during evaluation
call my_function(arg1, arg2)      # Call a function from the program
```

## Configuration and Output

``` bash
set print pretty on               # Format struct output nicely
set print array on                # Print arrays on multiple lines
set print array-indexes on        # Show array indices
set pagination off                # Disable paging (useful in scripts)
set confirm off                   # Disable confirmation prompts
set logging on                    # Log session to gdb.txt
set logging file output.log       # Specify log filename
handle SIGPIPE noprint nostop     # Ignore signal SIGPIPE
```

## Common Debugging Workflows

### Segmentation Fault

``` bash
gdb ./program
(gdb) run
# ... crash occurs
(gdb) backtrace full              # See full call stack with locals
(gdb) frame 2                     # Switch to frame 2
(gdb) info locals                 # Examine local variables
(gdb) x/20x $sp                   # Dump stack memory
```

### Memory Corruption with AddressSanitizer

Instead of hunting with GDB, compile with AddressSanitizer for faster detection:

``` bash
gcc -fsanitize=address -g -O1 program.c -o program
./program
```

AddressSanitizer will pinpoint the exact line causing memory errors.

### Debugging Optimized Binaries

Compile with `-O0 -g` for reliable debugging:

``` bash
gcc -O0 -g program.c -o program
```

Higher optimization levels (`-O2`, `-O3`) reorder instructions and inline functions, making breakpoints and variable inspection unreliable.

### Following Child Processes

``` bash
set follow-fork-mode child        # Debug child process instead of parent
set detach-on-fork off            # Keep both processes under GDB control
info inferiors                    # List all processes
inferior 2                        # Switch to process 2
```

### Scripting GDB

Create a script file for automation:

``` bash
cat > debug.gdb << 'EOF'
break main
run
backtrace
info locals
quit
EOF

gdb -x debug.gdb ./program
```

Or non-interactively:

``` bash
gdb -batch -x script.gdb ./program
```

## Tips and Tricks

- **Tab completion**: Works for commands, functions, and variable names
- **History**: Use arrow keys to navigate command history, or `history` command
- **Convenience variables**: Create variables with `set $myvar = value`
- **Help system**: `help command` or `help category` for detailed information
- **Quit**: `quit`, `q`, or Ctrl+D
- **Large output**: Use `set pagination off` in scripts to prevent hanging
- **GDB dashboard**: Install `gdb-dashboard` for a tmux-like UI showing registers, stack, and source simultaneously

## Performance Debugging

For CPU-intensive programs, use sampling profilers alongside GDB:

``` bash
# Attach to running process and sample
perf record -p <pid> -g -- sleep 10
perf report
```

Then use GDB to examine hot functions identified by perf.

For detailed GDB documentation, consult the <a href="https://sourceware.org/gdb/documentation/" rel="nofollow noopener" target="_blank">GDB manual</a>.
