---
title: "xcb_xkb_get_names(3)"
name: "xcb_xkb_get_names"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_names/"
description: "xcb_xkb_get_names –"
---

<p>xcb_xkb_get_names &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_xkb_get_names_cookie_t xcb_xkb_get_names(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint32_t which);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_names_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 uint32_t <i>which</i>;
 xcb_keycode_t <i>minKeyCode</i>;
 xcb_keycode_t <i>maxKeyCode</i>;
 uint8_t <i>nTypes</i>;
 uint8_t <i>groupNames</i>;
 uint16_t <i>virtualMods</i>;
 xcb_keycode_t <i>firstKey</i>;
 uint8_t <i>nKeys</i>;
 uint32_t <i>indicators</i>;
 uint8_t <i>nRadioGroups</i>;
 uint8_t <i>nKeyAliases</i>;
 uint16_t <i>nKTLevels</i>;
 uint8_t <i>pad0</i>[4];
} <code>xcb_xkb_get_names_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_names_reply_t *<code>xcb_xkb_get_names_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_names_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<p>xcb_xkb_get_names_value_list_t *xcb_xkb_get_names_value_list (const xcb_xkb_get_names_request_t *reply)</p>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>which</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_NAMES</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>which</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>minKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>maxKeyCode</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupNames</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>virtualMods</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>firstKey</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeys</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>indicators</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nRadioGroups</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyAliases</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKTLevels</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_names_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_names_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_names_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
