---
title: "xcb_ungrab_pointer_checked(3)"
name: "xcb_ungrab_pointer_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_ungrab_pointer_checked/"
description: "xcb_ungrab_pointer – release the pointer"
---

<p>xcb_ungrab_pointer &#8211; release the pointer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_ungrab_pointer(xcb_connection_t *conn, xcb_timestamp_t time);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>time</i></p>
<dd>Timestamp to avoid race conditions when running X over the network. </p>
<p> The pointer will not be released if <i>time</i> is earlier than the last-pointer-grab time or later than the current X server time.</dl>
<h2>Description</h2>
<p>Releases the pointer and any queued events if you actively grabbed the pointer before using <i>xcb_grab_pointer</i>, <i>xcb_grab_button</i> or within a normal button press. </p>
<p> EnterNotify and LeaveNotify events are generated.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_ungrab_pointer_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<p>This request does never generate any errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_enter_notify_event_t/">xcb_enter_notify_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_button/">xcb_grab_button</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_pointer/">xcb_grab_pointer</a></code>(3), <code><a href="/docs/linux/man/3-xcb_leave_notify_event_t/">xcb_leave_notify_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
