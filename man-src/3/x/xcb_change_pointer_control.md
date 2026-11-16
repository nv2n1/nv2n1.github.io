---
title: "xcb_change_pointer_control(3)"
name: "xcb_change_pointer_control"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_pointer_control/"
description: "xcb_change_pointer_control –"
---

<p>xcb_change_pointer_control &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_change_pointer_control(xcb_connection_t *conn, int16_t acceleration_numerator, int16_t acceleration_denominator, int16_t threshold, uint8_t do_acceleration, uint8_t do_threshold);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>acceleration_numerator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>acceleration_denominator</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>threshold</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>do_acceleration</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>do_threshold</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_pointer_control_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
