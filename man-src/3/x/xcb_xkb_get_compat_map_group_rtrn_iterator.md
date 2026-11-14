---
title: "xcb_xkb_get_compat_map_group_rtrn_iterator(3)"
name: "xcb_xkb_get_compat_map_group_rtrn_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_compat_map_group_rtrn_iterator/"
description: "xcb_xkb_get_compat_map –"
---

<p>xcb_xkb_get_compat_map &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_get_compat_map_cookie_t xcb_xkb_get_compat_map(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint8_t groups, uint8_t getAllSI, uint16_t firstSI, uint16_t nSI);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_compat_map_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint8_t <i>groupsRtrn</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>firstSIRtrn</i>;
 uint16_t <i>nSIRtrn</i>;
 uint16_t <i>nTotalSI</i>;
 uint8_t <i>pad1</i>[16];
} <code>xcb_xkb_get_compat_map_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_compat_map_reply_t *<code>xcb_xkb_get_compat_map_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_compat_map_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>xcb_xkb_sym_interpret_t *<code>xcb_xkb_get_compat_map_si_rtrn</code>(const xcb_xkb_get_compat_map_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_compat_map_si_rtrn_length</code>(const xcb_xkb_get_compat_map_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_sym_interpret_iterator_t <code>xcb_xkb_get_compat_map_si_rtrn_iterator</code>(const xcb_xkb_get_compat_map_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_mod_def_t *<code>xcb_xkb_get_compat_map_group_rtrn</code>(const xcb_xkb_get_compat_map_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_compat_map_group_rtrn_length</code>(const xcb_xkb_get_compat_map_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_mod_def_iterator_t <code>xcb_xkb_get_compat_map_group_rtrn_iterator</code>(const xcb_xkb_get_compat_map_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groups</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>getAllSI</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstSI</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nSI</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_COMPAT_MAP</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupsRtrn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstSIRtrn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nSIRtrn</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTotalSI</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_compat_map_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_compat_map_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_compat_map_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
