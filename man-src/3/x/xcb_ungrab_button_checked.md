---
title: "xcb_ungrab_button_checked(3)"
name: "xcb_ungrab_button_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_ungrab_button_checked/"
description: "xcb_ungrab_button –"
---

<p>xcb_ungrab_button &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_ungrab_button(xcb_connection_t *conn, uint8_t button, xcb_window_t grab_window, uint16_t modifiers);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>button</i></dt>
<dd>One of the following values:</dd>
<dl>
<dd>
</dd><dl>
<dt><i>XCB_BUTTON_INDEX_ANY</i></dt>
<dd>Any of the following (or none):</dd>
<dt><i>XCB_BUTTON_INDEX_1</i></dt>
<dd>The left mouse button.</dd>
<dt><i>XCB_BUTTON_INDEX_2</i></dt>
<dd>The right mouse button.</dd>
<dt><i>XCB_BUTTON_INDEX_3</i></dt>
<dd>The middle mouse button.</dd>
<dt><i>XCB_BUTTON_INDEX_4</i></dt>
<dd>Scroll wheel. TODO: direction?</dd>
<dt><i>XCB_BUTTON_INDEX_5</i></dt>
<dd>Scroll wheel. TODO: direction?</dd></dl>
</dl>
<dl>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<dt><i>grab_window</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>modifiers</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_ungrab_button_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
