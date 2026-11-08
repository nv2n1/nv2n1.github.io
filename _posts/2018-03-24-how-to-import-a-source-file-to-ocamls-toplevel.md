---
title: "How to Import Source Files into the OCaml Toplevel"
date: 2018-03-24 08:16:05 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-import-a-source-file-to-ocamls-toplevel/
---

To load and execute code from a source file in the OCaml interactive toplevel, use the `#use` directive:

``` ocaml
#use "file-name";;
```

This reads, compiles, and executes OCaml phrases from the specified file as if you’d typed them directly into the toplevel. Execution stops at the first error encountered.

## Common use cases

**Loading utility functions**

If you have helper functions in `utils.ml`:

``` ocaml
(* utils.ml *)
let add x y = x + y
let multiply x y = x * y
```

Load them into the toplevel:

``` ocaml
#use "utils.ml";;
(* val add : int -> int -> int = <fun> *)
(* val multiply : int -> int -> int = <fun> *)

add 5 3;;
(* - : int = 8 *)
```

**Loading with relative paths**

Use relative paths from your current working directory:

``` ocaml
#use "../lib/helpers.ml";;
#use "./src/mymodule.ml";;
```

**Clearing and reloading**

There’s no built-in `#unload`, but you can restart the toplevel or use `#quit;;` and restart. If you’re iterating on a file, it’s often cleaner to restart the session and reload:

``` ocaml
#quit;;
```

Then start a fresh toplevel and `#use` the file again.

## Modern workflow: Using dune

For larger projects, `#use` becomes cumbersome. The modern approach uses Dune and `utop`:

``` bash
opam install utop dune
```

In your `dune` file:

``` lisp
(executable
 (name my_program)
 (libraries str unix))
```

Run the REPL with your project loaded:

``` bash
dune utop
```

This automatically compiles your libraries and makes them available in the toplevel without manual `#use` directives.

## Related directives

- `#mod_use "file";;` — Like `#use`, but wraps the file’s content in a module
- `#load "file.cmo";;` — Load precompiled bytecode objects
- `#directory "path";;` — Add a directory to the search path for `#load`
- `#show_val name;;` — Display the type and value of a binding

## Troubleshooting

**File not found errors**: Make sure you’re running the toplevel from the correct directory. Use `#pwd;;` to check your current working directory.

**Compilation errors in the loaded file**: The toplevel will print the error and stop processing. Fix the file and reload with `#use` again.

**Dependencies on external libraries**: If your source file uses external packages, load them first:

``` ocaml
#require "str";;
#use "myfile.ml";;
```

Or use `#use_output` to dynamically generate and execute directives (OCaml 4.14+):

``` ocaml
#use_output "ls *.ml | sed 's/^/#use \"/' | sed 's/$/';;/'";;
```

For detailed documentation on all toplevel directives, see the <a href="https://ocaml.org/manual/toplevel.html" rel="nofollow noopener" target="_blank">OCaml manual</a>.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
