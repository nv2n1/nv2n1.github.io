---
title: "Finding and Controlling Windows with the Win32 API"
date: 2013-07-12 16:47:42 +0000
layout: post
canonical: https://www.systutorials.com/send-messages-to-other-windows/
---

Use `FindWindowW()` to locate a window by class name or title:

``` c
HWND wnd = FindWindowW(NULL, L"Calculator");
if (wnd == NULL) {
    wprintf(L"Window not found\n");
    return 1;
}
```

The first parameter is the window class name (NULL to skip). The second is the window title. Always use wide-character versions (`FindWindowW()`, `GetWindowTextW()`) for Unicode compatibility—ANSI variants like `FindWindowA()` fail with non-ASCII characters and are legacy cruft at this point.

Window titles vary by system locale and application language. On Chinese systems, Calculator appears as “计算器” rather than “Calculator”. For robust automation across locales, query the window class name instead:

``` c
wchar_t className[256];
GetClassNameW(wnd, className, sizeof(className));
// Compare against known class names like "CalcFrame"
if (wcscmp(className, L"CalcFrame") == 0) {
    wprintf(L"Found calculator\n");
}
```

Use Spy++ (included with Visual Studio), Winspector, or the newer <a href="https://github.com/KeyboardInterrupt/WindowDetective" rel="nofollow noopener" target="_blank">Window Detective</a> to inspect window hierarchies and actual class names before writing code.

## Enumerating Child Windows and Controls

Once you have a window handle, traverse its child windows:

``` c
HWND childWnd = GetWindow(wnd, GW_CHILD);
while (childWnd != NULL) {
    int textLen = GetWindowTextLengthW(childWnd);
    wchar_t* buffer = NULL;

    if (textLen > 0) {
        buffer = (wchar_t*)malloc((textLen + 1) * sizeof(wchar_t));
        GetWindowTextW(childWnd, buffer, textLen + 1);
    }

    int ctrlId = GetDlgCtrlID(childWnd);

    if (buffer) {
        wprintf(L"Control: %ls | ID: %d\n", buffer, ctrlId);
        free(buffer);
    }

    childWnd = GetNextWindow(childWnd, GW_HWNDNEXT);
}
```

Always query `GetWindowTextLengthW()` first to allocate the correct buffer size. For deeper hierarchy traversal, recursively call `GetWindow(childWnd, GW_CHILD)` on each child window. This is essential when targeting nested controls in complex dialogs.

Alternatively, use `EnumChildWindows()` for more readable code:

``` c
BOOL CALLBACK EnumChildProc(HWND hwnd, LPARAM lParam) {
    wchar_t className[256];
    GetClassNameW(hwnd, className, sizeof(className) / sizeof(wchar_t));

    int textLen = GetWindowTextLengthW(hwnd);
    if (textLen > 0) {
        wchar_t* buffer = (wchar_t*)malloc((textLen + 1) * sizeof(wchar_t));
        GetWindowTextW(hwnd, buffer, textLen + 1);
        wprintf(L"Class: %ls | Text: %ls\n", className, buffer);
        free(buffer);
    }

    return TRUE;  // Continue enumeration
}

EnumChildWindows(wnd, EnumChildProc, 0);
```

## Sending Messages to Windows

### Synchronous Message Send

Use `SendMessage()` for blocking message sends:

``` c
// Close a window
SendMessage(wnd, WM_CLOSE, 0, 0);

// Simulate a button click
SendMessage(buttonHandle, BM_CLICK, 0, 0);

// Set text in an edit control
SendMessage(editHandle, WM_SETTEXT, 0, (LPARAM)L"New text");

// Get text length
int textLen = SendMessage(editHandle, WM_GETTEXTLENGTH, 0, 0);
wchar_t* buffer = (wchar_t*)malloc((textLen + 1) * sizeof(wchar_t));
SendMessage(editHandle, WM_GETTEXT, textLen + 1, (LPARAM)buffer);
wprintf(L"Text: %ls\n", buffer);
free(buffer);
```

`SendMessage()` blocks your thread until the target window processes the message. If the window hangs, your thread hangs with it.

### Asynchronous Message Send

