---
title: "xcb_xkb_get_geometry_label_font(3)"
name: "xcb_xkb_get_geometry_label_font"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_geometry_label_font/"
description: "xcb_xkb_get_geometry –"
---

<p>xcb_xkb_get_geometry &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;
Request function
xcb_xkb_get_geometry_cookie_t xcb_xkb_get_geometry(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, xcb_atom_t name);</code></pre>
<h3>Reply datastructure</h3>
<pre>typedef struct xcb_xkb_get_geometry_reply_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>deviceID</i>;
 uint16_t <i>sequence</i>;
 uint32_t <i>length</i>;
 xcb_atom_t <i>name</i>;
 uint8_t <i>found</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>widthMM</i>;
 uint16_t <i>heightMM</i>;
 uint16_t <i>nProperties</i>;
 uint16_t <i>nColors</i>;
 uint16_t <i>nShapes</i>;
 uint16_t <i>nSections</i>;
 uint16_t <i>nDoodads</i>;
 uint16_t <i>nKeyAliases</i>;
 uint8_t <i>baseColorNdx</i>;
 uint8_t <i>labelColorNdx</i>;
} <code>xcb_xkb_get_geometry_reply_t</code>;</pre>
<h3>Reply function</h3>
<dl>
<dd>xcb_xkb_get_geometry_reply_t *<code>xcb_xkb_get_geometry_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_geometry_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dd></dl>
<h3>Reply accessors</h3>
<p>xcb_xkb_counted_string_16_t *xcb_xkb_get_geometry_label_font (const xcb_xkb_get_geometry_request_t *reply)</p>
<dl>
<dd>int <code>xcb_xkb_get_geometry_properties_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_property_iterator_t <code>xcb_xkb_get_geometry_properties_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xkb_get_geometry_colors_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_counted_string_16_iterator_t <code>xcb_xkb_get_geometry_colors_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xkb_get_geometry_shapes_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_shape_iterator_t <code>xcb_xkb_get_geometry_shapes_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xkb_get_geometry_sections_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_section_iterator_t <code>xcb_xkb_get_geometry_sections_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xkb_get_geometry_doodads_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_doodad_iterator_t <code>xcb_xkb_get_geometry_doodads_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_key_alias_t *<code>xcb_xkb_get_geometry_key_aliases</code>(const xcb_xkb_get_geometry_request_t *<i>reply</i>);</dd>
<dd>int <code>xcb_xkb_get_geometry_key_aliases_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</dd>
<dd>xcb_xkb_key_alias_iterator_t <code>xcb_xkb_get_geometry_key_aliases_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);
</dd></dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>name</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_GEOMETRY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>length</i></dt>
<dd>The length of the reply, in words (a word is 4 bytes).</dd>
<dt><i>deviceID</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>name</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>found</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>widthMM</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>heightMM</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nProperties</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nColors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nShapes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nSections</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nDoodads</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyAliases</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>baseColorNdx</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>labelColorNdx</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_geometry_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_geometry_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_geometry_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
