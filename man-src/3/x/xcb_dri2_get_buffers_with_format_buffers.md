---
title: "xcb_dri2_get_buffers_with_format_buffers(3)"
name: "xcb_dri2_get_buffers_with_format_buffers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_dri2_get_buffers_with_format_buffers/"
description: "xcb_dri2_get_buffers_with_format –"
---

<p>xcb_dri2_get_buffers_with_format &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/dri2.h&gt;
Request function
    xcb_dri2_get_buffers_with_format_cookie_t
    xcb_dri2_get_buffers_with_format(xcb_connection_t *conn, xcb_drawable_t drawable, uint32_t count, uint32_t attachments_len, const xcb_dri2_attach_format_t *attachments);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_dri2_get_buffers_with_format_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>width</i>;
 uint32_t <i>height</i>;
 uint32_t <i>count</i>;
 uint8_t <i>pad1</i>[12];
} <code>xcb_dri2_get_buffers_with_format_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_dri2_get_buffers_with_format_reply_t *<code>xcb_dri2_get_buffers_with_format_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_dri2_get_buffers_with_format_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_dri2_dri2_buffer_t *<code>xcb_dri2_get_buffers_with_format_buffers</code>(const xcb_dri2_get_buffers_with_format_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_dri2_get_buffers_with_format_buffers_length</code>(const xcb_dri2_get_buffers_with_format_reply_t *<i>reply</i>);</dd>
<dd>xcb_dri2_dri2_buffer_iterator_t <code>xcb_dri2_get_buffers_with_format_buffers_iterator</code>(const xcb_dri2_get_buffers_with_format_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>count</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>attachments_len</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>attachments</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_DRI2_GET_BUFFERS_WITH_FORMAT</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>count</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_dri2_get_buffers_with_format_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_dri2_get_buffers_with_format_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_dri2_get_buffers_with_format_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from dri2.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
