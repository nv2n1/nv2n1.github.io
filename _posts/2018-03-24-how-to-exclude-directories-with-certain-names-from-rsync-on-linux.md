---
title: "Excluding Directories by Name Pattern in rsync"
date: 2018-03-24 11:44:39 +0000
modified: 2026-04-12 16:10:20 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-exclude-directories-with-certain-names-from-rsync-on-linux/
---

When backing up with rsync, you often need to skip directories like `cache/`, `node_modules/`, or `.git/` that appear at multiple levels in your directory tree. Listing every instance individually is impractical, but rsync’s exclude patterns handle this elegantly.

## Basic exclude syntax

The simplest approach uses `--exclude` with a directory name pattern:

``` bash
rsync -avxP --exclude=cache/ /path/to/src/directory/ /path/to/dst/dir/
```

This skips any directory named `cache` at any depth. The trailing slash matters — it tells rsync to match only directories, not files with that name.

## Excluding multiple directories

Chain multiple `--exclude` flags for several patterns:

``` bash
rsync -avxP \
  --exclude=cache/ \
  --exclude=node_modules/ \
  --exclude=.git/ \
  --exclude=__pycache__/ \
  /path/to/src/directory/ /path/to/dst/dir/
```

## Using an exclude file

For complex exclusion rules, write patterns to a file and reference it with `--exclude-from`:

``` bash
cat > /tmp/rsync-excludes.txt << 'EOF'
cache/
node_modules/
.git/
.venv/
__pycache__/
*.tmp
.DS_Store
EOF

rsync -avxP --exclude-from=/tmp/rsync-excludes.txt /path/to/src/directory/ /path/to/dst/dir/
```

Each pattern on its own line. Patterns without trailing slashes match both files and directories.

## Pattern matching rules

- `cache/` — matches directories named `cache` at any level
- `*.log` — matches files ending in `.log` at any level
- `/cache/` — (leading slash) matches `cache/` only at the source root
- `src/cache/` — matches `cache/` inside `src/` directory only
- `**/*.pyc` — matches `.pyc` files at any depth

## Combine include and exclude

Use `--include` and `--exclude` together to whitelist specific paths while blocking others:

``` bash
rsync -avxP \
  --include='*.pdf' \
  --exclude='*.tmp' \
  --exclude='cache/' \
  /path/to/src/directory/ /path/to/dst/dir/
```

Order matters — rsync processes rules top-to-bottom and stops at the first match.

## Practical example: web project backup

``` bash
rsync -avxP \
  --exclude=node_modules/ \
  --exclude=.git/ \
  --exclude=.env \
  --exclude=dist/ \
  --exclude=.next/ \
  --exclude='*.log' \
  /home/user/myapp/ /backup/myapp/
```

## Verify your excludes

Always dry-run before committing to an actual backup:

``` bash
rsync -avxP --dry-run \
  --exclude=cache/ \
  /path/to/src/directory/ /path/to/dst/dir/
```

The `--dry-run` flag shows what would be transferred without making changes. Review the output to confirm the right directories are being skipped.

## Performance note

Excluding directories early in the scan saves I/O and time, especially for large directory trees. Use exclude patterns rather than relying on post-transfer cleanup.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
