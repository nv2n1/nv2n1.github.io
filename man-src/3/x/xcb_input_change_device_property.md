---
title: "xcb_input_change_device_property(3)"
name: "xcb_input_change_device_property"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_change_device_property/"
description: "xcb_input_change_device_property –"
---

<p>xcb_input_change_device_property &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;
Request function
    xcb_void_cookie_t
    xcb_input_change_device_property(xcb_connection_t *conn, xcb_atom_t property, xcb_atom_t type, uint8_t device_id, uint8_t format, uint8_t mode, uint32_t num_items, const void *items);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>property</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>type</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>device_id</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>format</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>mode</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>num_items</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>items</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_change_device_property_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
