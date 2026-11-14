---
title: "xcb_damage_subtract(3)"
name: "xcb_damage_subtract"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_damage_subtract/"
description: "xcb_damage_subtract –"
---

<p>xcb_damage_subtract &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/damage.h&gt;


Request function



xcb_void_cookie_t xcb_damage_subtract(xcb_connection_t *conn, xcb_damage_damage_t damage, xcb_xfixes_region_t repair, xcb_xfixes_region_t parts);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>damage</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>repair</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>parts</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_damage_subtract_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from damage.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
