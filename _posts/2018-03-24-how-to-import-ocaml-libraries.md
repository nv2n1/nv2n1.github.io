---
title: "Importing OCaml Libraries: A Practical Guide"
date: 2018-03-24 08:17:50 +0000
modified: 2026-04-12 16:10:06 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-import-ocaml-libraries/
---

The OCaml compiler only finds the standard library (List, Array, etc.) by default. Third-party libraries require you to explicitly tell the compiler where to find them.

## Using ocamlfind

The standard approach is **ocamlfind**, a package manager that tracks installed libraries and their locations. It’s part of the OPAM ecosystem and should already be installed if you’re using OPAM (the recommended package manager for OCaml).

### Building with ocamlfind

For compilation, use `ocamlfind ocamlc` or `ocamlfind ocamlopt` instead of the bare compiler:

``` bash
ocamlfind ocamlc -package batteries -linkpkg -o myprogram myprogram.ml
ocamlfind ocamlopt -package batteries,yojson -linkpkg -o myprogram myprogram.ml
```

The `-package` flag specifies libraries, and `-linkpkg` automatically links them. For multiple packages, separate them with commas.

### Interactive REPL (ocaml toplevel)

In the interactive toplevel, automate library loading by editing `~/.ocamlinit`:

``` ocaml
#use "topfind";;
#require "batteries";;
#require "yojson";;
```

Then launch `ocaml` and the packages load automatically. In a running session, you can dynamically load packages:

``` ocaml
#use "topfind";;
#require "batteries";;
#require "unix";;
```

## Using Dune (Recommended)

Most modern OCaml projects use Dune as the build system. Specify dependencies in your `dune` file:

``` lisp
(executable
 (name myprogram)
 (libraries batteries yojson))
```

Or for libraries:

``` lisp
(library
 (name mylib)
 (libraries batteries str re))
```

Run `dune build` and Dune handles all library resolution through OPAM.

## Finding Available Packages

List installed packages and their locations:

``` bash
ocamlfind list
```

This shows package names, versions, and directories. To check if a specific package is installed:

``` bash
ocamlfind query batteries
```

If not installed, add it via OPAM:

``` bash
opam install batteries yojson
```

## Manual Path Specification (Legacy)

If you must specify paths manually (rarely necessary):

``` bash
ocamlc -I /path/to/lib -o myprogram myprogram.ml
```

But this is error-prone and doesn’t handle transitive dependencies. Always prefer ocamlfind or Dune.

## Common Issues

**Package not found**: Run `opam install package-name` and verify with `ocamlfind query package-name`.

**Version conflicts**: OPAM handles this. Check `opam switch` if using multiple OCaml versions.

**Module not loading in toplevel**: Ensure you called `#use "topfind";;` first, then `#require "package";;`.

Use OPAM and Dune for modern OCaml work. ocamlfind is the underlying mechanism that both rely on.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
