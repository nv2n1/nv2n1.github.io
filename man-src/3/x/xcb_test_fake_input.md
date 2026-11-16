---
title: "xcb_test_fake_input(3)"
name: "xcb_test_fake_input"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_test_fake_input/"
description: "xcb_test_fake_input –"
---

<p>xcb_test_fake_input &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xtest.h&gt;
Request function
xcb_void_cookie_t xcb_test_fake_input(xcb_connection_t *conn, uint8_t type, uint8_t detail, uint32_t time, xcb_window_t root, int16_t rootX, int16_t rootY, uint8_t deviceid);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>type</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>detail</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>root</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>rootX</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>rootY</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>deviceid</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_test_fake_input_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xtest.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
