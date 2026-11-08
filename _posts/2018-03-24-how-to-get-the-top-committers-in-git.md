---
title: "Identifying Top Contributors in Git Repositories"
date: 2018-03-24 11:49:47 +0000
modified: 2026-04-12 16:04:21 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-get-the-top-committers-in-git/
---

To identify the developers who’ve contributed the most commits to a repository, use `git log` with some text processing:

``` bash
git log --format='%aN' | sort | uniq -c | sort -rn
```

This returns a sorted list with commit counts and author names:

        247 Paul Phillips
         45 Dale Wijnand
         12 Yamashita Yuu
         10 Gilles Cornu
          8 Josh Suereth
          5 Mark Canlas
          3 Paul Phillips
          2 Jason Zaugg

## Breaking Down the Command

- `git log --format='%aN'` — Extract author names from commit history. The `%aN` format shows the author’s name (not email).
- `sort` — Group identical names together.
- `uniq -c` — Count occurrences of each name.
- `sort -rn` — Sort numerically in reverse order (highest counts first).

## Including Email Addresses

If you need email addresses alongside names for disambiguation:

``` bash
git log --format='%aN <%aE>' | sort | uniq -c | sort -rn
```

Output:

        247 Paul Phillips <paulp@improving.org>
         45 Dale Wijnand <dale.wijnand@gmail.com>
         12 Yamashita Yuu <yamashita@geishatokyo.com>

## Filtering by Date Range

To analyze contributions over a specific period:

``` bash
git log --since="2024-01-01" --until="2024-12-31" --format='%aN' | sort | uniq -c | sort -rn
```

## Top N Contributors

Show only the top 10 contributors:

``` bash
git log --format='%aN' | sort | uniq -c | sort -rn | head -10
```

## Analyzing Specific Branches or Paths

Limit analysis to a particular branch:

``` bash
git log branch-name --format='%aN' | sort | uniq -c | sort -rn
```

Or to a specific directory:

``` bash
git log --format='%aN' -- src/components | sort | uniq -c | sort -rn
```

## Using Git’s Built-in Shortlog

Git provides a dedicated command for this task:

``` bash
git shortlog -sn
```

The `-s` flag suppresses individual commit details and shows only counts, while `-n` sorts numerically. Output matches the manual method but is cleaner:

       247  Paul Phillips
        45  Dale Wijnand
        12  Yamashita Yuu

Add `--email` to include addresses:

``` bash
git shortlog -sne
```

The `shortlog` command is generally preferred since it’s purpose-built, handles edge cases better, and respects `.mailmap` configuration for normalizing duplicate author identities.

## Handling Author Name Variations

If the same person committed under different name/email combinations, create a `.mailmap` file in your repository root:

    Correct Name <correct@email.com> Alternate Name <alt@email.com>
    Correct Name <correct@email.com> <old@email.com>

Both `git log` and `git shortlog` will then consolidate commits under the canonical identity.

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
