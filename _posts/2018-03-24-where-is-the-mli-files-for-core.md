---
title: "Finding OCaml Core Library Interface Files"
date: 2018-03-24 08:17:55 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/where-is-the-mli-files-for-core/
---

\[md\]\
When you install Core via opam, the interface files (.mli) are stored in your OPAM switch directory. The exact path depends on your OCaml version and OPAM setup.

\## Standard Location

The `.mli` files for Core are located at:

```wp-block-code
~/.opam/$(ocaml -version | awk '{print $NF}')/lib/core/
```

where the OCaml version is part of the switch path. For example, with OCaml 5.2:

```wp-block-code
ls ~/.opam/5.2/lib/core/*.mli | head -10
```

If you use a named switch instead of the default:

```wp-block-code
opam switch list
# Then look in ~/.opam/<switch-name>/lib/core/
```

\## Finding the Path Programmatically

Use `ocamlfind` to locate the Core library directory:

```wp-block-code
ocamlfind list | grep core
ocamlfind printconf stdlib
```

Or get the exact path with:

```wp-block-code
ocamlfind query core
```

This outputs the directory containing both `.cmi` (compiled interface) and `.mli` (source interface) files.

\## Common Interface Files

Core provides interface files for all its modules. Some frequently referenced ones:

– `core.mli` — The main Core module with all re-exports\
– `list.mli` — Extended list operations\
– `option.mli` — Option type utilities\
– `string.mli` — Enhanced string functions\
– `int.mli` — Integer operations\
– `map.mli` and `set.mli` — Map and Set data structures\
– `result.mli` — Result type helpers\
– `printf.mli` — Type-safe formatting

\## Reading .mli Files in Your Editor

\*\*With Merlin/ocaml-lsp:\*\*

If you use Merlin or ocaml-lsp (for VS Code’s OCaml Platform extension), `M-x merlin-type-enclosing` or “Go to Definition” automatically opens the correct `.mli` file.

\*\*Manual lookup:\*\*

```wp-block-code
less $(ocamlfind query core)/list.mli
```

\*\*In utop:\*\*

```wp-block-code
#use "core.top";;
#show List.map;;  (* Shows the type signature *)
```

\## Core vs Core_kernel

Core has been split into multiple packages:

– \*\*core_kernel\*\* — Portable subset that works on all platforms (including JavaScript via js_of_ocaml)\
– \*\*core\*\* — Full Core, including Unix-specific functionality\
– \*\*core_unix\*\* — Unix-specific extensions (in newer versions)

The `.mli` files for each are in separate directories:

```wp-block-code
ocamlfind query core_kernel
ocamlfind query core_unix
```

For most non-Unix-specific modules (List, Option, String, Map, etc.), the interface files are in `core_kernel`.

\## Troubleshooting Missing .mli Files

\*\*”Unbound module Core”:\*\*

Make sure Core is installed in your current switch:

```wp-block-code
opam list | grep core
opam install core
```

\*\*Can’t find .mli after install:\*\*

Rebuild the package documentation:

```wp-block-code
opam reinstall core
```

\*\*Wrong switch:\*\*

Verify you’re using the right OPAM switch:

```wp-block-code
opam switch show
eval $(opam env)
```

\## Alternative: Use odoc for Browsable Docs

If you want HTML documentation instead of raw .mli files:

```wp-block-code
opam install odoc
opam doc core
```

This generates browsable HTML documentation from the .mli files with proper cross-references and search.

\## Generating Documentation for Your Project

If you’re building a library that uses Core, generate docs for your own .mli files:

```wp-block-code
# Install odoc
opam install odoc

# Build docs for your project
cd your-project
eval $(opam env)
odoc compile your_module.mli

# Or use dune to build all docs
dune build @doc
```

The generated HTML appears in `_build/default/_doc/_html/`.

\## Working with .mli Files in Practice

When developing OCaml libraries, writing .mli files is considered best practice. Here’s a typical workflow:

\*\*1. Write the interface first (.mli):\*\*

```wp-block-code
(* mylib.mli *)
val process : string -> string option
type config = { verbose: bool; max_size: int }
val make_config : verbose:bool -> max_size:int -> config
```

\*\*2. Implement it (.ml):\*\*

```wp-block-code
(* mylib.ml *)
let process input =
  if String.length input = 0 then None
  else Some (String.trim input)

type config = { verbose: bool; max_size: int }
let make_config ~verbose ~max_size = { verbose; max_size }
```

\*\*3. The .mli acts as the public API contract.\*\*\
Any value not listed in the .mli is private to the module.

This pattern — interface-driven development — is central to OCaml’s module system and helps catch errors early.
