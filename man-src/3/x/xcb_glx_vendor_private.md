---
title: "xcb_glx_vendor_private(3)"
name: "xcb_glx_vendor_private"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_vendor_private/"
description: "xcb_glx_vendor_private –"
---

<p>xcb_glx_vendor_private &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;

Request function

    xcb_void_cookie_t
    xcb_glx_vendor_private(xcb_connection_t *conn, uint32_t vendor_code, xcb_glx_context_tag_t context_tag, uint32_t data_len, const uint8_t *data);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>vendor_code</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>context_tag</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>data_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>data</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_glx_vendor_private_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
