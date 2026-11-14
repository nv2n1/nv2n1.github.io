---
title: "xcb_unmap_window_checked(3)"
name: "xcb_unmap_window_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_unmap_window_checked/"
description: "xcb_unmap_window – Makes a window invisible"
---

<p>xcb_unmap_window &#8211; Makes a window invisible</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_unmap_window(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to make invisible.</dl>
<h2>Description</h2>
<p>Unmaps the specified window. This means making the window invisible (and all its child windows). </p>
<p> Unmapping a window leads to the <i>UnmapNotify</i> event being generated. Also, <i>Expose</i> events are generated for formerly obscured windows.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_unmap_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_expose_event_t/">xcb_expose_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3), <code><a href="/docs/linux/man/3-xcb_unmap_notify_event_t/">xcb_unmap_notify_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
