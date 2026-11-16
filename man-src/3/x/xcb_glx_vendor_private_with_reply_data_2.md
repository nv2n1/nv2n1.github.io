---
title: "xcb_glx_vendor_private_with_reply_data_2(3)"
name: "xcb_glx_vendor_private_with_reply_data_2"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_vendor_private_with_reply_data_2/"
description: "xcb_glx_vendor_private_with_reply –"
---

<p>xcb_glx_vendor_private_with_reply &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;
Request function
    xcb_glx_vendor_private_with_reply_cookie_t
    xcb_glx_vendor_private_with_reply(xcb_connection_t *conn, uint32_t vendor_code, xcb_glx_context_tag_t context_tag, uint32_t data_len, const uint8_t *data);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_glx_vendor_private_with_reply_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>retval</i>;
 uint8_t <i>data1</i>[24];
} <code>xcb_glx_vendor_private_with_reply_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_glx_vendor_private_with_reply_reply_t *<code>xcb_glx_vendor_private_with_reply_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_glx_vendor_private_with_reply_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>uint8_t *<code>xcb_glx_vendor_private_with_reply_data_2</code>(const xcb_glx_vendor_private_with_reply_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_glx_vendor_private_with_reply_data_2_length</code>(const xcb_glx_vendor_private_with_reply_reply_t *<i>reply</i>);</dd>
<dd>xcb_generic_iterator_t <code>xcb_glx_vendor_private_with_reply_data_2_end</code>(const xcb_glx_vendor_private_with_reply_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>vendor_code</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>context_tag</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>data_len</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>data</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_GLX_VENDOR_PRIVATE_WITH_REPLY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>retval</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>data1</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_glx_vendor_private_with_reply_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_glx_vendor_private_with_reply_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_glx_vendor_private_with_reply_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
