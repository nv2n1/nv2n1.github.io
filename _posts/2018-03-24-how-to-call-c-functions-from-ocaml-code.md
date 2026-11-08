---
title: "Calling C Functions from OCaml"
date: 2018-03-24 08:15:56 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-call-c-functions-from-ocaml-code/
---

OCaml provides robust FFI (Foreign Function Interface) capabilities for calling C code. This is essential when you need to use existing C libraries or write performance-critical sections in C.

## Using the Unix Module

The simplest approach for Unix/Linux system calls is the built-in `Unix` module, which wraps common POSIX functions without requiring manual FFI binding.

``` ocaml
open Unix

let () =
  Printf.printf "My pid: %d\n" (getpid ());
  Printf.printf "Directory listing:\n";
  let _ = system "ls -la /" in
  ()
```

Compile and run with:

``` bash
ocamlc -o example unix.cma example.ml
./example
```

Or use `ocamlopt` for native code:

``` bash
ocamlopt -o example unix.cmxa example.ml
./example
```

## Writing OCaml Stubs for C Functions

For arbitrary C functions, you need to write OCaml stubs. This involves:

1.  **C stub file** (`mylib_stubs.c`) — wraps the C function
2.  **OCaml interface** (`mylib.mli`) — declares the OCaml function
3.  **Dune or Makefile** — compiles both

### Simple Example: Wrapping a C Function

Say you have a C library with:

``` c
/* mylib.h */
int add(int a, int b);
```

Create the stub file:

``` c
/* mylib_stubs.c */
#include <caml/alloc.h>
#include <caml/memory.h>
#include <caml/value.h>
#include "mylib.h"

value caml_add(value a, value b) {
  CAMLparam2(a, b);
  int result = add(Int_val(a), Int_val(b));
  CAMLreturn(Val_int(result));
}
```

Define the OCaml interface:

``` ocaml
(* mylib.mli *)
external add : int -> int -> int = "caml_add"
```

And the implementation:

``` ocaml
(* mylib.ml *)
external add : int -> int -> int = "caml_add"
```

### Using Dune (Recommended)

Create a `dune` file:

``` lisp
(library
 (name mylib)
 (foreign_stubs
  (language c)
  (names mylib_stubs)
  (flags (:standard -I/path/to/c/headers))))
```

Then use it:

``` ocaml
let () =
  Printf.printf "2 + 3 = %d\n" (Mylib.add 2 3)
```

Build with:

``` bash
dune build
dune exec ./program.exe
```

## Handling More Complex Types

For strings, you need different conversions:

``` c
/* String stub */
value caml_concat_strings(value str1, value str2) {
  CAMLparam2(str1, str2);
  char *s1 = String_val(str1);
  char *s2 = String_val(str2);

  char result[512];
  snprintf(result, sizeof(result), "%s%s", s1, s2);

  CAMLreturn(caml_copy_string(result));
}
```

For pointers and structs, use abstract types:

``` ocaml
(* mylib.mli *)
type opaque_ptr
external create_ptr : unit -> opaque_ptr = "caml_create_ptr"
external use_ptr : opaque_ptr -> unit = "caml_use_ptr"
```

## Resources

- **Official Manual**: <a href="https://v2.ocaml.org/manual/index.html" rel="nofollow noopener" target="_blank">Chapter 20: Interfacing C with OCaml</a> — comprehensive reference
- **Ctypes Library**: Alternative to hand-written stubs; safer and easier for complex bindings
- **OCaml FFI Best Practices**: Memory management, garbage collection interaction, and error handling

## Common Pitfalls

- **Forgetting `CAMLparam`/`CAMLreturn`** — these manage the OCaml stack and garbage collector
- **Not protecting heap allocations** — use `caml_copy_string()` and similar functions
- **Mixing OCaml and C calling conventions** — always wrap C functions in the stub layer
- **Mismatched types** — `Int_val()` extracts int, `Val_int()` wraps it; strings require `String_val()` and `caml_copy_string()`

For complex C libraries, consider using **Ctypes** or code generation tools rather than hand-written stubs. This reduces maintenance burden and safety issues.

## 2026 Best Practices and Advanced Techniques

For Calling C Functions from OCaml, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
