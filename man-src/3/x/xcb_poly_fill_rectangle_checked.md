---
title: "xcb_poly_fill_rectangle_checked(3)"
name: "xcb_poly_fill_rectangle_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_poly_fill_rectangle_checked/"
description: "xcb_poly_fill_rectangle – Fills rectangles"
---

<p>xcb_poly_fill_rectangle &#8211; Fills rectangles</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_poly_fill_rectangle(xcb_connection_t *conn, xcb_drawable_t drawable, xcb_gcontext_t gc, uint32_t rectangles_len, const xcb_rectangle_t *rectangles);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>drawable</i></p>
<dd>The drawable (Window or Pixmap) to draw on.</p>
<dt><i>gc</i></p>
<dd>The graphics context to use. </p>
<p> The following graphics context components are used: function, plane-mask, fill-style, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. </p>
<p> The following graphics context mode-dependent components are used: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin.</p>
<dt><i>rectangles_len</i></p>
<dd>The number of <i>xcb_rectangle_t</i> structures in <i>rectangles</i>.</p>
<dt><i>rectangles</i></p>
<dd>The rectangles to fill.</dl>
<h2>Description</h2>
<p>Fills the specified rectangle(s) in the order listed in the array. For any given rectangle, each pixel is not drawn more than once. If rectangles intersect, the intersecting pixels are drawn multiple times.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_poly_fill_rectangle_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>The specified <i>drawable</i> (Window or Pixmap) does not exist.</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>The specified graphics context does not exist.</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
