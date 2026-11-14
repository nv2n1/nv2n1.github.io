---
title: "xcb_selinux_list_selections_selections_iterator(3)"
name: "xcb_selinux_list_selections_selections_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_selinux_list_selections_selections_iterator/"
description: "xcb_selinux_list_selections –"
---

<p>xcb_selinux_list_selections &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xselinux.h&gt;


Request function



xcb_selinux_list_selections_cookie_t xcb_selinux_list_selections(xcb_connection_t *conn,</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_selinux_list_selections_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>selections_len</i>;
 uint8_t <i>pad1</i>[20];
} <code>xcb_selinux_list_selections_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_selinux_list_selections_reply_t *<code>xcb_selinux_list_selections_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_selinux_list_selections_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_selinux_list_selections_selections_length</code>(const xcb_selinux_list_selections_reply_t *<i>reply</i>);</p>
<dd>xcb_selinux_list_item_iterator_t <code>xcb_selinux_list_selections_selections_iterator</code>(const xcb_selinux_list_selections_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_SELINUX_LIST_SELECTIONS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>selections_len</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_selinux_list_selections_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_selinux_list_selections_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_selinux_list_selections_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xselinux.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
