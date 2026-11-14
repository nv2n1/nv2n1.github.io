---
title: "xcb_test_fake_input_checked(3)"
name: "xcb_test_fake_input_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_test_fake_input_checked/"
description: "xcb_test_fake_input –"
---

<p>xcb_test_fake_input &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xtest.h&gt;


Request function



xcb_void_cookie_t xcb_test_fake_input(xcb_connection_t *conn, uint8_t type, uint8_t detail, uint32_t time, xcb_window_t root, int16_t rootX, int16_t rootY, uint8_t deviceid);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>type</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>detail</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>root</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rootX</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>rootY</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>deviceid</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_test_fake_input_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xtest.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
