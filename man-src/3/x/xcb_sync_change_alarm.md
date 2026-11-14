---
title: "xcb_sync_change_alarm(3)"
name: "xcb_sync_change_alarm"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_sync_change_alarm/"
description: "xcb_sync_change_alarm –"
---

<p>xcb_sync_change_alarm &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/sync.h&gt;

Request function

    xcb_void_cookie_t
    xcb_sync_change_alarm(xcb_connection_t *conn, xcb_sync_alarm_t id, uint32_t value_mask, const void *value_list);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>id</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>value_mask</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>value_list</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_sync_change_alarm_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from sync.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
