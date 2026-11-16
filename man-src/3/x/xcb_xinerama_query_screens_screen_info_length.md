---
title: "xcb_xinerama_query_screens_screen_info_length(3)"
name: "xcb_xinerama_query_screens_screen_info_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xinerama_query_screens_screen_info_length/"
description: "xcb_xinerama_query_screens –"
---

<p>xcb_xinerama_query_screens &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinerama.h&gt;
Request function
xcb_xinerama_query_screens_cookie_t xcb_xinerama_query_screens(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xinerama_query_screens_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>number</i>;
 uint8_t <i>pad1</i>[20];
} <code>xcb_xinerama_query_screens_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xinerama_query_screens_reply_t *<code>xcb_xinerama_query_screens_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xinerama_query_screens_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_xinerama_screen_info_t *<code>xcb_xinerama_query_screens_screen_info</code>(const xcb_xinerama_query_screens_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xinerama_query_screens_screen_info_length</code>(const xcb_xinerama_query_screens_reply_t *<i>reply</i>);</dd>
<dd>xcb_xinerama_screen_info_iterator_t <code>xcb_xinerama_query_screens_screen_info_iterator</code>(const xcb_xinerama_query_screens_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_XINERAMA_QUERY_SCREENS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>number</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xinerama_query_screens_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xinerama_query_screens_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xinerama_query_screens_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinerama.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
