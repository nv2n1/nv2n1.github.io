---
title: "Measuring Function Execution Time in OCaml"
date: 2018-03-24 11:45:01 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-measure-a-functions-execution-time-in-ocaml/
---

Measuring the execution time of a function is useful for profiling and optimization work. OCaml provides straightforward tools for this.

## Basic approach with Unix.gettimeofday

The simplest method uses `Unix.gettimeofday()`, which returns wall-clock time as a float with microsecond precision:

``` ocaml
let time f =
  let t = Unix.gettimeofday () in
  let res = f () in
  Printf.printf "Execution time: %.6f seconds\n"
                (Unix.gettimeofday () -. t);
  res
```

This wrapper takes a thunk (a function of type `unit -> 'a`) and returns the result while printing elapsed time. The function must be wrapped in a lambda because you need to measure from after timing starts until the function completes.

Example with a naive Fibonacci:

``` ocaml
let rec fib n = 
  if n < 3 then 1 else fib (n-1) + fib (n-2)

let () = 
  let _ = time (fun () -> fib 40) in
  ()
```

Output:

    Execution time: 3.352741 seconds
    - : int = 102334155

## Improving precision and practicality

For better formatting and control, you can enhance the wrapper:

``` ocaml
let time_it ?(label="") f =
  let t = Unix.gettimeofday () in
  let res = f () in
  let elapsed = Unix.gettimeofday () -. t in
  let label_str = if label = "" then "" else label ^ ": " in
  Printf.printf "%sExecution time: %.6f seconds\n" label_str elapsed;
  res
```

Usage:

``` ocaml
time_it ~label:"Fibonacci(40)" (fun () -> fib 40)
```

## Measuring CPU time vs wall-clock time

`Unix.gettimeofday()` measures wall-clock (real) time, which includes sleep and I/O. For CPU-bound work, use `Unix.times()` instead to measure only CPU time consumed:

``` ocaml
let time_cpu f =
  let t1 = Unix.times () in
  let res = f () in
  let t2 = Unix.times () in
  let cpu_time = t2.Unix.tms_utime -. t1.Unix.tms_utime in
  Printf.printf "CPU time: %.6f seconds\n" cpu_time;
  res
```

The `tms_utime` field gives user-space CPU time. Add `tms_stime` if you want to include system calls.

## Using Sys.time for simplicity

OCaml also provides `Sys.time()`, which measures CPU time directly:

``` ocaml
let time_cpu_simple f =
  let t = Sys.time () in
  let res = f () in
  Printf.printf "CPU time: %.6f seconds\n" (Sys.time () -. t);
  res
```

This is simpler but less precise than `Unix.times()` for short operations.

## When measuring matters

Be aware that:

- Small timing values (\<10ms) are unreliable due to system noise—run multiple iterations
- First run may be slower due to JIT compilation or cache effects
- Wall-clock time includes garbage collection pauses; use profiling tools for detailed analysis

For serious profiling, consider using OCaml’s built-in profiling with `ocamlfind ocamlopt -p` or external tools like perf.

## 2026 Best Practices and Advanced Techniques

For Measuring Function Execution Time in OCaml, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
