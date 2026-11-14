---
title: "xcb_circulate_window(3)"
name: "xcb_circulate_window"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_circulate_window/"
description: "xcb_circulate_window – Change window stacking order"
---

<p>xcb_circulate_window &#8211; Change window stacking order</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_circulate_window(xcb_connection_t *conn, uint8_t direction, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>direction</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_CIRCULATE_RAISE_LOWEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_CIRCULATE_LOWER_HIGHEST</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd></dl>
<dt><i>window</i></p>
<dd>The window to raise/lower (depending on <i>direction</i>).</dl>
<h2>Description</h2>
<p>If <i>direction</i> is <i>XCB_CIRCULATE_RAISE_LOWEST</i>, the lowest mapped child (if any) will be raised to the top of the stack. </p>
<p> If <i>direction</i> is <i>XCB_CIRCULATE_LOWER_HIGHEST</i>, the highest mapped child will be lowered to the bottom of the stack.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_circulate_window_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_value_error_t</i></p>
<dd>The specified <i>direction</i> is invalid.</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>window</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
