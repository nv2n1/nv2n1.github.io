---
title: "xcb_xv_shm_put_image_checked(3)"
name: "xcb_xv_shm_put_image_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xv_shm_put_image_checked/"
description: "xcb_xv_shm_put_image –"
---

<p>xcb_xv_shm_put_image &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xv.h&gt;
Request function
xcb_void_cookie_t xcb_xv_shm_put_image(xcb_connection_t *conn, xcb_xv_port_t port, xcb_drawable_t drawable, xcb_gcontext_t gc, xcb_shm_seg_t shmseg, uint32_t id, uint32_t offset, int16_t src_x, int16_t src_y, uint16_t src_w, uint16_t src_h, int16_t drw_x, int16_t drw_y, uint16_t drw_w, uint16_t drw_h, uint16_t width, uint16_t height, uint8_t send_event);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>port</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>gc</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>shmseg</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>id</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>offset</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_w</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_h</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>drw_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>drw_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>drw_w</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>drw_h</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>send_event</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xv_shm_put_image_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xv.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
