---
title: "xcb_xfixes_create_region_from_window(3)"
name: "xcb_xfixes_create_region_from_window"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xfixes_create_region_from_window/"
description: "xcb_xfixes_create_region_from_window –"
---

<p>xcb_xfixes_create_region_from_window &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xfixes.h&gt;


Request function



xcb_void_cookie_t xcb_xfixes_create_region_from_window(xcb_connection_t *conn, xcb_xfixes_region_t region, xcb_window_t window, xcb_shape_kind_t kind);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>region</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>kind</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xfixes_create_region_from_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xfixes.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
