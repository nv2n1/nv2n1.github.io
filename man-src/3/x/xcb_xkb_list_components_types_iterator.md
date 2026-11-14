---
title: "xcb_xkb_list_components_types_iterator(3)"
name: "xcb_xkb_list_components_types_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_list_components_types_iterator/"
description: "xcb_xkb_list_components –"
---

<p>xcb_xkb_list_components &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_list_components_cookie_t xcb_xkb_list_components(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint16_t maxNames);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_list_components_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint16_t <i>nKeymaps</i>;
 uint16_t <i>nKeycodes</i>;
 uint16_t <i>nTypes</i>;
 uint16_t <i>nCompatMaps</i>;
 uint16_t <i>nSymbols</i>;
 uint16_t <i>nGeometries</i>;
 uint16_t <i>extra</i>;
 uint8_t <i>pad0</i>[10];
} <code>xcb_xkb_list_components_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_list_components_reply_t *<code>xcb_xkb_list_components_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_list_components_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<dl>
<dd>int <code>xcb_xkb_list_components_keymaps_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_keymaps_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_list_components_keycodes_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_keycodes_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_list_components_types_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_types_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_list_components_compat_maps_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_compat_maps_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_list_components_symbols_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_symbols_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_list_components_geometries_length</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_listing_iterator_t <code>xcb_xkb_list_components_geometries_iterator</code>(const xcb_xkb_list_components_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>maxNames</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_LIST_COMPONENTS</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeymaps</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeycodes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nCompatMaps</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nSymbols</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nGeometries</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>extra</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_list_components_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_list_components_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_list_components_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
