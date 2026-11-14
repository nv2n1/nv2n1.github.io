---
title: "xcb_create_colormap_checked(3)"
name: "xcb_create_colormap_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_create_colormap_checked/"
description: "xcb_create_colormap –"
---

<p>xcb_create_colormap &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_create_colormap(xcb_connection_t *conn, uint8_t alloc, xcb_colormap_t mid, xcb_window_t window, xcb_visualid_t visual);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>alloc</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_COLORMAP_ALLOC_NONE</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_COLORMAP_ALLOC_ALL</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<dt><i>mid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>visual</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_create_colormap_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
