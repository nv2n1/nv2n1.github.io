---
title: "xcb_xv_query_port_attributes_attributes_length(3)"
name: "xcb_xv_query_port_attributes_attributes_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xv_query_port_attributes_attributes_length/"
description: "xcb_xv_query_port_attributes –"
---

<p>xcb_xv_query_port_attributes &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xv.h&gt;


Request function



xcb_xv_query_port_attributes_cookie_t xcb_xv_query_port_attributes(xcb_connection_t *conn, xcb_xv_port_t port);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xv_query_port_attributes_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>num_attributes</i>;
 uint32_t <i>text_size</i>;
 uint8_t <i>pad1</i>[16];
} <code>xcb_xv_query_port_attributes_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xv_query_port_attributes_reply_t *<code>xcb_xv_query_port_attributes_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xv_query_port_attributes_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_xv_query_port_attributes_attributes_length</code>(const xcb_xv_query_port_attributes_reply_t *<i>reply</i>);</p>
<dd>xcb_xv_attribute_info_iterator_t <code>xcb_xv_query_port_attributes_attributes_iterator</code>(const xcb_xv_query_port_attributes_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>port</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XV_QUERY_PORT_ATTRIBUTES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>num_attributes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>text_size</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xv_query_port_attributes_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xv_query_port_attributes_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xv_query_port_attributes_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xv.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
