---
title: "Using Readline in the OCaml REPL"
date: 2018-03-24 08:15:33 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /add-readline-features-in-ocaml-toplevel/
---

The default OCaml toplevel lacks basic readline features like history, line editing, and command completion. Here are the practical approaches to fix this.

## utop: Full-Featured Replacement

The best option for daily interactive OCaml work is **utop**, a replacement toplevel that provides:

- Syntax highlighting with color output
- Command completion (for identifiers, keywords, library functions)
- Parenthesis and bracket matching
- Command history with arrow keys
- Multi-line input handling
- Integration with Merlin for type information

Install it via OPAM:

``` bash
opam install utop
```

Then start it with:

``` bash
utop
```

If you use dune projects, utop integrates seamlessly:

``` bash
dune utop
```

utop reads your `.ocamlinit` file and respects your existing toplevel configuration. For most developers, this is the clear winner — the productivity gains from completion and colors alone justify the small overhead.

## rlwrap: Minimal Wrapper Approach

If you want to stick with the vanilla OCaml toplevel but add basic readline support (history, line editing, basic completion), use **rlwrap**:

``` bash
rlwrap ocaml
```

rlwrap intercepts stdin/stdout and provides GNU readline functionality to any command. Install it from your package manager:

``` bash
# Debian/Ubuntu
sudo apt install rlwrap

# RHEL/CentOS
sudo dnf install rlwrap

# macOS
brew install rlwrap
```

### Creating a Wrapper Script

For convenience, create a shell script wrapper:

``` bash
#!/bin/sh
exec rlwrap -H ~/.ocaml_history -i /usr/bin/ocaml "$@"
```

Save this as `~/bin/ocaml` (or wherever your local binaries are) and make it executable:

``` bash
chmod +x ~/bin/ocaml
```

The `-H` flag stores history in a persistent file, and `-i` adds case-insensitive completion matching. Now you get history and Ctrl+R search without installing additional OCaml packages.

### rlwrap Configuration

For more sophisticated completion, create `~/.rlwrap/ocaml_completions` with OCaml keywords and common library functions:

    let rec if then else match with fun
    List.map List.fold_left List.iter Array.map
    Printf.printf Printf.sprintf

Then use:

``` bash
rlwrap -f ~/.rlwrap/ocaml_completions ocaml
```

## Comparison

| Feature          | vanilla ocaml | rlwrap   | utop              |
|------------------|---------------|----------|-------------------|
| History          | No            | Yes      | Yes               |
| Line Editing     | No            | Yes      | Yes               |
| Colors           | No            | No       | Yes               |
| Completion       | No            | Basic    | Full              |
| Type Information | N/A           | No       | Yes (with Merlin) |
| Setup Time       | —             | \< 1 min | \< 1 min          |

## Practical Recommendation

- **Daily development**: Use **utop**. The syntax highlighting and intelligent completion pay for themselves immediately.
- **Quick scripts or testing**: Use **rlwrap ocaml** for lightweight line editing without extra dependencies.
- **Vanilla toplevel**: Only if you’re constrained by environment or need exact default behavior.

Most modern OCaml workflows rely on utop within editor integrations (VS Code, Vim, Emacs) rather than standalone toplevel sessions anyway, but for interactive exploration, utop remains the standard choice.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
