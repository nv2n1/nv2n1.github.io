---
title: "xcb_xv_put_image_checked(3)"
name: "xcb_xv_put_image_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xv_put_image_checked/"
description: "xcb_xv_put_image –"
---

<p>xcb_xv_put_image &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xv.h&gt;

Request function

    xcb_void_cookie_t
    xcb_xv_put_image(xcb_connection_t *conn, xcb_xv_port_t port, xcb_drawable_t drawable, xcb_gcontext_t gc, uint32_t id, int16_t src_x, int16_t src_y, uint16_t src_w, uint16_t src_h, int16_t drw_x, int16_t drw_y, uint16_t drw_w, uint16_t drw_h, uint16_t width, uint16_t height, uint32_t data_len, const uint8_t *data);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>port</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_w</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_h</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drw_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drw_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drw_w</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drw_h</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>data_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>data</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xv_put_image_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xv.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
