---
title: "xcb_glx_create_context(3)"
name: "xcb_glx_create_context"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_create_context/"
description: "xcb_glx_create_context –"
---

<p>xcb_glx_create_context &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;


Request function



xcb_void_cookie_t xcb_glx_create_context(xcb_connection_t *conn, xcb_glx_context_t context, xcb_visualid_t visual, uint32_t screen, xcb_glx_context_t share_list, uint8_t is_direct);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>context</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>visual</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>screen</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>share_list</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>is_direct</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_glx_create_context_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
