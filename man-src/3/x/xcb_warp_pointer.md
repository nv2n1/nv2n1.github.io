---
title: "xcb_warp_pointer(3)"
name: "xcb_warp_pointer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_warp_pointer/"
description: "xcb_warp_pointer – move mouse pointer"
---

<p>xcb_warp_pointer &#8211; move mouse pointer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_warp_pointer(xcb_connection_t *conn, xcb_window_t src_window, xcb_window_t dst_window, int16_t src_x, int16_t src_y, uint16_t src_width, uint16_t src_height, int16_t dst_x, int16_t dst_y);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>src_window</i></dt>
<dd>If <i>src_window</i> is not <i>XCB_NONE</i> (TODO), the move will only take place if the pointer is inside <i>src_window</i> and within the rectangle specified by (<i>src_x</i>, <i>src_y</i>, <i>src_width</i>, <i>src_height</i>). The rectangle coordinates are relative to <i>src_window</i>.</dd>
<dt><i>dst_window</i></dt>
<dd>If <i>dst_window</i> is not <i>XCB_NONE</i> (TODO), the pointer will be moved to the offsets (<i>dst_x</i>, <i>dst_y</i>) relative to <i>dst_window</i>. If <i>dst_window</i> is <i>XCB_NONE</i> (TODO), the pointer will be moved by the offsets (<i>dst_x</i>, <i>dst_y</i>) relative to the current position of the pointer.</dd>
<dt><i>src_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_width</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>src_height</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_x</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>dst_y</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<p>Moves the mouse pointer to the specified position. </p>
<p> If <i>src_window</i> is not <i>XCB_NONE</i> (TODO), the move will only take place if the pointer is inside <i>src_window</i> and within the rectangle specified by (<i>src_x</i>, <i>src_y</i>, <i>src_width</i>, <i>src_height</i>). The rectangle coordinates are relative to <i>src_window</i>. </p>
<p> If <i>dst_window</i> is not <i>XCB_NONE</i> (TODO), the pointer will be moved to the offsets (<i>dst_x</i>, <i>dst_y</i>) relative to <i>dst_window</i>. If <i>dst_window</i> is <i>XCB_NONE</i> (TODO), the pointer will be moved by the offsets (<i>dst_x</i>, <i>dst_y</i>) relative to the current position of the pointer.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_warp_pointer_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_window_error_t</i></dt>
<dd>TODO: reasons?</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_set_input_focus/">xcb_set_input_focus</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
