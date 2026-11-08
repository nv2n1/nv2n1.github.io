---
title: "Mastering Git Log: Essential Commands for Filtering Commits"
date: 2019-12-28 10:25:13 +0000
layout: post
canonical: https://www.systutorials.com/how-to-list-all-commits-in-a-git-repository/
---

`git log` is your primary tool for viewing repository history. These commands work across all Git hosting platforms (GitHub, GitLab, Gitea, etc.) and are essential for debugging, code review, and maintaining audit trails.

## Basic commit listing

``` bash
git log --oneline
```

Each commit appears as a single line with the abbreviated hash and message. Add `--reverse` to see oldest commits first:

``` bash
git log --oneline --reverse
```

For full details (author, date, full message body):

``` bash
git log
```

Press `q` to exit the pager. For a specific number of commits without paging:

``` bash
git log --oneline -n 20
```

## Viewing branch structure and merges

See how branches diverge and merge:

``` bash
git log --graph --all --oneline
```

The `--graph` flag draws ASCII lines showing branching points. `--all` includes all branches, not just your current one. For more context with branch labels:

``` bash
git log --graph --all --decorate --oneline
```

The `--decorate` flag labels branches and tags at each commit. For a wider, more readable graph in modern terminals:

``` bash
git log --graph --all --oneline --decorate --abbrev-commit
```

## Filtering commits by message

Search commit messages (case-insensitive by default):

``` bash
git log --grep="bug fix"
```

Use regex patterns:

``` bash
git log --grep="^Fix:" --oneline
```

Combine multiple patterns:

``` bash
git log --grep="bug" --grep="urgent" --all-match
```

The `--all-match` flag requires all patterns to match in a single commit.

## Filtering by author

``` bash
git log --author="eric"
```

Matches against author name or email. Use regex for flexible matching:

``` bash
git log --author="eric|sarah" --oneline
```

## Filtering by date range

``` bash
git log --since="2025-01-01" --until="2025-12-31"
```

Supported date formats include ISO (2025-01-15), relative (2.weeks.ago, 1.month.ago), or Unix timestamps.

## Filtering by file or directory

See only commits affecting specific paths:

``` bash
git log -- path/to/file
git log -- src/components/
```

Combine with other filters:

``` bash
git log --oneline --since="2024-06-01" -- src/api/
```

This is crucial for understanding when specific code changed and tracing feature history.

## Filtering by content changes

Find commits where specific code was added or removed:

``` bash
git log -S "function_name"
```

This finds commits where `function_name` was added or deleted, not just mentioned in commit messages. Use `-G` for regex pattern matching in diffs:

``` bash
git log -G "const.*handler.*=" -- src/
```

## Performance with large repositories

Limit history scope in monorepos and large codebases:

``` bash
git log --oneline -n 50
```

Show recent changes to a specific subtree:

``` bash
git log --oneline -n 100 -- apps/api/
```

For sparse checkouts with `git config core.sparseCheckout true`, your history still includes the full tree, but filtering to relevant directories speeds up searches.

If you regularly query a large monorepo, consider shallow clones during initial setup:

``` bash
git clone --depth=1 <repo-url>
```

Then fetch full history as needed for specific branches.

## Custom formatted output

Generate structured output for scripting or reporting:

``` bash
git log --format="%h %s %an %ad" --date=short
```

Useful format fields:

- `%h` — abbreviated commit hash
- `%H` — full commit hash
- `%s` — subject line
- `%b` — message body
- `%an` — author name
- `%ae` — author email
- `%ad` — author date
- `%ar` — author date (relative)

Export as pipe-delimited for CSV processing:

``` bash
git log --format="%H|%s|%an|%ad" --date=iso > commits.txt
```

For JSON-like output (pipe-delimited):

``` bash
git log --format="%H%n%s%n%an%n%ad" --date=iso | paste -sd '|' - - - -
```

## Viewing commit details

See what changed in a specific commit:

``` bash
git show <commit-hash>
```

Show only file statistics (files changed, insertions/deletions):

``` bash
git show --stat <commit-hash>
```

Compare two commits:

``` bash
git log <commit1>..<commit2> --oneline
```

This shows commits reachable from `commit2` but not from `commit1`.

## Practical workflows

**Code review of a feature branch:**

``` bash
git log --oneline main..feature-branch
```

Shows commits on `feature-branch` not yet merged to `main`.

**What shipped between releases:**

``` bash
git log --oneline v1.0.0..v1.1.0
```

Lists commits between two tags.

**Check your own recent work:**

``` bash
git log --author="$(git config user.name)" --oneline -20
```

**See commits by multiple team members:**

``` bash
git log --oneline --all --since="1.week.ago" --author="alice|bob|carlos"
```

**Find when a bug was introduced (bisect preparation):**

``` bash
git log -p --all -S "buggy_code" -- src/main.js
```

Shows full diffs (`-p`) of commits touching the buggy code.

**Export recent history for audit:**

``` bash
git log --format="%h|%s|%an|%ai|%d" --all --since="2025-01-01" > audit_log.txt
```
