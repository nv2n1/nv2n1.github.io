---
title: "xcb_glx_swap_buffers_checked(3)"
name: "xcb_glx_swap_buffers_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_swap_buffers_checked/"
description: "xcb_glx_swap_buffers –"
---

<p>xcb_glx_swap_buffers &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;


Request function



xcb_void_cookie_t xcb_glx_swap_buffers(xcb_connection_t *conn, xcb_glx_context_tag_t context_tag, xcb_glx_drawable_t drawable);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>context_tag</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_glx_swap_buffers_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
