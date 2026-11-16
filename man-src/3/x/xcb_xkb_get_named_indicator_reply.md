---
title: "xcb_xkb_get_named_indicator_reply(3)"
name: "xcb_xkb_get_named_indicator_reply"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_named_indicator_reply/"
description: "xcb_xkb_get_named_indicator –"
---

<p>xcb_xkb_get_named_indicator &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;
Request function
xcb_xkb_get_named_indicator_cookie_t xcb_xkb_get_named_indicator(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, xcb_xkb_led_class_spec_t ledClass, xcb_xkb_id_spec_t ledID, xcb_atom_t indicator);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_named_indicator_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>indicator</i>;
 uint8_t <i>found</i>;
 uint8_t <i>on</i>;
 uint8_t <i>realIndicator</i>;
 uint8_t <i>ndx</i>;
 uint8_t <i>map_flags</i>;
 uint8_t <i>map_whichGroups</i>;
 uint8_t <i>map_groups</i>;
 uint8_t <i>map_whichMods</i>;
 uint8_t <i>map_mods</i>;
 uint8_t <i>map_realMods</i>;
 uint16_t <i>map_vmod</i>;
 uint32_t <i>map_ctrls</i>;
 uint8_t <i>supported</i>;
 uint8_t <i>pad0</i>[3];
} <code>xcb_xkb_get_named_indicator_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_named_indicator_reply_t *<code>xcb_xkb_get_named_indicator_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_named_indicator_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ledClass</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ledID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>indicator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_NAMED_INDICATOR</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>deviceID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>indicator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>found</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>on</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>realIndicator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>ndx</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_flags</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_whichGroups</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_groups</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_whichMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_mods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_realMods</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_vmod</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>map_ctrls</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>supported</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_named_indicator_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_named_indicator_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_named_indicator_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
