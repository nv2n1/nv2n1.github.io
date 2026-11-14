---
title: "xcb_render_create_radial_gradient(3)"
name: "xcb_render_create_radial_gradient"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_render_create_radial_gradient/"
description: "xcb_render_create_radial_gradient –"
---

<p>xcb_render_create_radial_gradient &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/render.h&gt;

Request function

    xcb_void_cookie_t
    xcb_render_create_radial_gradient(xcb_connection_t *conn, xcb_render_picture_t picture, xcb_render_pointfix_t inner, xcb_render_pointfix_t outer, xcb_render_fixed_t inner_radius, xcb_render_fixed_t outer_radius, uint32_t num_stops, const xcb_render_fixed_t *stops, const xcb_render_color_t *colors);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>picture</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>inner</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>outer</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>inner_radius</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>outer_radius</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>num_stops</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>stops</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>colors</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_render_create_radial_gradient_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from render.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
