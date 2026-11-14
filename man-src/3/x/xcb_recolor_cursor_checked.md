---
title: "xcb_recolor_cursor_checked(3)"
name: "xcb_recolor_cursor_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_recolor_cursor_checked/"
description: "xcb_recolor_cursor –"
---

<p>xcb_recolor_cursor &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_recolor_cursor(xcb_connection_t *conn, xcb_cursor_t cursor, uint16_t fore_red, uint16_t fore_green, uint16_t fore_blue, uint16_t back_red, uint16_t back_green, uint16_t back_blue);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>cursor</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>fore_red</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>fore_green</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>fore_blue</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>back_red</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>back_green</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>back_blue</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_recolor_cursor_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
