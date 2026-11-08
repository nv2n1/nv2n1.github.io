---
title: "Checking if a Path is a Block Device in Python"
date: 2018-04-02 09:09:41 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-check-whether-a-file-of-a-given-path-is-a-block-device-in-python/
---

In Linux, everything is a file—including hardware devices. Block devices like disks, SSDs, and USB drives appear as files in /dev and handle I/O in fixed-size blocks. You need reliable ways to detect them in your Python scripts, especially when automating storage operations.

## Using pathlib (Recommended)

Python 3.4+ provides `pathlib.Path.is_block_device()`, which is the modern standard:

``` python
from pathlib import Path

device = Path("/dev/sda")
if device.is_block_device():
    print("It's a block device")
else:
    print("Not a block device")
```

This returns `True` only if the path exists and is a block device. It returns `False` if the path doesn’t exist, is a regular file, directory, or another device type. `pathlib` handles path operations consistently across platforms and integrates better with contemporary Python code.

## Using os.path (Legacy)

If you’re maintaining older code, `os.path.isblockdev()` works but is less flexible:

``` python
import os

if os.path.isblockdev("/dev/sda"):
    print("It's a block device")
else:
    print("Not a block device")
```

Prefer `pathlib` for new code.

## Differentiating Device Types

Beyond block devices, you often need to distinguish between different device types:

``` python
from pathlib import Path

def check_device_type(path_str):
    p = Path(path_str)

    if p.is_block_device():
        return "block device"
    elif p.is_char_device():
        return "character device"
    elif p.is_fifo():
        return "FIFO/named pipe"
    elif p.is_socket():
        return "socket"
    elif p.is_symlink():
        return "symlink"
    elif p.is_dir():
        return "directory"
    elif p.is_file():
        return "regular file"
    else:
        return "unknown or doesn't exist"

# Examples
print(check_device_type("/dev/sda"))      # block device
print(check_device_type("/dev/null"))     # character device
print(check_device_type("/dev/stdin"))    # character device
print(check_device_type("/dev/log"))      # socket
```

## Retrieving Device Numbers

Block devices have major and minor device numbers accessible via `stat`. The major number identifies the driver type (e.g., SATA controller), while the minor number identifies the specific device:

``` python
from pathlib import Path
import stat

device = Path("/dev/sda")

if device.is_block_device():
    st = device.stat()
    major = stat.S_MAJOR(st.st_rdev)
    minor = stat.S_MINOR(st.st_rdev)
    print(f"Device: {device.name}, major: {major}, minor: {minor}")
```

For a typical system, you might see:

- `/dev/sda` (SATA disk): major 8, minor 0
- `/dev/nvme0n1` (NVMe disk): major 259, minor 0
- `/dev/loop0` (loop device): major 7, minor 0

## Validating Devices Before Raw I/O

When your script will perform raw I/O operations, validate both the device type and permissions:

``` python
from pathlib import Path
import os

def validate_block_device(device_path):
    p = Path(device_path)

    if not p.is_block_device():
        raise ValueError(f"{device_path} is not a block device")

    if not os.access(p, os.R_OK | os.W_OK):
        raise PermissionError(f"No read/write access to {device_path}")

    # Optional: Check if device is in use (mounted)
    try:
        with open("/proc/mounts", "r") as f:
            mounts = f.read()
            if device_path in mounts:
                raise RuntimeError(f"{device_path} is currently mounted")
    except FileNotFoundError:
        pass  # Not on Linux

    return True

try:
    validate_block_device("/dev/sda")
    print("Device validated for raw operations")
except (ValueError, PermissionError, RuntimeError) as e:
    print(f"Validation failed: {e}")
```

## Listing Block Devices

To enumerate all block devices on the system:

``` python
from pathlib import Path

def list_block_devices():
    dev_dir = Path("/dev")
    block_devices = [p for p in dev_dir.iterdir() if p.is_block_device()]
    return sorted(block_devices)

for device in list_block_devices():
    print(device.name)
```

For more detailed information, parse `/proc/partitions` or `/sys/block`:

``` python
from pathlib import Path

def get_block_device_size(device_name):
    """Get size in sectors from /sys/block"""
    sys_path = Path(f"/sys/block/{device_name}/size")
    if sys_path.exists():
        return int(sys_path.read_text().strip())
    return None

# Example
size = get_block_device_size("sda")
if size:
    print(f"sda size: {size} sectors ({size * 512 / (1024**3):.2f} GB)")
```

## Why This Matters

**System administration**: Custom scripts interacting with storage must distinguish between block devices and regular files. Attempting to read a raw block device as text produces garbage or errors.

**Container orchestration**: When mounting devices into containers or passing through specialized hardware, validating the device type prevents runtime failures.

**Device configuration**: Automation tools for partition management, encryption setup, or device formatting must verify they’re operating on actual block devices before executing destructive operations.

**Safety**: Always validate device paths and check mounted status before performing I/O operations, especially in automated scripts or tools running with elevated privileges. A simple typo in a device path could destroy data on the wrong disk.
