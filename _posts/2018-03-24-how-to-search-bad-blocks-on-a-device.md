---
title: "Detecting Bad Blocks on Storage Devices"
date: 2018-03-24 07:54:11 +0000
layout: post
canonical: https://www.systutorials.com/how-to-search-bad-blocks-on-a-device/
---

If you suspect a disk has bad blocks, use the `badblocks` utility to scan for them. This tool probes a device (usually a disk partition) and reports which blocks are unreliable or unreadable.

### Basic Usage

``` bash
badblocks /dev/sda1
```

This scans `/dev/sda1` from the first block to the last block on the device.

### Common Options

- `-s`: Show progress (recommended for large disks)
- `-v`: Verbose output
- `-w`: Perform a destructive write test (overwrites data — use only on blank/backup disks)
- `-n`: Non-destructive read-write test (safer, but slower)
- `-f`: Force the test even if the device appears mounted
- `-b block_size`: Specify block size in bytes (default: 4096)
- `-c blocks_at_once`: Number of blocks to test at once (default: 16)
- `-p num_passes`: Number of test passes (default: 0, runs until interrupted)
- `-t test_pattern`: Use a specific test pattern (0, 1, 2, 3, or random)
- `-e max_bad_blocks`: Stop after finding this many bad blocks
- `-o output_file`: Write bad block numbers to a file
- `-i input_file`: Read bad block list from a file

### Examples

**Non-destructive read test on a mounted partition:**

``` bash
sudo badblocks -s -n /dev/sda1
```

**Write-destructive test (warns: data will be overwritten):**

``` bash
sudo badblocks -s -w /dev/sda1
```

**Test a specific range (blocks 1000 to 5000):**

``` bash
sudo badblocks -s /dev/sda1 5000 1000
```

**Save results to a file:**

``` bash
sudo badblocks -s -o bad_blocks.txt /dev/sda1
```

### Important Considerations

- **Root access required**: `badblocks` needs root privileges to access raw device blocks.
- **Don’t run on mounted filesystems** with `-w` flag; you’ll corrupt data. Use `-n` instead for non-destructive testing on live systems.
- **Slow on large disks**: Full scans of multi-terabyte drives take hours. Consider testing specific ranges or increasing `-c` for speed.
- **Modern SSDs**: `badblocks` is primarily designed for HDD testing. Modern SSDs have built-in SMART monitoring and wear-leveling that makes traditional bad block testing less relevant.

### Integration with Filesystem Tools

After identifying bad blocks, use `fsck` with the bad block list to mark them as unusable:

``` bash
sudo fsck -l bad_blocks.txt /dev/sda1
```

Alternatively, `e2fsck` for ext2/3/4 filesystems:

``` bash
sudo e2fsck -l bad_blocks.txt /dev/sda1
```

### Checking SMART Data First

Before running `badblocks`, check your drive’s SMART status to see if the manufacturer already detected issues:

``` bash
sudo smartctl -a /dev/sda
```

This is faster and won’t risk further disk stress if the drive is already failing.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
