---
title: "Getting Started with Linux for Developers"
date: 2015-11-29 02:20:05 +0000
layout: post
canonical: https://www.systutorials.com/notes-software-development-linux-beginners/
---

Before writing code, get comfortable with fundamental Linux commands. You’ll use these daily:

- **File operations**: `ls`, `cd`, `cat`, `less`
- **Text search**: `grep`, `ripgrep` (rg)
- **Remote access**: `ssh`, `scp`, `rsync`
- **Session management**: `tmux` or `screen` for persistent terminal sessions
- **Shell**: `bash` (default on most distributions), though `zsh` and `fish` are popular alternatives

Start with built-in documentation. Man pages are your primary reference:

``` bash
man ls
man ssh
man grep
```

Use `--help` flags for quick syntax reminders, and leverage online resources when offline docs aren’t enough.

Essential commands to bookmark early:

``` bash
man -k keyword           # Search man pages by topic
which command            # Find the full path of a command
type command             # Determine if command is built-in or external
history                  # View your command history
Ctrl+R                   # Reverse search through history (in bash/zsh)
```

## Package Management for Your Distribution

Each Linux distribution uses a different package manager. Learn the one for your chosen distro:

**Debian/Ubuntu (apt)**

``` bash
apt update
apt install git
apt search package-name
apt remove package-name
```

**RHEL/CentOS/Fedora (dnf)**

``` bash
dnf install git
dnf search package-name
dnf remove package-name
```

**Arch Linux (pacman)**

``` bash
pacman -S git
pacman -Ss package-name
pacman -R package-name
```

**openSUSE (zypper)**

``` bash
zypper install git
zypper search package-name
zypper remove package-name
```

Modern distributions also support `flatpak` and `snap` for containerized packages, but avoid these initially for development tools — native packages integrate better with build systems.

### Building Software from Source

When a package isn’t available in your distro’s repository, you’ll compile from source. Check the project’s README first, then follow these typical steps:

``` bash
tar xzf project.tar.gz
cd project
./configure
make
sudo make install
```

Modern projects use different build systems:

- **CMake**: `mkdir build && cd build && cmake .. && make && sudo make install`
- **Meson**: `meson setup builddir && meson compile -C builddir && sudo meson install -C builddir`
- **Language-specific tools**: `cargo build --release` (Rust), `go build` (Go), `python -m build` (Python)

Always check the project documentation before building — the specific steps matter.

## Text Editors and Development Environments

Your choice of editor significantly impacts workflow. Options range from simple to complex:

**Beginner-friendly**

- `nano` — minimal learning curve, suitable for quick edits
- `gedit` / `kate` — GUI editors with basic features
- **VS Code** — install via your package manager, highly configurable

**Intermediate to advanced**

- `vim` — powerful but steep learning curve; start with `vimtutor`
- `emacs` — extensible and powerful; significant investment to learn
- **JetBrains IDEs** — feature-rich but resource-intensive
- **Helix** — modern Rust-written editor gaining traction

Start simple. Master one editor rather than jumping between them. If vim seems overwhelming, use nano or VS Code until you’re ready to invest time in deeper editor mastery.

## Build Systems and Compilation

**C/C++ development**

- **Compilers**: `gcc` and `clang` are the standards
- **Debugging**: `gdb` for stepping through code, or use `valgrind` for memory debugging
- **Build tool**: `make` with `Makefile` is traditional; `cmake` is modern

**Language-specific tools**

- **Rust**: `cargo` handles everything (build, test, package)
- **Go**: `go build`, `go test`, `go run`
- **Python**: `python -m venv` for virtual environments, `pip` for packages
- **Node.js**: `npm` or `yarn` for JavaScript projects

## Practical Development Workflow

A typical code-test-debug cycle looks like this:

1.  Edit code locally in your editor
2.  Run locally to catch syntax errors and obvious bugs
3.  Compile or test: `make`, `cargo build`, `python -m pytest`, `go test`
4.  Review output and logs
5.  Iterate until working

### Remote Development

When you need to test on a server:

``` bash
# Sync local changes to remote
rsync -avz --delete src/ user@server:/app/src/

# Execute build on remote
ssh user@server "cd /app && make"

# Or use version control
git push origin main
ssh user@server "cd /app && git pull && make"
```

For longer sessions, use `tmux` on the remote server to maintain persistent environments that survive disconnects:

``` bash
ssh user@server
tmux new-session -s dev
# Now run long processes; disconnect with Ctrl+B then D
# Reconnect later with: tmux attach-session -t dev
```

## Debugging and Logging

Early debugging often means reading error messages carefully and using print statements. As you advance:

- **System-level tracing**: `strace` shows system calls; `ltrace` shows library calls
- **Performance analysis**: `perf` identifies bottlenecks
- **Log review**: `journalctl` reads systemd logs; grep through application logs
- **Structured logging**: Write logs to stdout/stderr in a parseable format (JSON works well), then use tools like `jq` to filter and analyze

Avoid ad-hoc debugging in production. Implement proper logging from the start.

## Getting Started in Practice

You don’t need to master everything immediately. Follow this path:

1.  Install a Linux distribution you’re comfortable with
2.  Learn your distro’s package manager — install a few packages to practice
3.  Choose a simple editor (nano is fine to start)
4.  Build something small — a shell script, a simple C program, a Python script
5.  Deploy it to a test environment and run it

Within a few weeks of regular work, core commands become muscle memory. The shell feels less intimidating. You’ll develop habits that make Linux development fast and productive.
