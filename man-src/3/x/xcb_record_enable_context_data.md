---
title: "xcb_record_enable_context_data(3)"
name: "xcb_record_enable_context_data"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_record_enable_context_data/"
description: "xcb_record_enable_context –"
---

<p>xcb_record_enable_context &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/record.h&gt;
Request function
xcb_record_enable_context_cookie_t xcb_record_enable_context(xcb_connection_t *conn, xcb_record_context_t context);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_record_enable_context_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>category</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_record_element_header_t <i>element_header</i>;
 uint8_t <i>client_swapped</i>;
 uint8_t <i>pad0</i>[2];
 uint32_t <i>xid_base</i>;
 uint32_t <i>server_time</i>;
 uint32_t <i>rec_sequence_num</i>;
 uint8_t <i>pad1</i>[8];
} <code>xcb_record_enable_context_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_record_enable_context_reply_t *<code>xcb_record_enable_context_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_record_enable_context_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>uint8_t *<code>xcb_record_enable_context_data</code>(const xcb_record_enable_context_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_record_enable_context_data_length</code>(const xcb_record_enable_context_reply_t *<i>reply</i>);</dd>
<dd>xcb_generic_iterator_t <code>xcb_record_enable_context_data_end</code>(const xcb_record_enable_context_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>context</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_RECORD_ENABLE_CONTEXT</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>category</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>element_header</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>client_swapped</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>xid_base</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>server_time</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>rec_sequence_num</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_record_enable_context_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_record_enable_context_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_record_enable_context_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from record.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
