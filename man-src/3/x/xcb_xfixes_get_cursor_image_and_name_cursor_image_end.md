---
title: "xcb_xfixes_get_cursor_image_and_name_cursor_image_end(3)"
name: "xcb_xfixes_get_cursor_image_and_name_cursor_image_end"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xfixes_get_cursor_image_and_name_cursor_image_end/"
description: "xcb_xfixes_get_cursor_image_and_name –"
---

<p>xcb_xfixes_get_cursor_image_and_name &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xfixes.h&gt;
Request function
xcb_xfixes_get_cursor_image_and_name_cookie_t xcb_xfixes_get_cursor_image_and_name(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xfixes_get_cursor_image_and_name_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 int16_t <i>x</i>;
 int16_t <i>y</i>;
 uint16_t <i>width</i>;
 uint16_t <i>height</i>;
 uint16_t <i>xhot</i>;
 uint16_t <i>yhot</i>;
 uint32_t <i>cursor_serial</i>;
 xcb_atom_t <i>cursor_atom</i>;
 uint16_t <i>nbytes</i>;
 uint8_t <i>pad1</i>[2];
} <code>xcb_xfixes_get_cursor_image_and_name_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xfixes_get_cursor_image_and_name_reply_t *<code>xcb_xfixes_get_cursor_image_and_name_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xfixes_get_cursor_image_and_name_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>uint32_t *<code>xcb_xfixes_get_cursor_image_and_name_cursor_image</code>(const xcb_xfixes_get_cursor_image_and_name_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xfixes_get_cursor_image_and_name_cursor_image_length</code>(const xcb_xfixes_get_cursor_image_and_name_reply_t *<i>reply</i>);</dd>
<dd>xcb_generic_iterator_t <code>xcb_xfixes_get_cursor_image_and_name_cursor_image_end</code>(const xcb_xfixes_get_cursor_image_and_name_reply_t *<i>reply</i>);</dd>
<dd>char *<code>xcb_xfixes_get_cursor_image_and_name_name</code>(const xcb_xfixes_get_cursor_image_and_name_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xfixes_get_cursor_image_and_name_name_length</code>(const xcb_xfixes_get_cursor_image_and_name_reply_t *<i>reply</i>);</dd>
<dd>xcb_generic_iterator_t <code>xcb_xfixes_get_cursor_image_and_name_name_end</code>(const xcb_xfixes_get_cursor_image_and_name_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_XFIXES_GET_CURSOR_IMAGE_AND_NAME</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>xhot</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>yhot</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>cursor_serial</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>cursor_atom</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nbytes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xfixes_get_cursor_image_and_name_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xfixes_get_cursor_image_and_name_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xfixes_get_cursor_image_and_name_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xfixes.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
