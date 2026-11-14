---
title: "xcb_input_xi_change_hierarchy(3)"
name: "xcb_input_xi_change_hierarchy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_input_xi_change_hierarchy/"
description: "xcb_input_xi_change_hierarchy –"
---

<p>xcb_input_xi_change_hierarchy &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xinput.h&gt;

Request function

    xcb_void_cookie_t
    xcb_input_xi_change_hierarchy(xcb_connection_t *conn, uint8_t num_changes, const xcb_input_hierarchy_change_t *changes);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>num_changes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>changes</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_input_xi_change_hierarchy_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xinput.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
