---
title: "xcb_set_dashes_checked(3)"
name: "xcb_set_dashes_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_set_dashes_checked/"
description: "xcb_set_dashes –"
---

<p>xcb_set_dashes &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;

Request function

    xcb_void_cookie_t
    xcb_set_dashes(xcb_connection_t *conn, xcb_gcontext_t gc, uint16_t dash_offset, uint16_t dashes_len, const uint8_t *dashes);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>gc</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dash_offset</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dashes_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dashes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_set_dashes_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
