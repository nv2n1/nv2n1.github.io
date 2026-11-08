---
title: "Find the K Largest Files in a Linux Directory"
date: 2018-03-24 08:20:28 +0000
layout: post
canonical: https://www.systutorials.com/how-to-find-top-k-largest-files-in-a-directory-on-linux/
---

When a disk fills up or you’re doing a cleanup pass, finding the biggest files quickly saves a lot of time. Here are the practical approaches on Linux.

### Top 10 largest files in the current directory

``` bash
du -ah --max-depth=1 | sort -rh | head -n 10
```

Breaking this down:

- `du -ah` shows sizes for all files and directories in human-readable format
- `--max-depth=1` limits output to one level deep (not recursive)
- `sort -rh` sorts by human-readable size, largest first
- `head -n 10` takes the top 10

Change `10` to whatever K you need. This is fast for shallow directory structures but won’t recurse into subdirectories.

### Recursive search across the entire tree

To find the largest files anywhere under a directory:

``` bash
find . -type f -printf '%s %p\n' | sort -rn | head -n 20 | awk '{printf "%.1fMB\t%s\n", $1/1048576, $2}'
```

This approach is cleaner than piping through `du` because:

- `find -printf '%s %p\n'` outputs size in bytes and path — no subprocess overhead
- `sort -rn` sorts numerically (more reliable with large files)
- `awk` formats the output in MB for readability

Output looks like:

    2543.5MB    ./backups/old-vm.iso
    1024.2MB    ./videos/recording.mp4
    512.8MB ./logs/application.log

### Excluding specific directories

Skip `.git`, `node_modules`, cache directories, etc.:

``` bash
find . -type f \
  -not -path './.git/*' \
  -not -path './node_modules/*' \
  -not -path './.cache/*' \
  -printf '%s %p\n' | sort -rn | head -n 20 | \
  awk '{printf "%.1fMB\t%s\n", $1/1048576, $2}'
```

You can chain as many `-not -path` filters as needed. This is essential when scanning application directories where cache or dependency directories can dominate the results.

### Finding files larger than a specific size

Instead of top-K, sometimes you want all files over a threshold:

``` bash
find . -type f -size +500M -printf '%s %p\n' | sort -rn | \
  awk '{printf "%.1fMB\t%s\n", $1/1048576, $2}'
```

Useful size units: `+1G` (over 1GB), `+100M`, `+10k`. Use `-` for smaller than.

### Whole filesystem scan

To find the largest files anywhere on the system (requires root):

``` bash
sudo find / -type f -printf '%s %p\n' 2>/dev/null | sort -rn | head -n 20 | \
  awk '{printf "%.2fGB\t%s\n", $1/1073741824, $2}'
```

The `2>/dev/null` suppresses permission errors on directories you can’t read. Be patient — this can take minutes on large systems with many files. Consider restricting to specific mount points: `find /home /var -type f ...` instead.

### Interactive exploration with ncdu

For manual cleanup work, command-line tools are tedious. `ncdu` gives you an interactive tree view where you can drill down and delete directly:

``` bash
# Install
sudo apt install ncdu      # Debian/Ubuntu
sudo dnf install ncdu      # Fedora/RHEL/AlmaLinux
sudo pacman -S ncdu        # Arch

# Run
ncdu /path/to/directory
```

Navigate with arrow keys, press `d` to delete, `q` to quit. Much faster for ad-hoc cleanup than parsing output from find or du. It also handles symlinks intelligently and shows actual disk usage vs. apparent size.

### Performance considerations

- For a single directory level, `du -ah --max-depth=1` is fastest
- For recursive scans, `find -printf` with `sort -rn` beats `du -exec` — fewer processes spawned
- On very large directories (100k+ files), even `sort` can be slow. Pipe to `head -n K` as early as possible
- If you’re scripting, use byte sizes in sort (`sort -rn`) rather than human-readable — it’s predictable and faster
- On networked or slow storage, `du` can thrash; `find -printf` is more responsive for initial results
