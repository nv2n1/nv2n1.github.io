---
title: "xcb_input_xi_warp_pointer(3)"
name: "xcb_input_xi_warp_pointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_xi_warp_pointer/"
description: "xcb_input_xi_warp_pointer –"
---

<p>xcb_input_xi_warp_pointer &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;


Request function



xcb_void_cookie_t xcb_input_xi_warp_pointer(xcb_connection_t *conn, xcb_window_t src_win, xcb_window_t dst_win, xcb_input_fp1616_t src_x, xcb_input_fp1616_t src_y, uint16_t src_width, uint16_t src_height, xcb_input_fp1616_t dst_x, xcb_input_fp1616_t dst_y, xcb_input_device_id_t deviceid);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>src_win</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_win</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_width</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>src_height</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_x</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>dst_y</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>deviceid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_xi_warp_pointer_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
