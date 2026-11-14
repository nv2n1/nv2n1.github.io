---
title: "xcb_xkb_latch_lock_state_checked(3)"
name: "xcb_xkb_latch_lock_state_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_latch_lock_state_checked/"
description: "xcb_xkb_latch_lock_state –"
---

<p>xcb_xkb_latch_lock_state &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;


Request function



xcb_void_cookie_t xcb_xkb_latch_lock_state(xcb_connection_t *conn, xcb_xkb_device_spec_t deviceSpec, uint8_t affectModLocks, uint8_t modLocks, uint8_t lockGroup, uint8_t groupLock, uint8_t affectModLatches, uint8_t latchGroup, uint16_t groupLatch);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>deviceSpec</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectModLocks</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>modLocks</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>lockGroup</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupLock</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>affectModLatches</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>latchGroup</i></p>
<dd>TODO: NOT YET DOCUMENTED.</p>
<dt><i>groupLatch</i></p>
<dd>TODO: NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_xkb_latch_lock_state_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
