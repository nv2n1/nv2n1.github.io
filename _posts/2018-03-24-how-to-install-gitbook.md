---
title: "Installing GitBook on Linux"
date: 2018-03-24 11:43:38 +0000
modified: 2026-04-12 16:05:21 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-gitbook/
---

GitBook is a tool for building documentation and ebooks from Markdown content. Here’s how to set it up on a Linux system.

## Prerequisites

You’ll need Node.js installed first. On Ubuntu/Debian:

``` bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

On Fedora/RHEL:

``` bash
sudo dnf install nodejs
```

Verify the installation:

``` bash
node --version
npm --version
```

## Installation Methods

### Using npm (Global)

The simplest approach is to install GitBook globally via npm:

``` bash
sudo npm install -g gitbook-cli
```

This installs the GitBook command-line interface, which manages different GitBook versions automatically. Test the installation:

``` bash
gitbook --version
```

### Using npm (Local Project Directory)

If you prefer to keep GitBook scoped to a specific project:

``` bash
cd /opt/your-project
npm init -y
npm install gitbook
```

Then run it via:

``` bash
npx gitbook serve
```

## Building Your First Book

Create a project directory with the required structure:

``` bash
mkdir my-book && cd my-book
gitbook init
```

This generates a `README.md` (book introduction) and `SUMMARY.md` (table of contents). Edit these files, then build:

``` bash
gitbook build
```

Output appears in the `_book/` directory. To run a local preview server:

``` bash
gitbook serve
```

Access it at `http://localhost:4000`.

## Generating Different Formats

GitBook can output to multiple formats beyond HTML. For PDF generation, install Calibre:

``` bash
sudo apt-get install calibre
```

Or on Fedora:

``` bash
sudo dnf install calibre
```

Then generate outputs:

``` bash
gitbook pdf ./ ./book.pdf
gitbook epub ./ ./book.epub
gitbook mobi ./ ./book.mobi
```

Note: If PDF generation fails, ensure Calibre’s `ebook-convert` is in your PATH:

``` bash
which ebook-convert
```

## Troubleshooting

**Command not found**: If `gitbook` isn’t recognized after global installation, add npm’s global bin directory to your PATH:

``` bash
echo 'export PATH=$(npm config get prefix)/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**Calibre issues**: Some users experience issues with newer versions of Calibre. If ebook generation fails, try downgrading or using alternative tools like Pandoc:

``` bash
sudo apt-get install pandoc
pandoc README.md -o output.pdf
```

**Outdated dependencies**: GitBook can have stale dependencies. If you encounter errors, try clearing npm cache:

``` bash
npm cache clean --force
npm install -g gitbook-cli
```

## Modern Alternatives

GitBook’s development has slowed. Consider these alternatives for new projects:

- **mdBook** (Rust-based, fast, simpler): `cargo install mdbook`
- **Hugo** (static site generator with docs theme): Better for large projects
- **Sphinx** (Python documentation generator): Industry standard for technical docs

For existing GitBook projects, the tool remains functional and worth maintaining.

## Git Workflow Tips

Effective Git usage goes beyond knowing individual commands. Consider adopting a branching strategy that suits your team size. Feature branching works well for small teams, while GitFlow or trunk-based development scales better for larger organizations.

Always write descriptive commit messages. A good commit message explains what changed and why, not just what. Use the imperative mood: “Add feature” not “Added feature”.

## Useful Git Shortcuts

Add these aliases to your Git configuration for faster daily workflows:

```wp-block-code
[alias]
    st = status -sb
    co = checkout
    br = branch -v
    lg = log --oneline --graph --decorate -20
    unstage = reset HEAD --
    amend = commit --amend --no-edit
    last = log -1 HEAD --stat
```

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
