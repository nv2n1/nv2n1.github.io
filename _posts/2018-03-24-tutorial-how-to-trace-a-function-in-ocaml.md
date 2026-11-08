---
title: "Tracing Function Calls in OCaml"
date: 2018-03-24 08:18:25 +0000
modified: 2026-04-11 16:06:43 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /tutorial-how-to-trace-a-function-in-ocaml/
---

The `#trace` directive in OCaml’s interactive toplevel (ocaml or utop) logs function calls and returns, showing you exactly what arguments go in and what values come back out. This is invaluable for debugging recursive functions and understanding execution flow.

### Basic Usage

Define a function and enable tracing with `#trace`:

``` ocaml
# let rec factorial n = if n = 0 then 1 else factorial (n - 1) * n;;
val factorial : int -> int = <fun>

# #trace factorial;;
factorial is now traced.

# factorial 4;;
factorial <-- 4
factorial <-- 3
factorial <-- 2
factorial <-- 1
factorial <-- 0
factorial --> 1
factorial --> 1
factorial --> 2
factorial --> 6
factorial --> 24
- : int = 24
```

Each `<--` line shows an argument entering the function; each `-->` line shows a return value. The indentation visualizes call depth. This trace reveals the full recursion: factorial(4) calls factorial(3), which calls factorial(2), and so on down to the base case.

### Tracing Multiple Functions

You can trace several functions simultaneously:

``` ocaml
# let rec fib n = if n <= 1 then n else fib (n - 1) + fib (n - 2);;
val fib : int -> int = <fun>

# #trace fib;;
fib is now traced.

# #trace factorial;;
factorial is now traced.

# fib 5;;
fib <-- 5
fib <-- 4
fib <-- 3
fib <-- 2
fib <-- 1
fib --> 1
fib <-- 1
fib --> 1
fib --> 2
fib <-- 2
fib <-- 1
fib --> 1
fib <-- 0
fib --> 0
fib --> 1
fib --> 3
fib --> 5
- : int = 5
```

### Disabling Traces

Use `#untrace` to stop logging a specific function:

``` ocaml
# #untrace fib;;
fib is no longer traced.
```

Or remove all active traces:

``` ocaml
# #untrace all;;
```

### Practical Limitations and Alternatives

**Performance**: Tracing adds overhead and becomes unwieldy with high-frequency calls. The fib example above shows redundant calls—fib(3) is computed twice. Traces get long quickly.

**Scope**: `#trace` only works in the interactive toplevel. For compiled code, use a debugger like `ocamldebug`:

``` bash
ocamlc -g myfile.ml -o myprogram
ocamldebug ./myprogram
```

Then use `ocamldebug` commands like `step`, `next`, `print`, and `backtrace` to inspect execution.

**Alternative: Custom Logging**

For production or batch debugging, add explicit logging:

``` ocaml
let trace_calls = ref true

let rec factorial n =
  if !trace_calls then Printf.printf "factorial <-- %d\n" n;
  let result = if n = 0 then 1 else factorial (n - 1) * n in
  if !trace_calls then Printf.printf "factorial --> %d\n" result;
  result
```

This gives you control over what gets logged and lets you redirect output.

### When to Use

- **Debugging simple functions**: Use `#trace` in the REPL for quick inspection.
- **Understanding recursion**: Traces clarify the call order and argument flow.
- **Finding infinite loops or stack issues**: Watch for unexpected repeated calls.
- **Performance analysis**: Traces reveal redundant computation (as in fib above).

For serious debugging of compiled code or complex programs, `ocamldebug` is more capable. For ongoing instrumentation, custom logging is cleaner and more flexible.
