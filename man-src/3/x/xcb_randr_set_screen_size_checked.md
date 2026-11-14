---
title: "xcb_randr_set_screen_size_checked(3)"
name: "xcb_randr_set_screen_size_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_randr_set_screen_size_checked/"
description: "xcb_randr_set_screen_size –"
---

<p>xcb_randr_set_screen_size &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/randr.h&gt;


Request function



xcb_void_cookie_t xcb_randr_set_screen_size(xcb_connection_t *conn, xcb_window_t window, uint16_t width, uint16_t height, uint32_t mm_width, uint32_t mm_height);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>window</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mm_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>mm_height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_randr_set_screen_size_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from randr.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
