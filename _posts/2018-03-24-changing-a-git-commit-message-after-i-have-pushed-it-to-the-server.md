---
title: "Safely Rewriting Git Commit Messages After Push"
date: 2018-03-24 11:40:36 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /changing-a-git-commit-message-after-i-have-pushed-it-to-the-server/
---

If you’ve pushed a commit with a bad message, you can fix it—but the approach depends on whether others have pulled that commit yet.

## When Rewriting Is Safe

Only amend and force-push if:

- You’re the only one using the repository
- You’re absolutely certain no one else has pulled the commit yet
- Your branch protection rules allow force pushes

If your team has already pulled, amending and force-pushing will break their local copies and force them to resolve conflicts. In shared repositories, use safer alternatives instead.

## Amend the Most Recent Commit

To fix the last commit message locally:

``` bash
git commit --amend -m "Corrected commit message"
```

This rewrites only your local history. To update the remote:

``` bash
git push --force-with-lease
```

Use `--force-with-lease` instead of `-f`. It’s safer—it only pushes if your local branch matches the remote, preventing accidental overwrites if someone else pushed while you were working.

If no one has pulled yet, a plain `git push` might work. Check first:

``` bash
git log origin/main..HEAD
```

If that shows nothing, the remote is already ahead and you’ll need the force flag.

## Reword Multiple Commits

For wrong messages further back in history, use interactive rebase:

``` bash
git rebase -i HEAD~5
```

Replace `5` with however many commits back you need. Your editor opens with a list:

    pick a1b2c3d First commit
    pick d4e5f6g Wrong message here
    pick h8i9j0k Third commit

Change `pick` to `reword` for any you want to edit:

    pick a1b2c3d First commit
    reword d4e5f6g Wrong message here
    pick h8i9j0k Third commit

Save and quit. Git pauses at each `reword` commit and lets you edit the message. After you finish all of them:

``` bash
git push --force-with-lease
```

## Safer Alternatives for Shared Repos

If teammates have pulled the commit, rewriting history is disruptive. Instead:

**Create a correction commit:**

``` bash
git commit --allow-empty -m "fix: correct message from commit a1b2c3d"
```

This documents the correction without rewriting history. Reference the original commit hash in the message so it’s traceable.

**Revert and recommit:**

``` bash
git revert a1b2c3d
git commit -m "your corrected message"
```

This creates an explicit undo, making the change visible in history.

**Update in the PR/merge request:**

If the commit hasn’t merged to main yet, update the PR description or add a comment explaining the correct message. Many teams accept this as sufficient documentation.

## Verify Before You Change Anything

Before amending, check what you’re modifying:

``` bash
git log --oneline -10
git show HEAD
```

For interactive rebase, review the entire commit list in your editor before saving. Mistakes here are harder to undo.

## Recover from a Bad Force Push

If you force-pushed and need to undo, check your reflog immediately:

``` bash
git reflog
```

Output looks like:

    abc1234 HEAD@{0}: push (forced-update): refs/heads/main
    def5678 HEAD@{1}: commit (amend): old message
    ghi9012 HEAD@{2}: commit: original message

Reset to the commit you want:

``` bash
git reset --hard ghi9012
git push --force-with-lease
```

**Warning:** Reflog is local only and expires after 30-90 days by default. Don’t rely on it long-term. If your team uses a shared reflog or backup service (some platforms like GitHub keep push history), you may have more recovery options.

## Best Practices

- Use `--force-with-lease` always, never `--force` alone
- Never rewrite commits on shared branches like `main` or `develop`
- For single-developer branches or feature branches no one else uses, amending is fine
- Document controversial rewrites in commit messages or PRs
- Check branch protection rules—some block force pushes entirely
- If you’re unsure whether others have pulled, assume they have and use a safer method
