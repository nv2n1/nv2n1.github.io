---
title: "xcb_glx_set_client_info_2arb(3)"
name: "xcb_glx_set_client_info_2arb"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_set_client_info_2arb/"
description: "xcb_glx_set_client_info_2arb –"
---

<p>xcb_glx_set_client_info_2arb &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;

Request function

    xcb_void_cookie_t
    xcb_glx_set_client_info_2arb(xcb_connection_t *conn, uint32_t major_version, uint32_t minor_version, uint32_t num_versions, uint32_t gl_str_len, uint32_t glx_str_len, const uint32_t *gl_versions, const char *gl_extension_string, const char *glx_extension_string);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>major_version</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>minor_version</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_versions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gl_str_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>glx_str_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gl_versions</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>gl_extension_string</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>glx_extension_string</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_glx_set_client_info_2arb_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
