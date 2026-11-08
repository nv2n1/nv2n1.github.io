---
title: "How to Revert a Single File to a Previous Commit"
date: 2018-03-24 08:19:52 +0000
modified: 2026-04-12 16:10:01 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-revert-only-one-file-back-to-a-revision-or-commit/
---

You’ve accidentally broken a file and need to restore it from an earlier commit without touching anything else in your repository. Here’s how.

### Restore a file to a specific commit

To restore `my_file.name` to its state at a specific commit:

``` bash
git checkout commit_sha1 my_file.name
```

Replace `commit_sha1` with the actual commit hash. You can find it using `git log`:

``` bash
git log --oneline my_file.name
```

### Using relative commit references

Instead of a full commit hash, you can reference commits relative to HEAD:

``` bash
git checkout HEAD~4 my_file.name    # 4 commits ago
git checkout HEAD~1 my_file.name    # previous commit
git checkout HEAD^ my_file.name     # equivalent to HEAD~1
```

Or reference relative to a branch:

``` bash
git checkout master~3 my_file.name  # 3 commits back on master
git checkout main~2 my_file.name    # 2 commits back on main
```

### Restore to current branch

To discard local changes and restore the file from your current branch (typically master or main):

``` bash
git checkout my_file.name
```

This is equivalent to:

``` bash
git checkout HEAD my_file.name
```

### What actually happens

When you run these commands, git:

1.  Retrieves the file from the specified commit
2.  Places it in your working directory
3.  Stages the change (adds it to the index)

You still need to commit this change:

``` bash
git add my_file.name
git commit -m "Restore my_file.name to previous version"
```

### Checking the file first

Before committing, verify the restored file is correct:

``` bash
git diff HEAD my_file.name
```

Or view it without checking it out:

``` bash
git show commit_sha1:my_file.name
```

### Common variations

**Restore multiple files from the same commit:**

``` bash
git checkout commit_sha1 file1.txt file2.txt file3.txt
```

**Restore all files to a previous commit** (rarely needed, but possible):

``` bash
git checkout commit_sha1 .
```

**Use `git restore` (modern alternative):**

Git 2.23+ introduced `git restore` as a clearer alternative:

``` bash
git restore --source=commit_sha1 my_file.name
```

This is functionally identical to `git checkout` but has clearer semantics — checkout is primarily for switching branches, while restore explicitly restores files.

**Using `git reset` for unstaged changes:**

If you’ve only modified the file locally but haven’t committed bad changes:

``` bash
git reset my_file.name       # unstages changes
git checkout my_file.name    # discards local modifications
```

Or in one step:

``` bash
git restore my_file.name
```

### Troubleshooting

**File not found error:** The file may not have existed at that commit. Check the commit:

``` bash
git ls-tree -r commit_sha1 | grep my_file.name
```

**Wrong commit restored:** You can undo the restoration before committing:

``` bash
git reset HEAD my_file.name
git checkout my_file.name
```

Then try again with the correct commit reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
