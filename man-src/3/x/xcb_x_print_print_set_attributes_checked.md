---
title: "xcb_x_print_print_set_attributes_checked(3)"
name: "xcb_x_print_print_set_attributes_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_x_print_print_set_attributes_checked/"
description: "xcb_x_print_print_set_attributes –"
---

<p>xcb_x_print_print_set_attributes &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xprint.h&gt;

Request function

    xcb_void_cookie_t
    xcb_x_print_print_set_attributes(xcb_connection_t *conn, xcb_x_print_pcontext_t context, uint32_t stringLen, uint8_t pool, uint8_t rule, uint32_t attributes_len, const xcb_x_print_string8_t *attributes);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>context</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>stringLen</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pool</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rule</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>attributes_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>attributes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_x_print_print_set_attributes_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xprint.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
