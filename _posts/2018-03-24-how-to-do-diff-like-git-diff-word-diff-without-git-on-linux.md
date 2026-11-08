---
title: "Comparing Files Line-by-Line on Linux Without Git"
date: 2018-03-24 11:48:58 +0000
modified: 2026-04-12 16:04:28 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-do-diff-like-git-diff-word-diff-without-git-on-linux/
---

The `git diff --word-diff` output is clean and readable for tracking changes at the word level instead of line-by-line. If you need that functionality outside a git repository—or just want a standalone tool—`wdiff` is purpose-built for exactly this.

## Using wdiff for word-level diffs

`wdiff` compares two files word by word, where a word is defined as any sequence of characters separated by whitespace. Install it on most distributions:

``` bash
sudo apt install wdiff      # Debian/Ubuntu
sudo dnf install wdiff      # Fedora/RHEL
sudo pacman -S wdiff        # Arch
```

Basic usage is straightforward:

``` bash
wdiff file1.txt file2.txt
```

The output marks deletions with `[-` and `]` and additions with `{+` and `+}`. This makes it easy to spot what changed without scanning entire lines.

## Adding color output

While `wdiff` is functional, the default monochrome output lacks visual appeal. Pipe it through `colordiff`, a Perl-based wrapper that adds syntax highlighting to diff output:

``` bash
sudo apt install colordiff
wdiff file1.txt file2.txt | colordiff
```

For longer diffs, use a pager with color support:

``` bash
wdiff file1.txt file2.txt | colordiff | less -R
```

The `-R` flag tells `less` to interpret color escape sequences properly.

## Practical examples

Compare two configuration files to see what parameters changed:

``` bash
wdiff /etc/nginx/nginx.conf.bak /etc/nginx/nginx.conf | colordiff | less -R
```

Check differences in log entries word by word:

``` bash
wdiff syslog.old syslog.new | colordiff
```

## Alternative: unified word diff output

If you prefer a more unified format similar to `git diff --word-diff=unified`, you can use `wdiff` with the `-u` option to get context:

``` bash
wdiff -u file1.txt file2.txt | colordiff
```

## Combining with other tools

For even more control, pipe `wdiff` output through `grep` to filter for specific changes:

``` bash
wdiff file1.txt file2.txt | grep -E '\[-|\{\+' | colordiff
```

Or save the diff to a file for review:

``` bash
wdiff file1.txt file2.txt | colordiff > changes.txt
```

## Performance considerations

For very large files (\>100MB), `wdiff` can be slow since it tokenizes the entire file into words. In those cases, `diff` with the `--color=auto` option may be more practical, though less granular:

``` bash
diff --color=auto file1.txt file2.txt
```

For source code comparisons, `git diff` remains superior if the files are in a repository, but for one-off comparisons outside version control, `wdiff` + `colordiff` provides a reliable, focused alternative.

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
