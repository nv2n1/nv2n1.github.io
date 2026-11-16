---
title: "xcb_put_image(3)"
name: "xcb_put_image"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_put_image/"
description: "xcb_put_image –"
---

<p>xcb_put_image &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
    xcb_void_cookie_t
    xcb_put_image(xcb_connection_t *conn, uint8_t format, xcb_drawable_t drawable, xcb_gcontext_t gc, uint16_t width, uint16_t height, int16_t dst_x, int16_t dst_y, uint8_t left_pad, uint8_t depth, uint32_t data_len, const uint8_t *data);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>format</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_IMAGE_FORMAT_XY_BITMAP</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_IMAGE_FORMAT_XY_PIXMAP</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_IMAGE_FORMAT_Z_PIXMAP</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<dt><i>drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>gc</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>left_pad</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>depth</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>data_len</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>data</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_put_image_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
