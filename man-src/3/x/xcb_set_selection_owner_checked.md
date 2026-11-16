---
title: "xcb_set_selection_owner_checked(3)"
name: "xcb_set_selection_owner_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_set_selection_owner_checked/"
description: "xcb_set_selection_owner – Sets the owner of a selection"
---

<p>xcb_set_selection_owner &#8211; Sets the owner of a selection</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;
Request function
xcb_void_cookie_t xcb_set_selection_owner(xcb_connection_t *conn, xcb_window_t owner, xcb_atom_t selection, xcb_timestamp_t time);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></dt>
<dd>The XCB connection to X11.</dd>
<dt><i>owner</i></dt>
<dd>The new owner of the selection. </dd>
<p> The special value <i>XCB_NONE</i> means that the selection will have no owner.</p>
<dt><i>selection</i></dt>
<dd>The selection.</dd>
<dt><i>time</i></dt>
<dd>Timestamp to avoid race conditions when running X over the network. </dd>
<p> The selection will not be changed if <i>time</i> is earlier than the current last-change time of the <i>selection</i> or is later than the current X server time. Otherwise, the last-change time is set to the specified time. </p>
<p> The special value <i>XCB_CURRENT_TIME</i> will be replaced with the current server time.</dl>
<h2>Description</h2>
<p>Makes <i>window</i> the owner of the selection <i>selection</i> and updates the last-change time of the specified selection. </p>
<p> TODO: briefly explain what a selection is.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_set_selection_owner_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_atom_error_t</i></dt>
<dd><i>selection</i> does not refer to a valid atom.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_set_selection_owner/">xcb_set_selection_owner</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
