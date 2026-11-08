---
title: "Passing Data Between Parent and Child Windows in JavaScript"
date: 2018-03-24 11:48:48 +0000
layout: post
canonical: https://www.systutorials.com/how-to-pass-results-from-the-opened-window-to-the-openning-window-in-javascript/
---

When you open a new window with `window.open()`, you often need to communicate between the parent (opener) window and the child (opened) window. The most straightforward approach is to access the opener window directly through the `opener` property.

## Basic Two-Way Communication

In the parent window, define a variable:

``` javascript
let exchangeVar = '';
```

From the child window, you can read and modify this variable:

``` javascript
// Read the value
console.log(opener.exchangeVar);

// Update the value
opener.exchangeVar = 'updated value';
```

The key point: `opener` is a reference to the window that opened the current window. You can access any property or call any function on the opener window directly.

## Practical Example: Form Data Handoff

A common use case is opening a child window for selection, then passing the result back:

**Parent window:**

``` javascript
function openSelector() {
  window.open('selector.html', 'selector', 'width=400,height=300');
}

function receiveSelection(data) {
  console.log('Selected:', data);
  document.getElementById('result').textContent = data;
}
```

**Child window (selector.html):**

``` javascript
function sendSelection(value) {
  opener.receiveSelection(value);
  window.close();
}
```

## Important Security Considerations

Direct `opener` access only works when both windows are from the same origin (protocol, domain, and port must match). Cross-origin windows are blocked by the browser’s Same-Origin Policy.

For same-origin windows, you have full access to the opener’s variables and functions, but this also means:

- The child window can modify any data in the parent
- The parent remains responsible for validating any data the child sends
- If the parent window closes, the child’s `opener` reference becomes `null`

Always check if `opener` exists before using it:

``` javascript
if (opener && !opener.closed) {
  opener.receiveSelection(value);
}
```

## Alternative: Using PostMessage for Better Isolation

For more robust communication, especially if you want to avoid tight coupling or plan cross-origin scenarios, use `postMessage()`:

**Parent window:**

``` javascript
const childWindow = window.open('child.html', 'child');

window.addEventListener('message', (event) => {
  if (event.origin !== window.location.origin) return;
  console.log('Received from child:', event.data);
});
```

**Child window:**

``` javascript
opener.postMessage({ selection: 'value' }, window.location.origin);
```

`postMessage()` is more secure because it doesn’t grant full access to the other window’s scope and works across origins (with proper origin validation).

## Checking Window Status

Before sending data, verify the opener window is still available:

``` javascript
if (opener && !opener.closed) {
  opener.myFunction(data);
} else {
  console.warn('Opener window is closed or unavailable');
}
```

This prevents errors when the parent window closes before the child attempts communication.

For simple same-origin scenarios, direct property access via `opener` works well. For production applications with multiple windows or future cross-origin needs, `postMessage()` is the more maintainable approach.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
