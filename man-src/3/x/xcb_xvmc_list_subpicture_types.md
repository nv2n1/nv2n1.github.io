---
title: "xcb_xvmc_list_subpicture_types(3)"
name: "xcb_xvmc_list_subpicture_types"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xvmc_list_subpicture_types/"
description: "xcb_xvmc_list_subpicture_types –"
---

<p>xcb_xvmc_list_subpicture_types &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xvmc.h&gt;


Request function



xcb_xvmc_list_subpicture_types_cookie_t xcb_xvmc_list_subpicture_types(xcb_connection_t *conn, xcb_xv_port_t port_id, xcb_xvmc_surface_t surface_id);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xvmc_list_subpicture_types_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>num</i>;
 uint8_t <i>pad1</i>[20];
} <code>xcb_xvmc_list_subpicture_types_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xvmc_list_subpicture_types_reply_t *<code>xcb_xvmc_list_subpicture_types_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xvmc_list_subpicture_types_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_xv_image_format_info_t *<code>xcb_xvmc_list_subpicture_types_types</code>(const xcb_xvmc_list_subpicture_types_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xvmc_list_subpicture_types_types_length</code>(const xcb_xvmc_list_subpicture_types_reply_t *<i>reply</i>);</p>
<dd>xcb_xv_image_format_info_iterator_t <code>xcb_xvmc_list_subpicture_types_types_iterator</code>(const xcb_xvmc_list_subpicture_types_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>port_id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>surface_id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XVMC_LIST_SUBPICTURE_TYPES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>num</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xvmc_list_subpicture_types_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xvmc_list_subpicture_types_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xvmc_list_subpicture_types_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xvmc.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
