---
title: "Serial Port Programming with Win32 API"
date: 2013-07-12 16:47:44 +0000
modified: 2026-04-11 17:16:28 +0000
author: "Eric Ma"
layout: post
categories: [web-development]
canonical: /com-port-programming-in-win32/
---

Serial communication remains essential for embedded systems, microcontroller programming, and legacy hardware integration. The Win32 API provides direct control over COM ports through a straightforward set of functions: `CreateFile()` to open the port, `GetCommState()` and `SetCommState()` to configure parameters, and `ReadFile()`/`WriteFile()` for I/O operations.

## Opening the COM Port

Start by opening the port with appropriate access flags:

``` c
HANDLE hCOM = CreateFile(
    "COM1",
    GENERIC_READ | GENERIC_WRITE,
    0,
    NULL,
    OPEN_EXISTING,
    0,
    NULL
);

if (hCOM == INVALID_HANDLE_VALUE) {
    fprintf(stderr, "Failed to open COM1: %lu\n", GetLastError());
    return 1;
}
```

Port names follow specific conventions: COM1 through COM9 can be opened directly, but COM10 and higher require the `\\.\` prefix (e.g., `\\.\COM10`). Always validate the handle against `INVALID_HANDLE_VALUE` before proceeding.

On modern Windows systems, COM ports are frequently virtual (USB-to-serial adapters, Bluetooth devices, etc.), so the actual port number may differ from what you expect. Enumerate available ports programmatically using WMI or by querying the registry:

``` c
// Using WMI to find COM ports
// Alternatively, check HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM
```

Device Manager shows port assignments, but for automated detection, WMI queries or registry enumeration are more reliable.

## Configuring Port Parameters

Initialize and configure the DCB (Device Control Block) structure with baud rate, data bits, parity, and stop bits:

``` c
DCB dcb;
ZeroMemory(&dcb, sizeof(dcb));
dcb.DCBlength = sizeof(dcb);

if (!GetCommState(hCOM, &dcb)) {
    fprintf(stderr, "Failed to read COM port state: %lu\n", GetLastError());
    CloseHandle(hCOM);
    return 1;
}

dcb.BaudRate = CBR_115200;
dcb.ByteSize = 8;
dcb.Parity = NOPARITY;
dcb.StopBits = ONESTOPBIT;
dcb.fDsrSensitivity = FALSE;
dcb.fOutxCtsFlow = FALSE;
dcb.fOutxDsrFlow = FALSE;
dcb.fDtrControl = DTR_CONTROL_ENABLE;
dcb.fRtsControl = RTS_CONTROL_ENABLE;

if (!SetCommState(hCOM, &dcb)) {
    fprintf(stderr, "Failed to configure COM port: %lu\n", GetLastError());
    CloseHandle(hCOM);
    return 1;
}
```

**Critical requirements:**

- Always initialize DCB with `ZeroMemory()` and set `DCBlength` before calling `GetCommState()`
- Use the `CBR_*` constants for baud rates: `CBR_9600`, `CBR_115200`, `CBR_921600`
- `CBR_115200` is standard for modern microcontroller boards; verify your device’s specification

**Flow control configuration:**
The `fDtrControl` and `fRtsControl` flags manage DTR and RTS lines. Set both to `ENABLE` when communicating with devices that require handshaking. For devices without hardware flow control, use `DTR_CONTROL_DISABLE` and `RTS_CONTROL_DISABLE`:

``` c
// For hardware flow control
dcb.fDtrControl = DTR_CONTROL_ENABLE;
dcb.fRtsControl = RTS_CONTROL_ENABLE;

// For devices without flow control
dcb.fDtrControl = DTR_CONTROL_DISABLE;
dcb.fRtsControl = RTS_CONTROL_DISABLE;
```

**Additional DCB flags:**

- `fInX` / `fOutX`: Enable XON/XOFF software flow control if your device requires it
- `fAbortOnError`: Set to TRUE to halt reads/writes on parity or framing errors
- `fNull`: Set to TRUE to discard null bytes from input
- `fErrorChar`: Set to TRUE and configure `ErrorChar` to replace characters with errors

## Setting Timeouts

Configure `COMMTIMEOUTS` to control blocking behavior:

``` c
COMMTIMEOUTS timeouts;
ZeroMemory(&timeouts, sizeof(timeouts));

timeouts.ReadIntervalTimeout = 50;
timeouts.ReadTotalTimeoutMultiplier = 0;
timeouts.ReadTotalTimeoutConstant = 100;
timeouts.WriteTotalTimeoutMultiplier = 0;
timeouts.WriteTotalTimeoutConstant = 100;

if (!SetCommTimeouts(hCOM, &timeouts)) {
    fprintf(stderr, "Failed to set timeouts: %lu\n", GetLastError());
    CloseHandle(hCOM);
    return 1;
}
```

All timeout values are in milliseconds. Understand each field:

- `ReadIntervalTimeout`: Maximum interval between consecutive received bytes. When exceeded, `ReadFile()` returns with available data. Set to `MAXDWORD` for non-blocking behavior
- `ReadTotalTimeoutConstant` + `ReadTotalTimeoutMultiplier × bytes_requested`: Total time allowed for the read operation
- Write timeouts function identically

**Common scenarios:**

``` c
// Non-blocking reads (return immediately with available data)
timeouts.ReadIntervalTimeout = MAXDWORD;
timeouts.ReadTotalTimeoutMultiplier = 0;
timeouts.ReadTotalTimeoutConstant = 0;

