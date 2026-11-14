---
title: "xcb_xkb_bell_checked(3)"
name: "xcb_xkb_bell_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_bell_checked/"
description: "xcb_xkb_bell –"
---

<p>xcb_xkb_bell &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_void_cookie_t xcb_xkb_bell(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, xcb_xkb_bell_class_spec_t bellClass, xcb_xkb_id_spec_t bellID, int8_t percent, uint8_t forceSound, uint8_t eventOnly, int16_t pitch, int16_t duration, xcb_atom_t name, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bellClass</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>bellID</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>percent</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>forceSound</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>eventOnly</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>pitch</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>duration</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>name</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_bell_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
