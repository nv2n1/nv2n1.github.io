---
title: "xcb_present_query_capabilities_unchecked(3)"
name: "xcb_present_query_capabilities_unchecked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_present_query_capabilities_unchecked/"
description: "xcb_present_query_capabilities –"
---

<p>xcb_present_query_capabilities &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/present.h&gt;


Request function



xcb_present_query_capabilities_cookie_t xcb_present_query_capabilities(xcb_connection_t *conn, uint32_t target);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_present_query_capabilities_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>capabilities</i>;
} <code>xcb_present_query_capabilities_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_present_query_capabilities_reply_t *<code>xcb_present_query_capabilities_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_present_query_capabilities_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>target</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_PRESENT_QUERY_CAPABILITIES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>capabilities</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_present_query_capabilities_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_present_query_capabilities_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_present_query_capabilities_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from present.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
