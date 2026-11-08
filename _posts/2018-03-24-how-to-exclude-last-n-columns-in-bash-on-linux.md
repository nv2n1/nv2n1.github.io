---
title: "Remove the Last N Delimited Fields in Bash"
date: 2018-03-24 11:46:48 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-exclude-last-n-columns-in-bash-on-linux/
---

When processing delimited data in Bash, you often need to drop the last N fields from each line without knowing the total field count. The naive `cut -d'.' -f1` approach fails immediately when field counts vary.

Given input like:

    systemd.3.gz
    systemd.mount.3.gz
    systemd.mount.f.3.gz

You want to remove the last 2 fields (`.3.gz`) to get:

    systemd
    systemd.mount
    systemd.mount.f

## Using rev with cut

The `rev` command reverses strings, which lets `cut` work from the opposite end:

``` bash
rev | cut -d'.' -f3- | rev
```

This works because:

1.  `rev` flips each line: `systemd.mount.f.3.gz` → `zg.3.f.tnuom.metsd`
2.  `cut -d'.' -f3-` keeps fields 3 onward from the reversed string
3.  Final `rev` flips back to normal

Example:

``` bash
$ echo -e "systemd.3.gz\nsystemd.mount.3.gz\nsystemd.mount.f.3.gz" | rev | cut -d'.' -f3- | rev
systemd
systemd.mount
systemd.mount.f
```

To exclude N fields, adjust the field number in `cut`: use `f(N+1)-` to skip N fields.

## Using awk

Awk’s field splitting gives you more explicit control:

``` bash
awk -F'.' '{n=NF-2; for(i=1;i<n;i++) printf "%s.", $i; print $n}' 
```

This approach:

1.  Sets `n = NF - 2` (number of fields to keep)
2.  Prints fields 1 through n-1 with delimiters
3.  Prints the last kept field without a trailing delimiter

Example with the same input:

``` bash
$ echo -e "systemd.3.gz\nsystemd.mount.3.gz\nsystemd.mount.f.3.gz" | \
  awk -F'.' '{n=NF-2; for(i=1;i<n;i++) printf "%s.", $i; print $n}'
systemd
systemd.mount
systemd.mount.f
```

To exclude M fields instead of 2, change `NF-2` to `NF-M`.

## Handling edge cases

If lines might have fewer fields than N, add a safety check:

``` bash
awk -F'.' '{n=NF-2; if(n<1) {print; next} for(i=1;i<n;i++) printf "%s.", $i; print $n}'
```

This prints the entire line unchanged if removing N fields would result in no output.

## Performance comparison

For large files, `rev | cut | rev` is faster because both commands are compiled builtins that operate character-by-character. The awk solution is more readable and flexible if you need additional field manipulation in the same pass.

## Using parameter expansion (shell-only)

If your lines are in Bash variables, you can avoid external commands:

``` bash
line="systemd.mount.f.3.gz"
delimiter="."
# Remove last 2 fields
result="${line%${delimiter}*${delimiter}*}"
echo "$result"  # systemd.mount.f
```

This uses Bash’s `%` operator to strip from the right, but only works reliably when the delimiter appears consistently and you know the exact count to remove.

For most sysadmin tasks involving delimited data streams, stick with `rev | cut | rev` for simplicity or `awk` for complex processing.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
