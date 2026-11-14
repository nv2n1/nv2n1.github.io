---
title: "xcb_free_gc(3)"
name: "xcb_free_gc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_free_gc/"
description: "xcb_free_gc – Destroys a graphics context"
---

<p>xcb_free_gc &#8211; Destroys a graphics context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_free_gc(xcb_connection_t *conn, xcb_gcontext_t gc);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>gc</i></p>
<dd>The graphics context to destroy.</dl>
<h2>Description</h2>
<p>Destroys the specified <i>gc</i> and all associated storage.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_free_gc_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_g_context_error_t</i></p>
<dd>The specified graphics context does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
