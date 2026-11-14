---
title: "xcb_xkb_set_debugging_flags(3)"
name: "xcb_xkb_set_debugging_flags"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_debugging_flags/"
description: "xcb_xkb_set_debugging_flags –"
---

<p>xcb_xkb_set_debugging_flags &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;

Request function

    xcb_xkb_set_debugging_flags_cookie_t
    xcb_xkb_set_debugging_flags(xcb_connection_t *conn, uint16_t msgLength, uint32_t affectFlags, uint32_t flags, uint32_t affectCtrls, uint32_t ctrls, const xcb_xkb_string8_t *message);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_set_debugging_flags_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>currentFlags</i>;
 uint32_t <i>currentCtrls</i>;
 uint32_t <i>supportedFlags</i>;
 uint32_t <i>supportedCtrls</i>;
 uint8_t <i>pad1</i>[8];
} <code>xcb_xkb_set_debugging_flags_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_set_debugging_flags_reply_t *<code>xcb_xkb_set_debugging_flags_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_set_debugging_flags_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>msgLength</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectFlags</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>flags</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectCtrls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>ctrls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>message</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_SET_DEBUGGING_FLAGS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>currentFlags</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>currentCtrls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>supportedFlags</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>supportedCtrls</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_set_debugging_flags_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_set_debugging_flags_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_set_debugging_flags_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
