---
title: "xcb_copy_area(3)"
name: "xcb_copy_area"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_copy_area/"
description: "xcb_copy_area – copy areas"
---

<p>xcb_copy_area &#8211; copy areas</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_copy_area(xcb_connection_t *conn, xcb_drawable_t src_drawable, xcb_drawable_t dst_drawable, xcb_gcontext_t gc, int16_t src_x, int16_t src_y, int16_t dst_x, int16_t dst_y, uint16_t width, uint16_t height);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>src_drawable</i></p>
<dd>The source drawable (Window or Pixmap).</p>
<dt><i>dst_drawable</i></p>
<dd>The destination drawable (Window or Pixmap).</p>
<dt><i>gc</i></p>
<dd>The graphics context to use.</p>
<dt><i>src_x</i></p>
<dd>The source X coordinate.</p>
<dt><i>src_y</i></p>
<dd>The source Y coordinate.</p>
<dt><i>dst_x</i></p>
<dd>The destination X coordinate.</p>
<dt><i>dst_y</i></p>
<dd>The destination Y coordinate.</p>
<dt><i>width</i></p>
<dd>The width of the area to copy (in pixels).</p>
<dt><i>height</i></p>
<dd>The height of the area to copy (in pixels).</dl>
<h2>Description</h2>
<p>Copies the specified rectangle from <i>src_drawable</i> to <i>dst_drawable</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_copy_area_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>The specified <i>drawable</i> (Window or Pixmap) does not exist.</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>The specified graphics context does not exist.</p>
<dt><i>xcb_match_error_t</i></p>
<dd><i>src_drawable</i> has a different root or depth than <i>dst_drawable</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
