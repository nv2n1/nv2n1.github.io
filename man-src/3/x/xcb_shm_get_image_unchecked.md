---
title: "xcb_shm_get_image_unchecked(3)"
name: "xcb_shm_get_image_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_shm_get_image_unchecked/"
description: "xcb_shm_get_image –"
---

<p>xcb_shm_get_image &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/shm.h&gt;


Request function



xcb_shm_get_image_cookie_t xcb_shm_get_image(xcb_connection_t *conn, xcb_drawable_t drawable, int16_t x, int16_t y, uint16_t width, uint16_t height, uint32_t plane_mask, uint8_t format, xcb_shm_seg_t shmseg, uint32_t offset);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_shm_get_image_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>depth</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_visualid_t <i>visual</i>;
 uint32_t <i>size</i>;
} <code>xcb_shm_get_image_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_shm_get_image_reply_t *<code>xcb_shm_get_image_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_shm_get_image_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>plane_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>shmseg</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>offset</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_SHM_GET_IMAGE</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>depth</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>visual</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>size</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_shm_get_image_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_shm_get_image_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_shm_get_image_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from shm.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
