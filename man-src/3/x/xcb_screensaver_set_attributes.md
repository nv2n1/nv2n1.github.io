---
title: "xcb_screensaver_set_attributes(3)"
name: "xcb_screensaver_set_attributes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_screensaver_set_attributes/"
description: "xcb_screensaver_set_attributes –"
---

<p>xcb_screensaver_set_attributes &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/screensaver.h&gt;
Request function
    xcb_void_cookie_t
    xcb_screensaver_set_attributes(xcb_connection_t *conn, xcb_drawable_t drawable, int16_t x, int16_t y, uint16_t width, uint16_t height, uint16_t border_width, uint8_t _class, uint8_t depth, xcb_visualid_t visual, uint32_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>drawable</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>border_width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>_class</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>depth</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>visual</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>value_mask</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>value_list</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_screensaver_set_attributes_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from screensaver.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
