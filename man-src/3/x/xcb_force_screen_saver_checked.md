---
title: "xcb_force_screen_saver_checked(3)"
name: "xcb_force_screen_saver_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_force_screen_saver_checked/"
description: "xcb_force_screen_saver –"
---

<p>xcb_force_screen_saver &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_force_screen_saver(xcb_connection_t *conn, uint8_t mode);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>mode</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_SCREEN_SAVER_RESET</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>XCB_SCREEN_SAVER_ACTIVE</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_force_screen_saver_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
