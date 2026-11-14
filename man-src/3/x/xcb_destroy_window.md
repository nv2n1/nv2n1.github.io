---
title: "xcb_destroy_window(3)"
name: "xcb_destroy_window"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_destroy_window/"
description: "xcb_destroy_window – Destroys a window"
---

<p>xcb_destroy_window &#8211; Destroys a window</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_destroy_window(xcb_connection_t *conn, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to destroy.</dl>
<h2>Description</h2>
<p>Destroys the specified window and all of its subwindows. A DestroyNotify event is generated for each destroyed window (a DestroyNotify event is first generated for any given window&#8217;s inferiors). If the window was mapped, it will be automatically unmapped before destroying. </p>
<p> Calling DestroyWindow on the root window will do nothing.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_destroy_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_destroy_notify_event_t/">xcb_destroy_notify_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3), <code><a href="/docs/linux/man/3-xcb_unmap_window/">xcb_unmap_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
