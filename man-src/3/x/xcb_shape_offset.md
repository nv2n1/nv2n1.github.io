---
title: "xcb_shape_offset(3)"
name: "xcb_shape_offset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_shape_offset/"
description: "xcb_shape_offset –"
---

<p>xcb_shape_offset &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/shape.h&gt;
Request function
xcb_void_cookie_t xcb_shape_offset(xcb_connection_t *conn, xcb_shape_kind_t destination_kind, xcb_window_t destination_window, int16_t x_offset, int16_t y_offset);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>destination_kind</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>destination_window</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>x_offset</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>y_offset</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_shape_offset_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from shape.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
