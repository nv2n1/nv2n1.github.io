---
title: "xcb_render_create_glyph_set_checked(3)"
name: "xcb_render_create_glyph_set_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_render_create_glyph_set_checked/"
description: "xcb_render_create_glyph_set –"
---

<p>xcb_render_create_glyph_set &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/render.h&gt;


Request function



xcb_void_cookie_t xcb_render_create_glyph_set(xcb_connection_t *conn, xcb_render_glyphset_t gsid, xcb_render_pictformat_t format);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>gsid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>format</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_render_create_glyph_set_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from render.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
