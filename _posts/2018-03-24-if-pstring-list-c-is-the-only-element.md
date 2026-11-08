---
title: "Pattern Matching Single-Element Lists in OCaml and Scala"
date: 2018-03-24 11:43:14 +0000
modified: 2026-04-12 16:38:04 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /if-pstring-list-c-is-the-only-element/
---

When you need to extract a value from a list that should contain exactly one element, pattern matching is the idiomatic way to handle it in functional languages. The error “unbound value c” typically occurs when you try to use a variable that wasn’t properly bound through pattern matching.

## OCaml Pattern Matching

In OCaml, use `match` to destructure the list and bind the single element to a variable:

``` ocaml
let p = ["ocaml"]

let f s = match s with
  | [c] -> print_endline c
  | _ -> print_endline "ops"

f p  (* prints: ocaml *)
```

The pattern `[c]` matches a list with exactly one element and binds that element to the variable `c`. This is where `c` gets bound, making it available in the expression `print_endline c`.

If you try to use `c` outside the match expression without binding it first, you’ll get the “unbound value” error:

``` ocaml
(* This will fail *)
let divide p1 c = p1 ^ c
if p = [c] then divide "prefix" c  (* Error: unbound value c *)
```

Instead, bind `c` through pattern matching:

``` ocaml
let divide p1 c = p1 ^ c

let result = match p with
  | [c] -> divide "prefix" c
  | _ -> "error"
```

## Scala Equivalent

Scala’s pattern matching works similarly:

``` scala
def f(s: List[String]): Unit = s match {
  case List(c) => println(c)
  case _ => println("ops")
}

val p = List("Scala")
f(p)  // prints: Scala
```

For more complex operations, you can nest the logic:

``` scala
def process(s: List[String]): String = s match {
  case List(c) => s"Found: $c"
  case Nil => "Empty list"
  case multiple => s"Got ${multiple.length} elements"
}

println(process(List("test")))      // Found: test
println(process(List()))            // Empty list
println(process(List("a", "b")))    // Got 2 elements
```

## Common Patterns

Match on list length with guards:

``` ocaml
let classify s = match s with
  | [single] -> Printf.sprintf "Single: %s" single
  | [first; second] -> Printf.sprintf "Pair: %s, %s" first second
  | lst -> Printf.sprintf "List of %d elements" (List.length lst)
```

If you need to match and validate:

``` ocaml
let safe_head s = match s with
  | [c] when String.length c > 0 -> Some c
  | [_] -> None  (* empty string *)
  | _ -> None    (* not a single-element list *)
```

The key takeaway: always bind variables through pattern matching. Trying to reference `c` before it’s bound in a match expression is what causes the error. The pattern `[c]` doesn’t check if `c` equals something—it *binds* whatever element is in that position to the name `c`.

## 2026 Best Practices and Advanced Techniques

For Pattern Matching Single-Element Lists in OCaml and Scala, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
