---
title: "xcb_input_xi_get_property_unchecked(3)"
name: "xcb_input_xi_get_property_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_xi_get_property_unchecked/"
description: "xcb_input_xi_get_property –"
---

<p>xcb_input_xi_get_property &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;


Request function



xcb_input_xi_get_property_cookie_t xcb_input_xi_get_property(xcb_connection_t *conn, xcb_input_device_id_t deviceid, uint8_t _delete, xcb_atom_t property, xcb_atom_t type, uint32_t offset, uint32_t len);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_input_xi_get_property_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>type</i>;
 uint32_t <i>bytes_after</i>;
 uint32_t <i>num_items</i>;
 uint8_t <i>format</i>;
 uint8_t <i>pad1</i>[11];
} <code>xcb_input_xi_get_property_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_input_xi_get_property_reply_t *<code>xcb_input_xi_get_property_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_input_xi_get_property_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<p>xcb_input_xi_get_property_items_t *xcb_input_xi_get_property_items (const xcb_input_xi_get_property_request_t *reply)</p>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>_delete</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>property</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>offset</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_INPUT_XI_GET_PROPERTY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bytes_after</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_items</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_input_xi_get_property_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_input_xi_get_property_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_input_xi_get_property_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
