---
title: "xcb_xkb_get_geometry_properties_length(3)"
name: "xcb_xkb_get_geometry_properties_length"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_get_geometry_properties_length/"
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
<dd>xcb_xkb_get_geometry_reply_t *<code>xcb_xkb_get_geometry_reply</code>(xcb_connection_t&nbsp;<wbr>*<i>conn</i>, xcb_xkb_get_geometry_cookie_t&nbsp;<wbr><i>cookie</i>, xcb_generic_error_t&nbsp;<wbr>**<i>e</i>);</dl>
<h3>Reply accessors</h3>
<p>xcb_xkb_counted_string_16_t *xcb_xkb_get_geometry_label_font (const xcb_xkb_get_geometry_request_t *reply)</p>
<dl>
<dd>int <code>xcb_xkb_get_geometry_properties_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_property_iterator_t <code>xcb_xkb_get_geometry_properties_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_geometry_colors_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_counted_string_16_iterator_t <code>xcb_xkb_get_geometry_colors_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_geometry_shapes_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_shape_iterator_t <code>xcb_xkb_get_geometry_shapes_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_geometry_sections_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_section_iterator_t <code>xcb_xkb_get_geometry_sections_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_geometry_doodads_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_doodad_iterator_t <code>xcb_xkb_get_geometry_doodads_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_key_alias_t *<code>xcb_xkb_get_geometry_key_aliases</code>(const xcb_xkb_get_geometry_request_t *<i>reply</i>);</p>
<dd>int <code>xcb_xkb_get_geometry_key_aliases_length</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);</p>
<dd>xcb_xkb_key_alias_iterator_t <code>xcb_xkb_get_geometry_key_aliases_iterator</code>(const xcb_xkb_get_geometry_reply_t *<i>reply</i>);
</dl>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Reply Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this reply, in this case <i>XCB_XKB_GET_GEOMETRY</i>. This field is also present in the <i>xcb_generic_reply_t</i> and can be used to tell replies apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>length</i></p>
<dd>The length of the reply, in words (a word is 4 bytes).</p>
<dt><i>deviceID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>found</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>widthMM</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>heightMM</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nProperties</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nColors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nShapes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nSections</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nDoodads</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyAliases</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>baseColorNdx</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>labelColorNdx</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_xkb_get_geometry_cookie_t</i>. Errors have to be handled when calling the reply function <i>xcb_xkb_get_geometry_reply</i>. </p>
<p> If you want to handle errors in the event loop instead, use <i>xcb_xkb_get_geometry_unchecked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
