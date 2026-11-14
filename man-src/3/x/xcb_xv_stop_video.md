---
title: "xcb_xv_stop_video(3)"
name: "xcb_xv_stop_video"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xv_stop_video/"
description: "xcb_xv_stop_video –"
---

<p>xcb_xv_stop_video &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xv.h&gt;


Request function



xcb_void_cookie_t xcb_xv_stop_video(xcb_connection_t *conn, xcb_xv_port_t port, xcb_drawable_t drawable);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>port</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xv_stop_video_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xv.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
