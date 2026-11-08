---
title: "Opening Links in New Windows and Tabs with JavaScript"
date: 2018-03-24 11:48:39 +0000
layout: post
canonical: https://www.systutorials.com/how-to-open-a-url-in-a-new-window-in-javascript/
---

The `window.open()` method is the standard way to open URLs in a new browser window or tab. Here’s how to use it effectively in modern JavaScript.

## Basic Usage

To open a URL in a new window or tab:

``` javascript
const url = "https://www.systutorials.com";
window.open(url);
```

Most modern browsers will open this in a new tab by default, respecting user preferences set in browser settings. Users generally prefer tabs over separate windows, and browsers enforce this choice to improve the experience.

## Controlling Window Features

If you need to open a separate window with specific dimensions, you can pass a third parameter with window features:

``` javascript
const url = "https://www.systutorials.com";
window.open(url, "popup", "width=800,height=600,left=100,top=100");
```

Common window feature parameters include:

- `width` and `height` — dimensions in pixels
- `left` and `top` — position on screen
- `menubar`, `toolbar`, `location`, `status` — show/hide browser UI elements (values: `yes` or `no`)
- `scrollbars` — enable scrollbars if content exceeds window size
- `resizable` — allow user to resize the window

**Important note:** Modern browsers ignore many of these parameters for security reasons. Parameters like `modal` and `alwaysRaised` have no effect in current browser versions. The `width` and `height` parameters still work but respect minimum dimensions for usability.

## Named Windows and Window References

You can give a window a name and reference it later:

``` javascript
const url = "https://www.systutorials.com";
const popup = window.open(url, "myWindow");

// Later, you can check if the window is still open
if (popup && !popup.closed) {
    popup.focus(); // Bring it to focus
}
```

If you call `window.open()` with the same window name, it reuses the existing window instead of creating a new one.

## Closing Windows

Only close windows that your script created with `window.open()`:

``` javascript
const popup = window.open("https://www.systutorials.com");

// Later, when appropriate
popup.close();
```

A window cannot close itself without user interaction unless it was opened by a script. This prevents malicious scripts from closing user windows.

## Cross-Origin Considerations

When opening URLs from a different origin, the opened window won’t have access to the opener for security reasons:

``` javascript
// This works on same origin
const popup = window.open("/local-page");
popup.document.title; // Can access this

// This doesn't work cross-origin
const external = window.open("https://example.com");
external.document.title; // SecurityError
```

If you need communication between windows on different origins, use `postMessage()`:

``` javascript
// In opener window
const popup = window.open("https://example.com");
popup.postMessage({ message: "Hello from opener" }, "https://example.com");

// In the opened window
window.addEventListener("message", (event) => {
    if (event.origin === "https://trusted-domain.com") {
        console.log(event.data.message);
    }
});
```

## Modern Alternatives

For most use cases, consider these alternatives before using `window.open()`:

- **Links with `target="_blank"`** — simpler, more accessible, respects user preferences
- **Fetch API or `XMLHttpRequest`** — when you need background requests
- **`window.location`** — when you want to navigate the current window

If you just need to open a link in a new tab, using an anchor element is usually the better choice:

``` html
<a href="https://www.systutorials.com" target="_blank" rel="noopener noreferrer">
    Open in new tab
</a>
```

The `rel="noopener noreferrer"` attributes prevent the opened page from accessing your `window` object and improve security.

## Browser Compatibility

`window.open()` is supported in all modern browsers. Most contemporary browsers ignore security-sensitive parameters and respect user settings for window/tab behavior over script directives.
