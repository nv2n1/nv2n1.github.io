---
title: "xcb_xkb_set_geometry(3)"
name: "xcb_xkb_set_geometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_geometry/"
description: "xcb_xkb_set_geometry –"
---

<p>xcb_xkb_set_geometry &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;

Request function

    xcb_void_cookie_t
    xcb_xkb_set_geometry(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint8_t nShapes, uint8_t nSections, xcb_atom_t name, uint16_t widthMM, uint16_t heightMM, uint16_t nProperties, uint16_t nColors, uint16_t nDoodads, uint16_t nKeyAliases, uint8_t baseColorNdx, uint8_t labelColorNdx, xcb_xkb_counted_string_16_t *labelFont, const xcb_xkb_property_t *properties, const xcb_xkb_counted_string_16_t *colors, const xcb_xkb_shape_t *shapes, const xcb_xkb_section_t *sections, const xcb_xkb_doodad_t *doodads, const xcb_xkb_key_alias_t *keyAliases);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nShapes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nSections</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>widthMM</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>heightMM</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nProperties</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nColors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nDoodads</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>nKeyAliases</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>baseColorNdx</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>labelColorNdx</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>labelFont</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>properties</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>colors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>shapes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>sections</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>doodads</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>keyAliases</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_geometry_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
