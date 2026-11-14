---
title: "xcb_render_set_picture_clip_rectangles_checked(3)"
name: "xcb_render_set_picture_clip_rectangles_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_render_set_picture_clip_rectangles_checked/"
description: "xcb_render_set_picture_clip_rectangles –"
---

<p>xcb_render_set_picture_clip_rectangles &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/render.h&gt;

Request function

    xcb_void_cookie_t
    xcb_render_set_picture_clip_rectangles(xcb_connection_t *conn, xcb_render_picture_t picture, int16_t clip_x_origin, int16_t clip_y_origin, uint32_t rectangles_len, const xcb_rectangle_t *rectangles);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>picture</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>clip_x_origin</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>clip_y_origin</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rectangles_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rectangles</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_render_set_picture_clip_rectangles_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from render.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
