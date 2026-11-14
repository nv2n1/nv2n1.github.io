---
title: "xcb_copy_gc(3)"
name: "xcb_copy_gc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_copy_gc/"
description: "xcb_copy_gc –"
---

<p>xcb_copy_gc &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_copy_gc(xcb_connection_t *conn, xcb_gcontext_t src_gc, xcb_gcontext_t dst_gc, uint32_t value_mask);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>src_gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>value_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_copy_gc_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
