---
title: "xcb_sync_change_counter_checked(3)"
name: "xcb_sync_change_counter_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_sync_change_counter_checked/"
description: "xcb_sync_change_counter –"
---

<p>xcb_sync_change_counter &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/sync.h&gt;
Request function
xcb_void_cookie_t xcb_sync_change_counter(xcb_connection_t *conn, xcb_sync_counter_t counter, xcb_sync_int64_t amount);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>counter</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd>
<dt><i>amount</i></dt>
<dd>TODO: NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_sync_change_counter_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from sync.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
