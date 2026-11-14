---
title: "xcb_kill_client_checked-2(3)"
name: "xcb_kill_client_checked-2"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_kill_client_checked-2/"
description: "xcb_kill_client – kills a client"
---

<p>xcb_kill_client &#8211; kills a client</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_kill_client(xcb_connection_t *conn, uint32_t resource);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>resource</i></p>
<dd>Any resource belonging to the client (for example a Window), used to identify the client connection. </p>
<p> The special value of <i>XCB_KILL_ALL_TEMPORARY</i>, the resources of all clients that have terminated in <i>RetainTemporary</i> (TODO) are destroyed.</dl>
<h2>Description</h2>
<p>Forces a close down of the client that created the specified <i>resource</i>.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_kill_client_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_value_error_t</i></p>
<dd>The specified <i>resource</i> does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/1-xkill/">xkill</a></code>(1)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
