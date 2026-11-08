---
title: "Creating Unique Temporary Files in Bash"
date: 2018-03-24 11:51:10 +0000
layout: post
canonical: https://www.systutorials.com/how-to-make-a-unique-temporary-file-in-bash-on-linux/
---

Temporary files are essential for any non-trivial Bash script. Whether you’re processing data, staging changes, or handling inter-process communication, you need reliable ways to create uniquely-named files that won’t collide with other processes.

## Using mktemp

The standard and most reliable approach is `mktemp`, which generates a cryptographically random temporary filename:

``` bash
tmpfile=$(mktemp)
echo "Temporary file created at: $tmpfile"
# Use the file
rm "$tmpfile"
```

By default, `mktemp` creates files in `/tmp` with the mode `0600` (readable and writable only by the owner). This is secure — the file won’t be accessible to other users.

For a template that makes your intent clear:

``` bash
tmpfile=$(mktemp /tmp/myapp.XXXXXX)
```

The `X` characters are replaced with random alphanumeric characters. You can use more `X`s for additional entropy if you’re concerned about collisions in high-concurrency scenarios.

## Creating Temporary Directories

For scripts that need scratch space, create a temporary directory instead:

``` bash
tmpdir=$(mktemp -d)
# mkdir $tmpdir will fail if it already exists, but mktemp -d avoids that
work_file="$tmpdir/data.txt"
```

## Cleanup With Traps

Always clean up your temporary files. Use a trap to ensure cleanup even if your script exits abnormally:

``` bash
tmpfile=$(mktemp)
trap "rm -f $tmpfile" EXIT

# Your script logic here
echo "Processing data..." > "$tmpfile"

# Cleanup happens automatically on exit
```

For temporary directories, clean them recursively:

``` bash
tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

# Use the directory
cp some_data "$tmpdir/"
```

## Named Temporary Files

If you need a predictable name within a temporary directory, combine `mktemp -d` with your own naming:

``` bash
tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

input="$tmpdir/input.txt"
output="$tmpdir/output.txt"
log="$tmpdir/process.log"

# Now use these files
```

This approach keeps related temporary files organized without sacrificing uniqueness.

## Avoiding Common Mistakes

**Don’t use `$$` alone for uniqueness:**

``` bash
# Bad — PID alone can collide across multiple runs
tmpfile="/tmp/data.$$.txt"
```

Process IDs can be reused rapidly, especially in containerized environments. `mktemp` uses proper randomization.

**Don’t hardcode paths:**

``` bash
# Bad — what if /tmp is full or doesn't exist?
tmpfile="/tmp/myfile"
```

Some systems mount `/tmp` with `noexec`. Use `TMPDIR` environment variable or let `mktemp` handle it:

``` bash
# Good — respects TMPDIR environment variable
tmpfile=$(mktemp)
```

**Don’t forget quoting:**

``` bash
# Bad — if tmpfile contains spaces, the script breaks
rm $tmpfile

# Good
rm "$tmpfile"
```

## Checking mktemp Availability

On rare systems without `mktemp`, you can fall back to a less secure approach (but prefer `mktemp` everywhere modern):

``` bash
if ! command -v mktemp &> /dev/null; then
    tmpfile="/tmp/app_$$_$RANDOM"
else
    tmpfile=$(mktemp)
fi
```

## Performance Considerations

`mktemp` is extremely lightweight and suitable for creating hundreds of temporary files in a loop. However, if you’re creating thousands of files, consider batching operations:

``` bash
tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT

# Better than calling mktemp repeatedly
for i in {1..1000}; do
    datafile="$tmpdir/data_$i.txt"
    # Process using $datafile
done
```

## Integration With Other Tools

Many utilities accept file descriptors or allow you to pipe directly, avoiding temporary files altogether:

``` bash
# Instead of a temp file, use process substitution
diff <(command1) <(command2)

# Or file descriptor for some tools
exec 3> >(some_command)
```

But when you do need physical files, `mktemp` with proper traps is the standard approach that scales across every Linux distribution and macOS system.
