---
title: "xcb_render_create_linear_gradient_checked(3)"
name: "xcb_render_create_linear_gradient_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_render_create_linear_gradient_checked/"
description: "xcb_render_create_linear_gradient –"
---

<p>xcb_render_create_linear_gradient &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/render.h&gt;
Request function
    xcb_void_cookie_t
    xcb_render_create_linear_gradient(xcb_connection_t *conn, xcb_render_picture_t picture, xcb_render_pointfix_t p1, xcb_render_pointfix_t p2, uint32_t num_stops, const xcb_render_fixed_t *stops, const xcb_render_color_t *colors);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>picture</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>p1</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>p2</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>num_stops</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>stops</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>colors</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_render_create_linear_gradient_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from render.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
