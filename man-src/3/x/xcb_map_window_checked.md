---
title: "xcb_map_window_checked(3)"
name: "xcb_map_window_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_map_window_checked/"
description: "xcb_map_window – Makes a window visible"
---

<p>xcb_map_window &#8211; Makes a window visible</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_map_window(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to make visible.</dl>
<h2>Description</h2>
<p>Maps the specified window. This means making the window visible (as long as its parent is visible). </p>
<p> This MapWindow request will be translated to a MapRequest request if a window manager is running. The window manager then decides to either map the window or not. Set the override-redirect window attribute to true if you want to bypass this mechanism. </p>
<p> If the window manager decides to map the window (or if no window manager is running), a MapNotify event is generated. </p>
<p> If the window becomes viewable and no earlier contents for it are remembered, the X server tiles the window with its background. If the window&#8217;s background is undefined, the existing screen contents are not altered, and the X server generates zero or more Expose events. </p>
<p> If the window type is InputOutput, an Expose event will be generated when the window becomes visible. The normal response to an Expose event should be to repaint the window.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_map_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_match_error_t</i></p>
<dd>The specified window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_expose_event_t/">xcb_expose_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_notify_event_t/">xcb_map_notify_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_unmap_window/">xcb_unmap_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
