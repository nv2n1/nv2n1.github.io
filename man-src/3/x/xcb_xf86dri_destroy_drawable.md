---
title: "xcb_xf86dri_destroy_drawable(3)"
name: "xcb_xf86dri_destroy_drawable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xf86dri_destroy_drawable/"
description: "xcb_xf86dri_destroy_drawable –"
---

<p>xcb_xf86dri_destroy_drawable &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xf86dri.h&gt;


Request function



xcb_void_cookie_t xcb_xf86dri_destroy_drawable(xcb_connection_t *conn, uint32_t screen, uint32_t drawable);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>screen</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xf86dri_destroy_drawable_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xf86dri.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
