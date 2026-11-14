---
title: "xcb_x_print_print_put_document_data_checked(3)"
name: "xcb_x_print_print_put_document_data_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_x_print_print_put_document_data_checked/"
description: "xcb_x_print_print_put_document_data –"
---

<p>xcb_x_print_print_put_document_data &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xprint.h&gt;

Request function

    xcb_void_cookie_t
    xcb_x_print_print_put_document_data(xcb_connection_t *conn, xcb_drawable_t drawable, uint32_t len_data, uint16_t len_fmt, uint16_t len_options, const uint8_t *data, const xcb_x_print_string8_t *doc_format, const xcb_x_print_string8_t *options);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>drawable</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>len_data</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>len_fmt</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>len_options</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>data</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>doc_format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>options</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_x_print_print_put_document_data_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xprint.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
