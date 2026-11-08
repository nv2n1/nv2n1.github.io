---
title: "OCaml Array Length Limits Explained"
date: 2018-03-24 08:17:45 +0000
modified: 2026-04-12 06:23:19 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /max-array-length-in-ocaml/
---

\[md\]
The maximum array length in OCaml is platform-dependent and can be queried at runtime using `Sys.max_array_length`:

```wp-block-code
# Sys.max_array_length;;
- : int = 4611686018427387903
```

\## Values by Platform

\*\*64-bit systems:\*\*

```wp-block-code
# Sys.max_array_length;;
- : int = 4611686018427387903
```

\*\*32-bit systems:\*\*

```wp-block-code
# Sys.max_array_length;;
- : int = 1073741823
```

Note that 32-bit OCaml support has been deprecated in recent versions. Modern OCaml distributions primarily target 64-bit architectures, and OCaml 5.0+ dropped official support for 32-bit platforms entirely.

\## Why These Limits Exist

OCaml’s array length limit stems from how the runtime represents values in memory. Arrays store a length field alongside the data, and this length is encoded in a tagged integer. On 64-bit systems, OCaml uses 63 bits for value representation (one bit reserved for tagging), giving the theoretical maximum of 2^62 – 1 elements.

The practical limit accounts for:

– The tag bit reserved by OCaml’s garbage collector
– Memory alignment requirements
– The need to distinguish between different value types

\## Memory Consumption

While the theoretical limits are enormous, you’ll hit memory constraints long before reaching `Sys.max_array_length`. Here’s the actual memory usage for OCaml arrays:

– `int array` — 8 bytes per element on 64-bit (tagged integers)
– `float array` — 8 bytes per element (unboxed in dedicated float arrays)
– `string array` — 8 bytes per pointer + string data

A float array with 100 million elements uses ~800MB. A billion elements requires ~8GB — feasible on modern hardware but beyond typical workstation workloads.

\## Practical Alternatives for Large Data

For handling datasets that approach memory limits, consider these alternatives:

\*\*Bigarrays\*\* for C-interop and memory-mapped I/O:

```wp-block-code
let big_arr = Bigarray.Array1.create Bigarray.float64 Bigarray.c_layout 100_000_000
```

Bigarrays have their own limit (`Sys.max_bigarray_length`), which is typically larger than regular arrays, and they can be memory-mapped to files for persistent storage.

\*\*Buffers for byte data:\*\*

```wp-block-code
let buf = Buffer.create 65536
Buffer.add_string buf "data"
```

\*\*Bytes for mutable byte sequences:\*\*

```wp-block-code
let b = Bytes.make 1024 '\\000'
```

\*\*Persistent data structures\*\* from libraries like Core or Base when immutability is needed:

```wp-block-code
(* Using Core_kernel *)
let arr = Array.of_list [1; 2; 3]
```

\## OCaml 5.0 Parallelism Changes

OCaml 5.0 introduced major changes to the runtime that affect array behavior in parallel contexts:

– \*\*Domains\*\* — OCaml 5’s parallelism unit. Each domain has its own minor heap but shares the major heap.
– Arrays in shared memory are accessible from multiple domains, but you need proper synchronization for mutation.
– The `Domain` module enables parallel computation on array segments:

```wp-block-code
let parallel_map f arr =
  let n = Array.length arr in
  let domain_count = Domain.recommended_domain_count () in
  let chunk_size = n / domain_count in
  let domains = Array.init domain_count (fun i ->
    let start = i * chunk_size in
    let stop = min ((i + 1) * chunk_size) n in
    Domain.spawn (fun () ->
      Array.init (stop - start) (fun j -> f arr.(start + j))
    )
  ) in
  Array.concat_map (Domain.join) domains
```

\## Check Your Actual Limits

In a running OCaml session:

```wp-block-code
let () =
  Printf.printf "Max array length: %d\n" Sys.max_array_length;
  Printf.printf "Max bigarray length: %d\n" Sys.max_bigarray_length;
  Printf.printf "System word size: %d bits\n" Sys.word_size;
  Printf.printf "OCaml version: %s\n" Sys.ocaml_version
```

For safe array allocation without exceeding available memory, validate requested sizes against both `Sys.max_array_length` and available heap space before allocation.
