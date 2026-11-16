---
title: "xcb_poly_segment(3)"
name: "xcb_poly_segment"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_poly_segment/"
description: "xcb_poly_segment – draw lines"
---

<p>xcb_poly_segment &#8211; draw lines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
    xcb_void_cookie_t
    xcb_poly_segment(xcb_connection_t *conn, xcb_drawable_t drawable, xcb_gcontext_t gc, uint32_t segments_len, const xcb_segment_t *segments);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>drawable</i></dt>
<dd>A drawable (Window or Pixmap) to draw on.</dd>
<dt><i>gc</i></dt>
<dd>The graphics context to use. </dd>
<p> TODO: document which attributes of a gc are used</p>
<dt><i>segments_len</i></dt>
<dd>The number of <i>xcb_segment_t</i> structures in <i>segments</i>.</dd>
<dt><i>segments</i></dt>
<dd>An array of <i>xcb_segment_t</i> structures.</dd></dl>
<h2>Description</h2>
<p>Draws multiple, unconnected lines. For each segment, a line is drawn between (x1, y1) and (x2, y2). The lines are drawn in the order listed in the array of <i>xcb_segment_t</i> structures and does not perform joining at coincident endpoints. For any given line, a pixel is not drawn more than once. If lines intersect, the intersecting pixels are drawn multiple times. </p>
<p> TODO: include the xcb_segment_t data structure </p>
<p> TODO: an example</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_poly_segment_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_drawable_error_t</i></dt>
<dd>The specified <i>drawable</i> does not exist.</dd>
<dt><i>xcb_g_context_error_t</i></dt>
<dd>The specified <i>gc</i> does not exist.</dd>
<dt><i>xcb_match_error_t</i></dt>
<dd>TODO: reasons?</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
