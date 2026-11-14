---
title: "xcb_change_save_set(3)"
name: "xcb_change_save_set"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_change_save_set/"
description: "xcb_change_save_set – Changes a client’s save set"
---

<p>xcb_change_save_set &#8211; Changes a client&#8217;s save set</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_change_save_set(xcb_connection_t *conn, uint8_t mode, xcb_window_t window);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>mode</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_SET_MODE_INSERT</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>XCB_SET_MODE_DELETE</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
</dl>
<dl>
<dd>Insert to add the specified window to the save set or Delete to delete it from the save set.</dl>
<dt><i>window</i></p>
<dd>The window to add or delete to/from your save set.</dl>
<h2>Description</h2>
<p>TODO: explain what the save set is for. </p>
<p> This function either adds or removes the specified window to the client&#8217;s (your application&#8217;s) save set.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_change_save_set_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_match_error_t</i></p>
<dd>You created the specified window. This does not make sense, you can only add windows created by other clients to your save set.</p>
<dt><i>xcb_value_error_t</i></p>
<dd>You specified an invalid mode.</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_reparent_window/">xcb_reparent_window</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
