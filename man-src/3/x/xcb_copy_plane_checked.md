---
title: "xcb_copy_plane_checked(3)"
name: "xcb_copy_plane_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_copy_plane_checked/"
description: "xcb_copy_plane –"
---

<p>xcb_copy_plane &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_copy_plane(xcb_connection_t *conn, xcb_drawable_t src_drawable, xcb_drawable_t dst_drawable, xcb_gcontext_t gc, int16_t src_x, int16_t src_y, int16_t dst_x, int16_t dst_y, uint16_t width, uint16_t height, uint32_t bit_plane);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>src_drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>gc</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>bit_plane</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_copy_plane_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
