---
title: "Managing Git Submodules: Add, Update, and Remove"
date: 2014-05-29 12:04:56 +0000
modified: 2026-04-11 16:22:32 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /git-submodule-cheat-sheet/
---

Git submodules let you keep external repositories as subdirectories within your project while maintaining separate commit histories. They’re useful for managing dependencies, shared libraries, or multi-repo projects—but they require explicit commands to work properly.

## Adding a Submodule

To add a submodule to your repository:

``` bash
git submodule add https://github.com/user/repo.git ./path/to/submodule
```

This creates or updates `.gitmodules` and clones the repository into the specified path. The parent repo tracks only the specific commit the submodule points to, not its entire history.

To track a specific branch instead of the default:

``` bash
git submodule add -b main https://github.com/user/repo.git ./path/to/submodule
```

To pin a submodule to a specific commit or tag immediately:

``` bash
cd ./path/to/submodule
git checkout v1.2.3
cd ..
git add ./path/to/submodule
git commit -m "Pin submodule to v1.2.3"
git push
```

## Cloning Repositories with Submodules

By default, `git clone` doesn’t fetch submodule contents. Clone with submodules included:

``` bash
git clone --recursive https://github.com/user/repo.git
```

If you’ve already cloned without `--recursive`, initialize and fetch all submodules:

``` bash
git submodule update --init --recursive
```

For a single submodule:

``` bash
git submodule update --init ./path/to/submodule
```

For faster cloning of repositories with large or many submodules, use a shallow clone:

``` bash
git clone --recursive --depth 1 https://github.com/user/repo.git
```

## Updating Submodules

Fetch and merge the latest changes from each submodule’s remote tracking branch:

``` bash
git submodule update --recursive --remote
```

This updates submodules to the latest commit on their configured branch. To rebase instead of merge:

``` bash
git submodule update --recursive --remote --rebase
```

Update a single submodule:

``` bash
git submodule update --remote ./path/to/submodule
```

## Running Commands Across Submodules

The `foreach` command executes operations in each submodule:

``` bash
git submodule foreach --recursive git pull
```

Check out a specific branch in all submodules:

``` bash
git submodule foreach --recursive git checkout main
```

Combine multiple operations:

``` bash
git submodule foreach --recursive 'git checkout main && git pull'
```

Get the path and status of each submodule:

``` bash
git submodule foreach --recursive pwd
```

## Updating Submodule References in Parent Repo

When you update which commit a submodule points to, commit that change to the parent repository:

``` bash
cd ./path/to/submodule
git checkout <commit-or-tag>
cd ..
git add ./path/to/submodule
git commit -m "Update submodule to v1.5.0"
git push
```

Team members will receive the updated reference when they pull. They should then run `git submodule update --recursive` to sync their local submodules.

## Removing a Submodule

Remove a submodule completely:

``` bash
git submodule deinit -f ./path/to/submodule
git rm -f ./path/to/submodule
git commit -m "Remove submodule"
git push
```

The `deinit` command unregisters the submodule, and `git rm` deletes the directory and its `.gitmodules` entry. The `-f` flag forces removal if the submodule has uncommitted changes.

Team members who pull the removal should clean up their local submodule directory if it persists:

``` bash
rm -rf .git/modules/path/to/submodule
```

## Viewing Submodule Status

See which submodules exist and their current commit:

``` bash
git config --file .gitmodules --get-regexp path
```

Check submodule status in your working directory:

``` bash
git submodule status
```

Output shows the commit hash and path for each submodule. A `+` prefix indicates uncommitted changes; a `-` prefix indicates the submodule isn’t initialized.

## Common Issues

**Detached HEAD in submodule**: After updating, submodules check out a specific commit rather than a branch. To work on a branch:

``` bash
cd ./path/to/submodule
git checkout main
cd ..
```

**Uncommitted submodule changes**: Modifications inside a submodule stay in that submodule’s repo—they don’t affect the parent repo unless you explicitly push from within the submodule. Always remember to commit and push submodule changes separately.

**`.gitmodules` merge conflicts**: If two branches modify submodule entries differently, manually resolve the conflict in `.gitmodules`, then:

``` bash
git add .gitmodules
git commit
```

**Submodule appears as untracked directory**: This usually means the submodule wasn’t properly initialized. Run:

``` bash
git submodule update --init --recursive
```

**Accidental submodule additions**: If you added a submodule by mistake, remove it using the deletion commands above before pushing.
