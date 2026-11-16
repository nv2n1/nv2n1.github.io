---
title: "xcb_render_triangles_checked(3)"
name: "xcb_render_triangles_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_render_triangles_checked/"
description: "xcb_render_triangles –"
---

<p>xcb_render_triangles &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/render.h&gt;
Request function
    xcb_void_cookie_t
    xcb_render_triangles(xcb_connection_t *conn, uint8_t op, xcb_render_picture_t src, xcb_render_picture_t dst, xcb_render_pictformat_t mask_format, int16_t src_x, int16_t src_y, uint32_t triangles_len, const xcb_render_triangle_t *triangles);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>op</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mask_format</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>triangles_len</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>triangles</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_render_triangles_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from render.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