// Blocking mode with 500ms total timeout
timeouts.ReadIntervalTimeout = 0;
timeouts.ReadTotalTimeoutMultiplier = 10;
timeouts.ReadTotalTimeoutConstant = 500;

// Balance: return after 50ms of inactivity OR 200ms total
timeouts.ReadIntervalTimeout = 50;
timeouts.ReadTotalTimeoutMultiplier = 1;
timeouts.ReadTotalTimeoutConstant = 200;
```

Choose timeouts based on your baud rate and expected message size. High baud rates allow shorter timeouts; slow devices need longer waits.

## Reading and Writing Data

Perform I/O with proper error checking:

``` c
// Write
const char data_out[] = "ABC";
DWORD bytes_written = 0;

if (!WriteFile(hCOM, data_out, sizeof(data_out) - 1, &bytes_written, NULL)) {
    fprintf(stderr, "Write failed: %lu\n", GetLastError());
}

if (bytes_written != sizeof(data_out) - 1) {
    fprintf(stderr, "Incomplete write: %lu of %lu bytes\n", 
            bytes_written, sizeof(data_out) - 1);
}

// Read
char buffer[256];
DWORD bytes_read = 0;

if (!ReadFile(hCOM, buffer, sizeof(buffer), &bytes_read, NULL)) {
    DWORD err = GetLastError();
    if (err != ERROR_TIMEOUT) {
        fprintf(stderr, "Read failed: %lu\n", err);
    }
    bytes_read = 0;
}

if (bytes_read > 0) {
    printf("Received %lu bytes\n", bytes_read);
    // Process buffer
}
```

**Key points:**

- Check return value and compare bytes transferred against the requested amount
- Short writes/reads occur when buffers fill, especially at lower baud rates
- `ERROR_TIMEOUT` is not a fatal error; handle it gracefully
- For binary or structured data, accumulate reads until a complete message is available

## Robust Data Transfer

Wrap operations in helper functions that handle incomplete transfers:

``` c
BOOL SendData(HANDLE hCOM, const void *data, DWORD length) {
    DWORD total_written = 0;

    while (total_written < length) {
        DWORD written = 0;

        if (!WriteFile(hCOM, (BYTE*)data + total_written, 
                      length - total_written, &written, NULL)) {
            DWORD err = GetLastError();
            if (err != ERROR_TIMEOUT) {
                fprintf(stderr, "WriteFile error: %lu\n", err);
                return FALSE;
            }
            // Continue on timeout, retry
            Sleep(10);
            continue;
        }

        if (written == 0) {
            fprintf(stderr, "Write timeout or port closed\n");
            return FALSE;
        }

        total_written += written;
    }

    return TRUE;
}

BOOL ReceiveData(HANDLE hCOM, void *buffer, DWORD max_length, DWORD *bytes_read) {
    if (!ReadFile(hCOM, buffer, max_length, bytes_read, NULL)) {
        DWORD err = GetLastError();
        if (err != ERROR_TIMEOUT) {
            fprintf(stderr, "ReadFile error: %lu\n", err);
            return FALSE;
        }
        *bytes_read = 0;
    }
    return TRUE;
}
```

This pattern ensures all data is transmitted even when the OS buffers partial writes. Decide retry behavior based on your application’s requirements.

## Clearing the Port Buffer

Before starting communication or after detecting errors, purge pending data:

``` c
BOOL ClearComm(HANDLE hCOM) {
    return PurgeComm(hCOM, PURGE_RXCLEAR | PURGE_TXCLEAR);
}
```

This discards buffered input and output, essential when recovering from framing errors or synchronizing with a device after reconnection.

## Cleanup

Always close the port handle:

``` c
if (hCOM != INVALID_HANDLE_VALUE) {
    CloseHandle(hCOM);
}
```

Use RAII patterns (guard classes in C++) or structured exception handling to guarantee cleanup on error paths.

## Event-Driven I/O

For responsive handling of multiple ports or integration with event loops, use overlapped I/O:

``` c
// Enable event notification
SetCommMask(hCOM, EV_RXCHAR | EV_TXEMPTY);

// Wait for events
DWORD mask = 0;
if (!WaitCommEvent(hCOM, &mask, NULL)) {
    fprintf(stderr, "WaitCommEvent failed: %lu\n", GetLastError());
} else {
    if (mask & EV_RXCHAR) {
        // Data available, read it
    }
    if (mask & EV_TXEMPTY) {
        // Transmit buffer empty
    }
}
```

This approach eliminates polling and allows your application to wait on multiple events simultaneously with `WaitForMultipleObjects()`. For multithreaded designs, combine this with overlapped I/O handles passed to I/O completion ports.