For non-blocking sends, use `PostMessage()`:

``` c
PostMessage(wnd, WM_CLOSE, 0, 0);
```

`PostMessage()` queues the message and returns immediately. The target window processes it on its own message loop. There’s no return value indicating success, so you lose feedback about whether the message was actually delivered.

### Protected Message Send with Timeout

Use `SendMessageTimeout()` to avoid hanging on unresponsive windows:

``` c
DWORD_PTR result = 0;
LRESULT lr = SendMessageTimeout(wnd, WM_CLOSE, 0, 0, 
                                 SMTO_ABORTIFHUNG, 5000, &result);
if (lr == 0) {
    DWORD err = GetLastError();
    if (err == ERROR_TIMEOUT) {
        wprintf(L"Message timed out after 5000ms\n");
    } else {
        wprintf(L"SendMessageTimeout failed: %lu\n", err);
    }
}
```

The `SMTO_ABORTIFHUNG` flag causes the function to abort if the window is unresponsive. The 5000 parameter is milliseconds. This is critical for automation scripts targeting external applications.

## Message-Specific Patterns

Different control types require different messages:

``` c
// Button click
SendMessage(buttonHandle, BM_CLICK, 0, 0);

// Text input to edit control
SendMessage(editHandle, WM_SETTEXT, 0, (LPARAM)L"User input");

// Combobox selection (0-indexed)
SendMessage(comboHandle, CB_SETCURSEL, 2, 0);

// Checkbox state
SendMessage(checkboxHandle, BM_SETCHECK, BST_CHECKED, 0);
SendMessage(checkboxHandle, BM_SETCHECK, BST_UNCHECKED, 0);

// Listbox selection
SendMessage(listboxHandle, LB_SETCURSEL, 3, 0);

// Get combobox selection
int selectedIdx = SendMessage(comboHandle, CB_GETCURSEL, 0, 0);
```

Always verify the target window type before sending control-specific messages. Sending `BM_CLICK` to an edit control produces undefined behavior. Query the window class name to confirm what you’re dealing with.

## User Interface Privilege Isolation (UIPI)

Windows Vista and later enforce UIPI. Your process cannot send messages to windows running at higher privilege levels (e.g., Administrator windows from a non-elevated process). The message silently fails with no error indication.

Solutions:

- Run your sending process with administrator elevation
- Use a manifest with `requestedExecutionLevel="highestAvailable"`
- Implement a service running at elevated privilege that accepts IPC requests from your user-level process
- Use `ChangeWindowMessageFilter()` (Vista/7 only) to explicitly allow specific messages (deprecated in Windows 8+)

Always check `GetLastError()` after failed sends to distinguish permission failures from other errors.

## Validation and Error Handling

Before sending any message, validate the window still exists:

``` c
if (!IsWindow(wnd)) {
    wprintf(L"Window handle is no longer valid\n");
    return 1;
}

if (IsWindowVisible(wnd) == 0) {
    wprintf(L"Window is not visible\n");
}

if (IsWindowEnabled(wnd) == 0) {
    wprintf(L"Window is disabled\n");
}

// Safe message send
LRESULT lr = SendMessage(wnd, WM_CLOSE, 0, 0);
```

A window may exist when you find it but close before you send a message. Check `IsWindow()` immediately before operations. For remote processes, also verify the target process still exists by checking if the window handle is valid.

## Common Mistakes to Avoid

**Not checking for NULL window handles**: Always validate `FindWindowW()` results before using the handle.

**Hardcoded buffer sizes**: Use dynamic allocation or query buffer requirements with `GetWindowTextLengthW()`.

**Timing windows between find and send**: A race condition exists between finding a window and sending it a message. Wrap operations in error checking or use `SendMessageTimeout()`.

**Ignoring privilege elevation requirements**: UIPI failures are silent. Run as administrator or redesign your approach if targeting elevated windows.

**Sending to terminated processes**: After a process exits, its window handles become invalid. Validate with `IsWindow()` before sending.

**Mixing ANSI and Unicode functions**: Never use `FindWindowA()` or `GetWindowTextA()`. These fail with non-ASCII characters. Always use wide-character versions.
