---
title: "Static Linking OCaml Programs for Better Portability"
date: 2019-06-08 03:25:21 +0000
layout: post
canonical: https://www.systutorials.com/how-to-statically-link-ocaml-programs/
---

Static linking is essential when distributing OCaml binaries across systems without managing runtime dependencies. OCaml supports two main approaches: glibc-based static linking (which retains some dynamic dependencies) and musl-based static linking (producing truly portable binaries).

## Static Linking with glibc

The simplest approach uses glibc with the `-static` flag passed to the C linker. Since OCaml compiles to native code and delegates linking to the C toolchain, this is straightforward.

Create a test program:

``` ocaml
let () = print_endline "hello world"
```

Build with static linking:

``` bash
ocamlopt -ccopt -static -o hello hello.ml
```

You’ll see a warning:

    /usr/lib/ocaml/libasmrun.a(unix.o): In function `caml_dlopen':
    (.text+0x37f): warning: Using 'dlopen' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking

This warning reveals the core limitation: functions like `dlopen()` still require glibc shared libraries at runtime, even though most of glibc is statically linked. Your binary isn’t truly portable across different glibc versions—it carries a hard dependency on the glibc ABI it was compiled against.

Verify static linking:

``` bash
ldd ./hello
# Output: not a dynamic executable
```

While `ldd` reports no dynamic dependencies, the binary will fail on systems with an incompatible glibc version.

## Static Linking with musl

For truly static binaries with zero runtime libc dependencies, use musl instead of glibc. Binaries built this way run on any Linux system regardless of libc version or availability.

Install musl tooling on Debian/Ubuntu:

``` bash
sudo apt-get install musl-tools
```

Alpine Linux includes musl by default. On other distributions, check your package manager for `musl-tools` or equivalent.

Create an opam switch with musl and static compilation enabled:

``` bash
opam switch install 4.14.1+musl+static
eval $(opam env)
opam install ocamlfind
```

Build the program:

``` bash
ocamlfind ocamlopt -ccopt -static -o hello hello.ml
```

Verify full static linking:

``` bash
ldd ./hello
# Output: not a dynamic executable
```

No warnings appear—musl doesn’t require dynamic library resolution at runtime.

## Building Projects with Dependencies

For real applications using dune and opam, configure your switch first, then let dune handle linking:

``` bash
opam switch install 4.14.1+musl+static
eval $(opam env)
opam install dune
dune build @all
```

The dune build system respects your active opam switch and applies the correct compiler flags automatically. No manual `-ccopt` flags needed.

For projects with C stubs, ensure your opam dependencies are compatible with musl. Most common libraries (core, lwt, async) work fine, but libraries wrapping system-specific functionality may need adjustment. Check the opam repository or the project’s CI for musl-compatible variants.

If you encounter build failures with specific packages, you can pin a musl-compatible fork:

``` bash
opam pin add mypackage 'git+https://github.com/fork/mypackage.git#musl-support'
```

## Cross-Compilation with Docker

Building musl binaries from a glibc system (or vice versa) is simplest with Docker. Alpine-based images provide musl by default:

``` bash
docker run --rm -v $(pwd):/src -w /src ocaml:4.14-alpine sh -c \
  'opam install . --deps-only && dune build'
```

For Debian/glibc to Alpine/musl, use Alpine’s OCaml image. For the reverse, use `debian:bookworm` or `ubuntu:24.04` with OCaml installed via apt or opam.

You can also build a reusable Dockerfile for CI/CD:

``` dockerfile
FROM ocaml:4.14-alpine
WORKDIR /build
COPY . .
RUN opam install . --deps-only && dune build
```

## Binary Size Considerations

Static binaries are significantly larger. A simple “hello world” with musl is typically 5–10MB, while a dynamically linked glibc version is 300KB. The difference matters less for complex applications with many dependencies, but it’s relevant when distributing multiple binaries.

Strip debug symbols to reduce size:

``` bash
strip ./hello
```

For production, consider `upx` or other compressors, though they add runtime decompression overhead:

``` bash
upx --best -o hello.upx hello
```

Be cautious with compression—some container registries and deployment systems may flag or decompress UPX binaries automatically.

## Choosing an Approach

**Use glibc static linking when:**

- You control the deployment environment entirely
- You need smaller binaries and can guarantee glibc version compatibility
- You’re optimizing for a specific, homogeneous system
- You don’t need to distribute binaries publicly

**Use musl static linking when:**

- You’re distributing pre-built binaries to unknown systems
- You need to run in containers, VMs, or restricted environments with unpredictable glibc versions
- You want to avoid `LD_LIBRARY_PATH` complications
- You’re building for CI/CD pipelines with varied image bases
- You need absolute portability across Linux distributions

For container deployments, cloud platforms, and public binary distribution, musl is the pragmatic choice. Modern OCaml toolchains and opam have mature musl support, and the size difference is acceptable for nearly all use cases.
