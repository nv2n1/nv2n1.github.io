---
title: "xcb_record_register_clients_checked(3)"
name: "xcb_record_register_clients_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_record_register_clients_checked/"
description: "xcb_record_register_clients –"
---

<p>xcb_record_register_clients &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/record.h&gt;

Request function

    xcb_void_cookie_t
    xcb_record_register_clients(xcb_connection_t *conn, xcb_record_context_t context, xcb_record_element_header_t element_header, uint32_t num_client_specs, uint32_t num_ranges, const xcb_record_client_spec_t *client_specs, const xcb_record_range_t *ranges);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>context</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>element_header</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_client_specs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_ranges</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>client_specs</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ranges</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_record_register_clients_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from record.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
