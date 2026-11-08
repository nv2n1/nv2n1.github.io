---
title: "How to View Partition Start and End Sectors with Parted"
date: 2018-03-24 11:55:04 +0000
layout: post
canonical: https://www.systutorials.com/how-to-list-start-and-end-sectors-of-a-partition-by-parted-in-linux/
---

By default, `parted` displays partition boundaries in bytes. To view start and end positions in sectors instead, you need to set the unit explicitly using the `unit` command.

## Using the unit command

The `unit` subcommand in parted sets the display unit for locations and sizes. The syntax is straightforward:

    parted /dev/sda unit s print

The available units are:

- `s` — sectors
- `B` — bytes
- `kB`, `MB`, `GB`, `TB` — decimal units
- `KiB`, `MiB`, `GiB`, `TiB` — binary units
- `%` — percentage of device size
- `cyl` — cylinders
- `chs` — cylinders, heads, sectors
- `compact` — megabytes for input, human-friendly output

## Example: viewing sectors

``` bash
parted /dev/sda unit s print
```

Output:

    Model: ATA ST2000DM001-1CH1 (scsi)
    Disk /dev/sda: 3907029168s
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt
    Disk Flags: 

    Number  Start        End          Size         File system  Name  Flags
     1      4096s        1229064191s  1229060096s               data
     2      1229064192s  3907029134s  2677964943s

Here, partition 1 starts at sector 4096 and ends at sector 1229064191.

## Using the interactive shell

You can also enter parted’s interactive mode and change units there:

``` bash
parted /dev/sda
(parted) unit s
(parted) print
```

This is useful when you need to run multiple commands against the same disk.

## Converting sectors to bytes

If you need to calculate byte offsets from sector numbers, multiply by the sector size. In the example above, the sector size is 512B:

- Start byte: 4096 × 512 = 2,097,152 bytes
- End byte: 1,229,064,191 × 512 = 629,024,865,792 bytes

## Practical considerations

When partitioning or resizing disks, working with sectors is often more precise than dealing with megabytes or gigabytes. Modern alignment best practices recommend:

- Start partitions at 4096-sector (2MB) boundaries for optimal performance with 4K-native storage
- Use `parted -a optimal` during creation to have parted handle alignment automatically

For scripting or automation, you can parse parted output using `--script` mode:

``` bash
parted --script /dev/sda unit s print | grep -E "^\s*[0-9]+" | awk '{print $1, $2, $3}'
```

This extracts partition numbers, start sectors, and end sectors from the output.

## Modern alternatives

While `parted` remains widely used, `fdisk` also supports sector display:

``` bash
fdisk -l /dev/sda
```

Output from fdisk already defaults to sectors and is often faster for simple queries. For programmatic access to partition information, consider reading `/proc/partitions` or using `lsblk` with JSON output:

``` bash
lsblk --json /dev/sda
```

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
