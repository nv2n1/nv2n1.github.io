---
title: "Understanding Exit Codes in Linux and Windows"
date: 2018-03-24 08:21:21 +0000
layout: post
canonical: https://www.systutorials.com/convention-of-error-codes-on-linux-and-windows/
---

Exit codes are how programs communicate success or failure to the shell and parent processes. Understanding them is essential for writing reliable scripts and debugging applications. Linux and Windows handle these differently, so knowing both conventions matters if you work across platforms.

## Linux Exit Codes

On Linux, the convention is simple: **0 means success, 1–255 means failure**. The specific error number depends on the program, but standard system errors are defined in the `errno.h` headers.

### Standard errno Values

System error codes are declared in:

- `/usr/include/asm-generic/errno-base.h` — base errors (1–34)
- `/usr/include/asm-generic/errno.h` — extended errors

View them directly:

``` bash
cat /usr/include/asm-generic/errno-base.h
```

Or look up specific numbers with the `errno` command:

``` bash
errno 2
# ENOENT 2 No such file or directory
```

Common standard errors:

| Code | Name   | Meaning                       |
|------|--------|-------------------------------|
| 1    | EPERM  | Operation not permitted       |
| 2    | ENOENT | No such file or directory     |
| 3    | ESRCH  | No such process               |
| 4    | EINTR  | Interrupted system call       |
| 5    | EIO    | Input/output error            |
| 6    | ENXIO  | No such device or address     |
| 13   | EACCES | Permission denied             |
| 14   | EFAULT | Bad address                   |
| 16   | EBUSY  | Device or resource busy       |
| 17   | EEXIST | File exists                   |
| 22   | EINVAL | Invalid argument              |
| 28   | ENOSPC | No space left on device       |
| 32   | EPIPE  | Broken pipe                   |
| 34   | ERANGE | Numerical result out of range |

### Checking Exit Codes in Bash

Capture the last command’s exit code with `$?`:

``` bash
some_command
if [ $? -ne 0 ]; then
    echo "Command failed with code $?"
fi
```

More idiomatically, use the command directly in a conditional:

``` bash
if ! some_command; then
    echo "Command failed"
fi
```

Or check success:

``` bash
if some_command; then
    echo "Success"
else
    echo "Failed with code $?"
fi
```

For functions, use `return` to set the exit code:

``` bash
my_function() {
    if [ ! -f "$1" ]; then
        return 2  # ENOENT
    fi
    return 0
}

my_function "file.txt"
echo "Exit code: $?"
```

### Error Handling in C

Include `<errno.h>` and use `strerror()` to convert error numbers to readable messages:

``` c
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <string.h>

int fd = open("file.txt", O_RDONLY);
if (fd < 0) {
    perror("open failed");  // Automatically uses strerror()
    // Or manually:
    fprintf(stderr, "Error: %s\n", strerror(errno));
    return errno;
}
close(fd);
```

Always check the return value and `errno` immediately after the failing call, as other function calls may overwrite it.

### Error Handling in Python

Python 3 raises exceptions with errno attributes:

``` python
import errno
import os

try:
    os.remove("nonexistent.txt")
except FileNotFoundError as e:
    print(f"File not found: {e}")
except OSError as e:
    print(f"OS error {e.errno}: {e.strerror}")
```

You can also inspect errno directly:

``` python
import errno

try:
    open("protected_file.txt", "r")
except OSError as e:
    if e.errno == errno.EACCES:
        print("Permission denied")
    else:
        print(f"Error {e.errno}: {e.strerror}")
```

## Windows Exit Codes

Windows uses 0 for success but allows exit codes from 0–2147483647 (32-bit signed). Windows error codes are more complex than Unix errno values and encode additional information in their structure.

### Common Windows Error Codes

| Code | Name                    | Meaning                          |
|------|-------------------------|----------------------------------|
| 0    | ERROR_SUCCESS           | Operation completed successfully |
| 1    | ERROR_INVALID_FUNCTION  | Incorrect function               |
| 2    | ERROR_FILE_NOT_FOUND    | File not found                   |
| 3    | ERROR_PATH_NOT_FOUND    | Path not found                   |
| 5    | ERROR_ACCESS_DENIED     | Access denied                    |
| 6    | ERROR_INVALID_HANDLE    | Handle is invalid                |
| 8    | ERROR_NOT_ENOUGH_MEMORY | Not enough memory                |
| 80   | ERROR_FILE_EXISTS       | File exists                      |
| 87   | ERROR_INVALID_PARAMETER | Parameter is incorrect           |

For a comprehensive list, see the <a href="https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes" rel="nofollow noopener" target="_blank">Windows System Error Codes documentation</a>.

### Checking Exit Codes in PowerShell

Use `$LASTEXITCODE` after running a command:

``` powershell
some-command
if ($LASTEXITCODE -ne 0) {
    Write-Host "Command failed with code $LASTEXITCODE"
}
```

For native PowerShell cmdlets, check `$?` instead (boolean):

``` powershell
if (-not $?) {
    Write-Host "Cmdlet failed"
}
```

You can also use error records from `$Error`:

``` powershell
try {
    Get-Item "nonexistent.txt" -ErrorAction Stop
}
catch {
    Write-Host "Error: $($_.Exception.Message)"
    Write-Host "Exit code: $($_.Exception.HResult)"
}
```

### Error Handling in C on Windows

Use `GetLastError()` to retrieve error codes and `FormatMessage()` to convert them to readable text:

``` c
#include <windows.h>
#include <stdio.h>

HANDLE hFile = CreateFileA(
    "file.txt",
    GENERIC_READ,
    0,
    NULL,
    OPEN_EXISTING,
    FILE_ATTRIBUTE_NORMAL,
    NULL);

if (hFile == INVALID_HANDLE_VALUE) {
    DWORD dwError = GetLastError();
    LPVOID lpMsgBuf = NULL;

    FormatMessageA(
        FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
        NULL,
        dwError,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
        (LPSTR)&lpMsgBuf,
        0, NULL);

    fprintf(stderr, "Error %lu: %s\n", dwError, (char*)lpMsgBuf);
    LocalFree(lpMsgBuf);
    return dwError;
}

CloseHandle(hFile);
return 0;
```

Note: `GetLastError()` is thread-local and gets cleared by many operations, so call it immediately after failure.

## Cross-Platform Portable Code

When writing portable applications:

1.  **Don’t assume error codes match** — EACCES (13 on Unix) is `ERROR_ACCESS_DENIED` (5 on Windows)
2.  **Test on both platforms** — error handling logic may differ significantly
3.  **Use wrapper libraries** — Boost.System (C++), `errno` module (Python), or custom abstraction layers normalize error codes
4.  **Document platform-specific behavior** — if your code handles errors differently on each platform, make it explicit
5.  **Prefer exceptions over error codes** — languages like Python handle this better than C-style errno

For shell scripts targeting both systems, use conditional logic based on the platform:

``` bash
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux-specific error handling
    expected_code=2
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows error handling
    expected_code=5
fi
```

This awareness prevents subtle bugs when code runs on unexpected platforms.
