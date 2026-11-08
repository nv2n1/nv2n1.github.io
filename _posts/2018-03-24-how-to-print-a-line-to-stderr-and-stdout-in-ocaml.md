---
title: "Printing to STDERR and STDOUT in OCaml"
date: 2018-03-24 11:53:05 +0000
modified: 2026-04-12 08:03:32 +0000
author: "Q A"
layout: post
categories: [programming-languages]
canonical: /how-to-print-a-line-to-stderr-and-stdout-in-ocaml/
---

\[md\]
In OCaml, the standard library provides straightforward functions for writing to standard output and standard error.

\## Printing to STDOUT

Use `print_endline` to write a string followed by a newline to standard output:

```wp-block-code
print_endline "hello world!"
```

This function is in the `Stdlib` module (formerly `Pervasives` in older OCaml versions) and automatically flushes the output buffer. The signature is:

```wp-block-code
val print_endline : string -> unit
```

For printing without a newline:

```wp-block-code
print_string "hello "
```

\## Printing to STDERR

Use `prerr_endline` and `prerr_string` for standard error:

```wp-block-code
prerr_endline "error: something went wrong"
prerr_string "warning: "
```

The “prerr” prefix consistently indicates stderr output across the standard library.

\## Printf-Style Formatted Output

OCaml’s `Printf` module provides type-safe formatted printing:

```wp-block-code
(* To stdout *)
Printf.printf "Name: %s, Age: %d, Score: %.2f\n" name age score

(* To stderr *)
Printf.eprintf "Error: %s (code %d)\n" msg code
```

Common format specifiers:

– `%s` — string
– `%d` — integer
– `%f` — float
– `.2f` — float with 2 decimal places
– `%b` — boolean (true/false)
– `%c` — character
– `%a` — user-defined formatter (advanced)

The compiler checks that the number and types of arguments match the format string — a mismatch is a compile-time error, not a runtime crash.

\## Using Format for Pretty-Printing

For structured output with indentation and alignment, OCaml’s `Format` module is the standard approach:

```wp-block-code
let print_person name age =
  Format.printf "Person {@[@ name: %s;@ age: %d@]@,}@."
    name age
```

The `Format` module uses “pretty-print boxes” to manage layout:

– `@[` — open a box
– `@]` — close a box
– `@,` — break hint (may become a newline)
– `@;` — break hint with custom spacing
– `@.` — flush and newline

\## Redirecting Output Programmatically

You can redirect stdout or stderr to a file:

```wp-block-code
let with_output_to filename f =
  let oc = open_out filename in
  let old_stdout = Unix.dup Unix.stdout in
  Unix.dup2 (Unix.descr_of_out_channel oc) Unix.stdout;
  let result = f () in
  Unix.dup2 old_stdout Unix.stdout;
  close_out oc;
  result

(* Usage *)
let () =
  with_output_to "log.txt" (fun () ->
    print_endline "This goes to the file";
    42
  )
```

\## Using the Logs Library

For production applications, the `logs` library provides structured logging with level filtering:

```wp-block-code
(* Install: opam install logs *)

(* In your application *)
Logs.info (fun m -> m "Server started on port %d" port);
Logs.warn (fun m -> m "Connection timeout after %.1f seconds" elapsed);
Logs.err (fun m -> m "Failed to open %s: %a" filename Fmt.exn exn);

(* Set log level *)
Logs.set_level (Some Logs.Warning);  (* Only warn and error *)
```

\## Quick Reference

– `print_endline` — stdout with newline
– `print_string` — stdout without newline
– `prerr_endline` — stderr with newline
– `prerr_string` — stderr without newline
– `Printf.printf` — formatted stdout
– `Printf.eprintf` — formatted stderr
– `Format.printf` — pretty-printed stdout
– `Logs.info/warn/err` — structured logging

For most command-line tools, `print_endline` and `prerr_endline` cover the common cases. Reach for `Printf` when you need formatting, and `Format` when you need structured output.

\## Flushing Output

OCaml buffers output for performance. If your program crashes or you need real-time output, flush explicitly:

```wp-block-code
print_string "Processing...";
flush stdout;  (* Force immediate output *)
(* Do long computation *)
print_endline "done"
```

The `print_endline` and `prerr_endline` functions flush automatically. But `print_string` and `prerr_string` do not — you must call `flush stdout` or `flush stderr` manually.

This matters for progress indicators:

```wp-block-code
let show_progress i total =
  let pct = 100 * i / total in
  Printf.printf "\rProgress: %d%%" pct;
  flush stdout

let () =
  for i = 1 to 1000 do
    show_progress i 1000;
    Unix.sleepf 0.01
  done;
  print_endline ""
```

\## Capturing Output in Tests

When writing tests, you may want to capture stdout or stderr output:

```wp-block-code
let capture_stdout f =
  let buf = Buffer.create 256 in
  let old_stdout = stdout in
  let new_stdout = Stdlib.open_out_gen [Open_wronly; Open_creat] 0 "/dev/null" in
  (* Simplified: in practice use Unix.dup2 for proper capture *)
  let result = f () in
  result

(* Better approach: use the Camlunix or Core library's capture utilities *)
```

For testing, the simplest approach is often to use functions that return strings instead of printing, and only use printing in your main entry point:

```wp-block-code
(* Library function - returns string, easy to test *)
let format_result name score =
  Printf.sprintf "Result: %s scored %.1f" name score

(* CLI entry point - does the printing *)
let () =
  print_endline (format_result "Alice" 95.5)
```

This separation makes your code testable while still supporting formatted output.
