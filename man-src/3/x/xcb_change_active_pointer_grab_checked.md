---
title: "xcb_change_active_pointer_grab_checked(3)"
name: "xcb_change_active_pointer_grab_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_active_pointer_grab_checked/"
description: "xcb_change_active_pointer_grab –"
---

<p>xcb_change_active_pointer_grab &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_change_active_pointer_grab(xcb_connection_t *conn, xcb_cursor_t cursor, xcb_timestamp_t time, uint16_t event_mask);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>cursor</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>event_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_active_pointer_grab_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
