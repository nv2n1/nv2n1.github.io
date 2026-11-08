---
title: "Creating and Managing Symbolic Links in Linux"
date: 2013-07-12 19:16:05 +0000
modified: 2026-04-11 16:41:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /playing-with-symbolic-links-on-linux/
---

Symbolic links (symlinks) are aliases that point to other files or directories. Most operations treat them transparently—programs reading or writing through a symlink behave as if working with the target directly. Understanding how to create, test, and manage them correctly is essential for system administration.

## Creating Symbolic Links

Create a basic symlink:

``` bash
ln -s ../target ./target
```

Always specify the link name explicitly to avoid ambiguity. The `-s` flag creates a symbolic link rather than a hard link.

### Absolute vs. Relative Symlinks

Use **absolute paths** for symlinks that will be accessed from different locations or when the symlink might be moved independently:

``` bash
ln -s /opt/app/config ./config
ln -s /var/log/nginx ./nginx-logs
```

Use **relative symlinks** when the target is in a predictable location relative to the symlink. This allows moving both together without breaking the link:

``` bash
ln -s ../../target ./tt
```

Relative symlinks are smaller and portable; absolute symlinks are more reliable when the symlink location changes independently of its target. Choose based on your deployment model.

## Testing for Symbolic Links in Bash

Test whether a file is a symlink using the `-L` test operator:

``` bash
if [ -L "$file" ]; then
    echo "This is a symbolic link"
fi
```

Always quote variables to handle filenames with spaces correctly.

Distinguish symlinks from regular files and directories:

``` bash
if [ -L "$file" ]; then
    echo "Symlink"
elif [ -f "$file" ]; then
    echo "Regular file"
elif [ -d "$file" ]; then
    echo "Directory"
fi
```

Test whether a symlink target exists:

``` bash
if [ -L "$file" ] && [ -e "$file" ]; then
    echo "Valid symlink"
elif [ -L "$file" ]; then
    echo "Broken symlink"
fi
```

The `-e` test returns true only if the target exists, allowing you to distinguish broken symlinks from valid ones.

## Resolving Symlink Targets

Display the raw target without resolving the chain:

``` bash
readlink ./tt
```

Get the canonical (absolute) path by resolving all symlinks in the chain:

``` bash
readlink -f ./tt
```

The `-f` flag dereferences every symlink component and returns the absolute path of the final target. Use this when symlinks point to other symlinks or when relative paths need resolving.

Get the canonical path without requiring the target to exist (useful for broken symlinks):

``` bash
readlink -e ./tt
```

The `-e` flag works like `-f` but fails gracefully if the final target doesn’t exist.

## Finding and Managing Symlinks

List all symlinks in a directory:

``` bash
find . -maxdepth 1 -type l
```

Find broken symlinks (pointing to nonexistent targets):

``` bash
find . -type l ! -exec test -e {} \; -print
```

Remove broken symlinks recursively:

``` bash
find . -type l ! -exec test -e {} \; -delete
```

Display symlink information with details:

``` bash
ls -l ./tt
```

The output shows the symlink name and its target after the arrow `->`. Add the `-i` flag to include inode numbers:

``` bash
ls -li ./tt
```

Search for symlinks pointing to a specific target:

``` bash
find . -type l | while read -r link; do
    target=$(readlink "$link")
    if [[ "$target" == *"search-term"* ]]; then
        echo "$link -> $target"
    fi
done
```

## Practical Scripting Patterns

Safely create a symlink if it doesn’t already exist:

``` bash
if [ ! -e ./tt ]; then
    ln -s ../target ./tt
fi
```

Update an existing symlink:

``` bash
ln -sfn ../new-target ./tt
```

The `-f` flag forces replacement, and `-n` prevents treating symlink arguments as directories (critical when the target is a directory).

Create a symlink idempotently (safe to run multiple times):

``` bash
ln -sfn ../target ./tt
```

This replaces any existing symlink or regular file at `./tt` without error.

Process all symlinks in a directory:

``` bash
find . -maxdepth 1 -type l | while read -r link; do
    target=$(readlink -f "$link")
    echo "$link -> $target"
done
```

Using `while read` prevents issues with spaces in filenames, unlike command substitution.

Verify symlink validity before use:

``` bash
if [ -L "$file" ] && [ -e "$file" ]; then
    echo "Valid symlink pointing to: $(readlink -f "$file")"
    # Safe to use $file
elif [ -L "$file" ]; then
    echo "Broken symlink: $(readlink "$file")"
fi
```

Batch update symlinks pointing to an old target:

``` bash
find . -type l | while read -r link; do
    target=$(readlink "$link")
    if [[ "$target" == "/old/path/"* ]]; then
        new_target="${target//\/old\/path\//\/new\/path\/}"
        ln -sfn "$new_target" "$link"
        echo "Updated: $link"
    fi
done
```

## Common Gotchas

**Directory collision**: Creating a symlink with `-s target link` when `link` is an existing directory creates `link/target` instead of replacing `link`. Use `-f` to force replacement:

``` bash
ln -sfn target link
```

**Moving targets**: Symlinks don’t update automatically when targets move. Relative symlinks break if the target moves; absolute symlinks only break if the target moves to a different absolute path. Test symlinks after moving content:

``` bash
find . -type l ! -exec test -e {} \; -print
```

**Copy operations and symlinks**: The `cp` command dereferences symlinks by default, copying the target’s contents rather than the symlink itself:

``` bash
# Copy the target's contents, not the symlink
cp ./link ./copy
```

Preserve symlinks instead:

``` bash
# Copy as symlink
cp -P ./link ./copy
```

Or use `cp -d` as shorthand for preserving symlinks while copying recursively.

**Recursive symlink chains**: Creating symlinks that form loops causes infinite recursion:

``` bash
ln -s ./a ./b
ln -s ./b ./a
# Now readlink -f ./a hangs indefinitely
```

Tools like `readlink -f` will hang on circular chains. Detect this safely:

``` bash
timeout 2 readlink -f ./a 2>/dev/null || echo "Broken or circular symlink"
```

**Archive tools and symlinks**: `tar` preserves symlinks by default. `cp -r` dereferences them, but `rsync` preserves them:

``` bash
# Preserve symlinks with rsync
rsync -a --links source/ dest/
```

**Mount points and symlinks**: Symlinks crossing filesystem boundaries work normally. Be cautious when using `-L` (dereference) flags with tools like `du` or `find`, as they can follow symlinks into unexpected filesystems and report inflated usage.
