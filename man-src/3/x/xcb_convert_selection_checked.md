---
title: "xcb_convert_selection_checked(3)"
name: "xcb_convert_selection_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_convert_selection_checked/"
description: "xcb_convert_selection –"
---

<p>xcb_convert_selection &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_convert_selection(xcb_connection_t *conn, xcb_window_t requestor, xcb_atom_t selection, xcb_atom_t target, xcb_atom_t property, xcb_timestamp_t time);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>requestor</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>selection</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>target</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>property</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_convert_selection_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
