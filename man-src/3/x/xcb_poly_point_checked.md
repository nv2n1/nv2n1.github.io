---
title: "xcb_poly_point_checked(3)"
name: "xcb_poly_point_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_poly_point_checked/"
description: "xcb_poly_point –"
---

<p>xcb_poly_point &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_poly_point(xcb_connection_t *conn, uint8_t coordinate_mode, xcb_drawable_t drawable, xcb_gcontext_t gc, uint32_t points_len, const xcb_point_t *points);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>coordinate_mode</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_COORD_MODE_ORIGIN</i></p>
<dd>Treats all coordinates as relative to the origin.</p>
<dt><i>XCB_COORD_MODE_PREVIOUS</i></p>
<dd>Treats all coordinates after the first as relative to the previous coordinate.</dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>points_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>points</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_poly_point_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
