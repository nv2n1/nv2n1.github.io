---
title: "xcb_xfixes_create_pointer_barrier(3)"
name: "xcb_xfixes_create_pointer_barrier"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xfixes_create_pointer_barrier/"
description: "xcb_xfixes_create_pointer_barrier –"
---

<p>xcb_xfixes_create_pointer_barrier &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xfixes.h&gt;

Request function

    xcb_void_cookie_t
    xcb_xfixes_create_pointer_barrier(xcb_connection_t *conn, xcb_xfixes_barrier_t barrier, xcb_window_t window, uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint32_t directions, uint16_t num_devices, const uint16_t *devices);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>barrier</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x1</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y1</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x2</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y2</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>directions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_devices</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>devices</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xfixes_create_pointer_barrier_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xfixes.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
