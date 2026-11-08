---
title: "Cleaning Up Git Commit History: A Practical Guide"
date: 2018-03-28 10:10:29 +0000
layout: post
canonical: https://www.systutorials.com/how-to-clean-commit-history-of-a-repository/
---

“Cleaning” history usually means rewriting it to remove large files, sensitive data, or to squash messy commits into logical units. This is destructive—it rewrites history and affects anyone who’s cloned the repo. Only do this on branches you control or coordinate with your team first.

## git filter-repo: The Standard Tool

`git filter-repo` replaced the deprecated `git filter-branch` years ago. It’s faster, safer, and handles complex rewrites without the footguns.

Install it via your package manager:

``` bash
# Debian/Ubuntu
sudo apt install git-filter-repo

# macOS
brew install git-filter-repo

# Or from source
pip install --user git-filter-repo
```

Remove a large file from all commits:

``` bash
git filter-repo --path large-file.bin --invert-paths
```

Remove sensitive data (like an API key) from all commits:

``` bash
git filter-repo --replace-text replacements.txt
```

Where `replacements.txt` contains:

    api_key_123456789==>REDACTED

Rewrite author and committer information across the entire history:

``` bash
git filter-repo --mailmap mailmap.txt
```

Where `mailmap.txt` maps old emails to new ones:

    New Name <new@example.com> <old@example.com>
    New Name <new@example.com> Old Name <old@example.com>

**Important**: `filter-repo` rewrites all refs. After running it, you’ll need to force-push all branches:

``` bash
git push --force-with-lease origin --all
git push --force-with-lease origin --tags
```

## Interactive Rebase for Recent Commits

For squashing, rewording, or reordering commits on the current branch without affecting shared history:

``` bash
git rebase -i HEAD~5
```

This opens your editor with the last 5 commits. Commands available:

- `pick` — use this commit
- `squash` (or `s`) — meld into previous commit
- `reword` (or `r`) — keep changes, edit the message
- `fixup` (or `f`) — like squash, but discard the log message
- `drop` (or `d`) — remove the commit

After editing, save and exit. Git will apply the changes. If conflicts occur, resolve them and run `git rebase --continue`.

**Use this only for unpushed commits or feature branches.** Don’t rebase shared history without team agreement.

## BFG Repo-Cleaner for Quick Removals

If you just need to yank a huge file or a secret from history, BFG is simpler than crafting a `filter-repo` command:

``` bash
# Remove a file from all commits
bfg --delete-files large-file.bin

# Remove a folder
bfg --delete-folders node_modules

# Replace sensitive strings
bfg --replace-text secrets.txt
```

BFG is faster for simple cases and less error-prone if you don’t need fine-grained control.

## Safe Force Pushing

Rewriting history always requires a force push. Use `--force-with-lease` instead of `--force`:

``` bash
git push --force-with-lease origin branch-name
```

`--force-with-lease` checks that no one else has pushed to the branch since your last fetch. If they have, the push is rejected. This prevents accidentally overwriting teammates’ work.

Standard `--force` blindly overwrites everything and should be avoided in shared repos.

## Before You Clean History

- **Back up the original refs**: `git for-each-ref > .git-refs.backup`
- **Notify your team**: If this is a shared repo, let people know history is being rewritten
- **Test on a clone**: Run the command on a test clone first
- **Verify the result**: Check that the right commits were removed and no data was accidentally lost

If something goes wrong on a personal branch, you can recover from the reflog:

``` bash
git reflog
git reset --hard <commit-hash>
```

## When NOT to Clean History

Don’t rewrite history on:

- The main/master branch of a shared repository
- Long-lived branches with multiple contributors
- Public repositories unless absolutely necessary (security breach, GDPR, etc.)

For most teams, it’s safer to just accept messy history or create a new repo with a clean start.
