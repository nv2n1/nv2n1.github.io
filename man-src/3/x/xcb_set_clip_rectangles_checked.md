---
title: "xcb_set_clip_rectangles_checked(3)"
name: "xcb_set_clip_rectangles_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_set_clip_rectangles_checked/"
description: "xcb_set_clip_rectangles –"
---

<p>xcb_set_clip_rectangles &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_set_clip_rectangles(xcb_connection_t *conn, uint8_t ordering, xcb_gcontext_t gc, int16_t clip_x_origin, int16_t clip_y_origin, uint32_t rectangles_len, const xcb_rectangle_t *rectangles);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>ordering</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_CLIP_ORDERING_UNSORTED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_CLIP_ORDERING_Y_SORTED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_CLIP_ORDERING_YX_SORTED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_CLIP_ORDERING_YX_BANDED</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<dt><i>gc</i></p>
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
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_set_clip_rectangles_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
