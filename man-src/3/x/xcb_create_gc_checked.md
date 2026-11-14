---
title: "xcb_create_gc_checked(3)"
name: "xcb_create_gc_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_create_gc_checked/"
description: "xcb_create_gc – Creates a graphics context"
---

<p>xcb_create_gc &#8211; Creates a graphics context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_create_gc(xcb_connection_t *conn, xcb_gcontext_t cid, xcb_drawable_t drawable, uint32_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>cid</i></p>
<dd>The ID with which you will refer to the graphics context, created by <i>xcb_generate_id</i>.</p>
<dt><i>drawable</i></p>
<dd>Drawable to get the root/depth from.</p>
<dt><i>value_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>value_list</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<p>Creates a graphics context. The graphics context can be used with any drawable that has the same root and depth as the specified drawable.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_create_gc_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_alloc_error_t</i></p>
<dd>The X server could not allocate the requested resources (no memory?).</p>
<dt><i>xcb_drawable_error_t</i></p>
<dd>The specified <i>drawable</i> (Window or Pixmap) does not exist.</p>
<dt><i>xcb_font_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_match_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_pixmap_error_t</i></p>
<dd>TODO: reasons?</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: reasons?</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_generate_id/">xcb_generate_id</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
