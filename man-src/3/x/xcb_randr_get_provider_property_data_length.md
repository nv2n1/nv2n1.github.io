---
title: "xcb_randr_get_provider_property_data_length(3)"
name: "xcb_randr_get_provider_property_data_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_get_provider_property_data_length/"
description: "xcb_randr_get_provider_property –"
---

<p>xcb_randr_get_provider_property &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_randr_get_provider_property_cookie_t xcb_randr_get_provider_property(xcb_connection_t *conn, xcb_randr_provider_t provider, xcb_atom_t property, xcb_atom_t type, uint32_t long_offset, uint32_t long_length, uint8_t _delete, uint8_t pending);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_randr_get_provider_property_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>format</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>type</i>;
 uint32_t <i>bytes_after</i>;
 uint32_t <i>num_items</i>;
 uint8_t <i>pad0</i>[12];
} <code>xcb_randr_get_provider_property_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_randr_get_provider_property_reply_t *<code>xcb_randr_get_provider_property_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_randr_get_provider_property_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>void *<code>xcb_randr_get_provider_property_data</code>(const xcb_randr_get_provider_property_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_randr_get_provider_property_data_length</code>(const xcb_randr_get_provider_property_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_randr_get_provider_property_data_end</code>(const xcb_randr_get_provider_property_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>provider</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>property</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>long_offset</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>long_length</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>_delete</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pending</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_RANDR_GET_PROVIDER_PROPERTY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bytes_after</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_items</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_randr_get_provider_property_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_randr_get_provider_property_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_randr_get_provider_property_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
