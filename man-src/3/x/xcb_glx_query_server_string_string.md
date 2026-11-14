---
title: "xcb_glx_query_server_string_string(3)"
name: "xcb_glx_query_server_string_string"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_glx_query_server_string_string/"
description: "xcb_glx_query_server_string –"
---

<p>xcb_glx_query_server_string &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/glx.h&gt;


Request function



xcb_glx_query_server_string_cookie_t xcb_glx_query_server_string(xcb_connection_t *conn, uint32_t screen, uint32_t name);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_glx_query_server_string_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>pad1</i>[4];
 uint32_t <i>str_len</i>;
 uint8_t <i>pad2</i>[16];
} <code>xcb_glx_query_server_string_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_glx_query_server_string_reply_t *<code>xcb_glx_query_server_string_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_glx_query_server_string_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>char *<code>xcb_glx_query_server_string_string</code>(const xcb_glx_query_server_string_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_glx_query_server_string_string_length</code>(const xcb_glx_query_server_string_reply_t *<i>reply</i>);</p>
<dd>xcb_generic_iterator_t <code>xcb_glx_query_server_string_string_end</code>(const xcb_glx_query_server_string_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>screen</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_GLX_QUERY_SERVER_STRING</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>str_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_glx_query_server_string_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_glx_query_server_string_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_glx_query_server_string_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from glx.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
