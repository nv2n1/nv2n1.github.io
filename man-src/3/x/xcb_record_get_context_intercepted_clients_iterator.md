---
title: "xcb_record_get_context_intercepted_clients_iterator(3)"
name: "xcb_record_get_context_intercepted_clients_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_record_get_context_intercepted_clients_iterator/"
description: "xcb_record_get_context –"
---

<p>xcb_record_get_context &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/record.h&gt;


Request function



xcb_record_get_context_cookie_t xcb_record_get_context(xcb_connection_t *conn, xcb_record_context_t context);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_record_get_context_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>enabled</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_record_element_header_t <i>element_header</i>;
 uint8_t <i>pad0</i>[3];
 uint32_t <i>num_intercepted_clients</i>;
 uint8_t <i>pad1</i>[16];
} <code>xcb_record_get_context_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_record_get_context_reply_t *<code>xcb_record_get_context_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_record_get_context_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_record_get_context_intercepted_clients_length</code>(const xcb_record_get_context_reply_t *<i>reply</i>);</p>
<dd>xcb_record_client_info_iterator_t <code>xcb_record_get_context_intercepted_clients_iterator</code>(const xcb_record_get_context_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>context</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RECORD_GET_CONTEXT</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>enabled</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>element_header</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_intercepted_clients</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_record_get_context_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_record_get_context_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_record_get_context_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from record.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
