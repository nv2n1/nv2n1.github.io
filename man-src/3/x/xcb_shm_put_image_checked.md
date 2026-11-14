---
title: "xcb_shm_put_image_checked(3)"
name: "xcb_shm_put_image_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_shm_put_image_checked/"
description: "xcb_shm_put_image –"
---

<p>xcb_shm_put_image &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/shm.h&gt;


Request function



xcb_void_cookie_t xcb_shm_put_image(xcb_connection_t *conn, xcb_drawable_t drawable, xcb_gcontext_t gc, uint16_t total_width, uint16_t total_height, uint16_t src_x, uint16_t src_y, uint16_t src_width, uint16_t src_height, int16_t dst_x, int16_t dst_y, uint8_t depth, uint8_t format, uint8_t send_event, xcb_shm_seg_t shmseg, uint32_t offset);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>total_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>total_height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>depth</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>send_event</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>shmseg</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>offset</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_shm_put_image_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from shm.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
