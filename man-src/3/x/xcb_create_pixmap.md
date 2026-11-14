---
title: "xcb_create_pixmap(3)"
name: "xcb_create_pixmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_create_pixmap/"
description: "xcb_create_pixmap – Creates a pixmap"
---

<p>xcb_create_pixmap &#8211; Creates a pixmap</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_create_pixmap(xcb_connection_t *conn, uint8_t depth, xcb_pixmap_t pid, xcb_drawable_t drawable, uint16_t width, uint16_t height);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>depth</i></p>
<dd>TODO</p>
<dt><i>pid</i></p>
<dd>The ID with which you will refer to the new pixmap, created by <i>xcb_generate_id</i>.</p>
<dt><i>drawable</i></p>
<dd>Drawable to get the screen from.</p>
<dt><i>width</i></p>
<dd>The width of the new pixmap.</p>
<dt><i>height</i></p>
<dd>The height of the new pixmap.</dl>
<h2>Description</h2>
<p>Creates a pixmap. The pixmap can only be used on the same screen as <i>drawable</i> is on and only with drawables of the same <i>depth</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_create_pixmap_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></p>
<dd>The X server could not allocate the requested resources (no memory?).</p>
<dt><i>xcb_drawable_error_t</i></p>
<dd>The specified <i>drawable</i> (Window or Pixmap) does not exist.</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_generate_id/">xcb_generate_id</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
