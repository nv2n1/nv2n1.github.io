---
title: "Handling Long Lines in Git Diff Output"
date: 2018-03-24 11:42:44 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/git-diff-with-long-lines/
---

When working with files containing long lines, `git diff` output becomes hard to read — the diff spans beyond your terminal width, forcing you to scroll horizontally or losing context entirely. While you can’t force all files to use short lines, several strategies make diff output much more manageable.

## Using Word Diff for Line-Level Changes

The `--word-diff` flag changes how `git diff` displays modifications. Instead of showing two complete lines (one deleted, one added), it highlights the specific words or segments that changed within each line:

``` bash
git diff --word-diff
```

Output format:

    [-deleted word-]{+added word+}

This is especially useful for configuration files, long strings, or sentences where only a few words changed. By default, it uses the format above, but you can also specify alternatives:

``` bash
git diff --word-diff=color      # Color-coded changes (default)
git diff --word-diff=plain      # Plain text format
git diff --word-diff=porcelain  # Machine-readable format
```

## Line Wrapping with External Pagers

To force line wrapping in your diff output, override the default pager:

``` bash
PAGER='less -S' git diff
```

The `-S` flag in `less` allows horizontal scrolling while keeping the full context visible. Alternatively, use `fold` to hard-wrap lines:

``` bash
git diff | fold -w 80 -s
```

This wraps at 80 characters on word boundaries (use `-w` to set a different width).

## Combining Approaches

For maximum readability with long lines, combine word diff with line wrapping:

``` bash
PAGER='less -S' git diff --word-diff
```

Or use a custom pager that handles both:

``` bash
git config core.pager 'less -S'
git diff --word-diff
```

## Diff-So-Fancy for Enhanced Output

Modern alternatives like `diff-so-fancy` provide syntax highlighting and automatic line wrapping without extra configuration:

``` bash
brew install diff-so-fancy  # macOS
sudo apt install diff-so-fancy  # Debian/Ubuntu

git config core.pager "diff-so-fancy | less -S"
git diff
```

## Configuring Globally

If you frequently work with long lines, set your preferred diff format in your Git config:

``` bash
git config --global core.pager 'less -S'
git config --global diff.wordDiff true
```

Then `git diff` will use word-diff mode and line-wrapping pager automatically.

## Other Useful Flags

- `git diff --stat`: Shows only a summary of changes (file names and change counts)
- `git diff --unified=3`: Adjusts context lines (default is 3); use fewer for dense diffs
- `git diff --color-words`: Like `--word-diff=color` but uses a different algorithm

Each situation is different — experiment with these options to find what works best for your workflow.

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
