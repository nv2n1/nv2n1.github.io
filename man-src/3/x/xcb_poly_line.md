---
title: "xcb_poly_line(3)"
name: "xcb_poly_line"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_poly_line/"
description: "xcb_poly_line – draw lines"
---

<p>xcb_poly_line &#8211; draw lines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_poly_line(xcb_connection_t *conn, uint8_t coordinate_mode, xcb_drawable_t drawable, xcb_gcontext_t gc, uint32_t points_len, const xcb_point_t *points);</code></pre>
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
<dd></dl>
<dt><i>drawable</i></p>
<dd>The drawable to draw the line(s) on.</p>
<dt><i>gc</i></p>
<dd>The graphics context to use.</p>
<dt><i>points_len</i></p>
<dd>The number of <i>xcb_point_t</i> structures in <i>points</i>.</p>
<dt><i>points</i></p>
<dd>An array of points.</dl>
<h2>Description</h2>
<p>Draws <i>points_len</i>-1 lines between each pair of points (point[i], point[i+1]) in the <i>points</i> array. The lines are drawn in the order listed in the array. They join correctly at all intermediate points, and if the first and last points coincide, the first and last lines also join correctly. For any given line, a pixel is not drawn more than once. If thin (zero line-width) lines intersect, the intersecting pixels are drawn multiple times. If wide lines intersect, the intersecting pixels are drawn only once, as though the entire request were a single, filled shape.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_poly_line_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_g_context_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>Example</h2>
<pre>/*
 * Draw a straight line.
 *
 */
void my_example(xcb_connection_t *conn, xcb_drawable_t drawable, xcb_gcontext_t gc) {
 xcb_poly_line(conn, XCB_COORD_MODE_ORIGIN, drawable, gc, 2,
 (xcb_point_t[]) { {10, 10}, {100, 10} });
 xcb_flush(conn);
}</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb-examples/">xcb-examples</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
