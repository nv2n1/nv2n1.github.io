---
title: "xcb_reparent_window_checked(3)"
name: "xcb_reparent_window_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_reparent_window_checked/"
description: "xcb_reparent_window – Reparents a window"
---

<p>xcb_reparent_window &#8211; Reparents a window</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_reparent_window(xcb_connection_t *conn, xcb_window_t window, xcb_window_t parent, int16_t x, int16_t y);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>The window to reparent.</p>
<dt><i>parent</i></p>
<dd>The new parent of the window.</p>
<dt><i>x</i></p>
<dd>The X position of the window within its new parent.</p>
<dt><i>y</i></p>
<dd>The Y position of the window within its new parent.</dl>
<h2>Description</h2>
<p>Makes the specified window a child of the specified parent window. If the window is mapped, it will automatically be unmapped before reparenting and re-mapped after reparenting. The window is placed in the stacking order on top with respect to sibling windows. </p>
<p> After reparenting, a ReparentNotify event is generated.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_reparent_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_match_error_t</i></p>
<dd>The new parent window is not on the same screen as the old parent window. </p>
<p> The new parent window is the specified window or an inferior of the specified window. </p>
<p> The new parent is InputOnly and the window is not. </p>
<p> The specified window has a ParentRelative background and the new parent window is not the same depth as the specified window.</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_map_window/">xcb_map_window</a></code>(3), <code><a href="/docs/linux/man/3-xcb_reparent_notify_event_t/">xcb_reparent_notify_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_unmap_window/">xcb_unmap_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
