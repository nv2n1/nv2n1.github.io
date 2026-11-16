---
title: "xcb_xkb_set_geometry_checked(3)"
name: "xcb_xkb_set_geometry_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_set_geometry_checked/"
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
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>deviceSpec</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nShapes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nSections</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>name</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>widthMM</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>heightMM</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nProperties</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nColors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nDoodads</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>nKeyAliases</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>baseColorNdx</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>labelColorNdx</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>labelFont</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>properties</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>colors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>shapes</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>sections</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>doodads</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>keyAliases</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_set_geometry_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
