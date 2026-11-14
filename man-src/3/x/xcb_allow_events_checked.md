---
title: "xcb_allow_events_checked(3)"
name: "xcb_allow_events_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_allow_events_checked/"
description: "xcb_allow_events – release queued events"
---

<p>xcb_allow_events &#8211; release queued events</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_allow_events(xcb_connection_t *conn, uint8_t mode, xcb_timestamp_t time);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>mode</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_ALLOW_ASYNC_POINTER</i></p>
<dd>For AsyncPointer, if the pointer is frozen by the client, pointer event processing continues normally. If the pointer is frozen twice by the client on behalf of two separate grabs, AsyncPointer thaws for both. AsyncPointer has no effect if the pointer is not frozen by the client, but the pointer need not be grabbed by the client. </p>
<p> TODO: rewrite this in more understandable terms.</p>
<dt><i>XCB_ALLOW_SYNC_POINTER</i></p>
<dd>For SyncPointer, if the pointer is frozen and actively grabbed by the client, pointer event processing continues normally until the next ButtonPress or ButtonRelease event is reported to the client, at which time the pointer again appears to freeze. However, if the reported event causes the pointer grab to be released, then the pointer does not freeze. SyncPointer has no effect if the pointer is not frozen by the client or if the pointer is not grabbed by the client.</p>
<dt><i>XCB_ALLOW_REPLAY_POINTER</i></p>
<dd>For ReplayPointer, if the pointer is actively grabbed by the client and is frozen as the result of an event having been sent to the client (either from the activation of a GrabButton or from a previous AllowEvents with mode SyncPointer but not from a GrabPointer), then the pointer grab is released and that event is completely reprocessed, this time ignoring any passive grabs at or above (towards the root) the grab-window of the grab just released. The request has no effect if the pointer is not grabbed by the client or if the pointer is not frozen as the result of an event.</p>
<dt><i>XCB_ALLOW_ASYNC_KEYBOARD</i></p>
<dd>For AsyncKeyboard, if the keyboard is frozen by the client, keyboard event processing continues normally. If the keyboard is frozen twice by the client on behalf of two separate grabs, AsyncKeyboard thaws for both. AsyncKeyboard has no effect if the keyboard is not frozen by the client, but the keyboard need not be grabbed by the client.</p>
<dt><i>XCB_ALLOW_SYNC_KEYBOARD</i></p>
<dd>For SyncKeyboard, if the keyboard is frozen and actively grabbed by the client, keyboard event processing continues normally until the next KeyPress or KeyRelease event is reported to the client, at which time the keyboard again appears to freeze. However, if the reported event causes the keyboard grab to be released, then the keyboard does not freeze. SyncKeyboard has no effect if the keyboard is not frozen by the client or if the keyboard is not grabbed by the client.</p>
<dt><i>XCB_ALLOW_REPLAY_KEYBOARD</i></p>
<dd>For ReplayKeyboard, if the keyboard is actively grabbed by the client and is frozen as the result of an event having been sent to the client (either from the activation of a GrabKey or from a previous AllowEvents with mode SyncKeyboard but not from a GrabKeyboard), then the keyboard grab is released and that event is completely reprocessed, this time ignoring any passive grabs at or above (towards the root) the grab-window of the grab just released. The request has no effect if the keyboard is not grabbed by the client or if the keyboard is not frozen as the result of an event.</p>
<dt><i>XCB_ALLOW_ASYNC_BOTH</i></p>
<dd>For AsyncBoth, if the pointer and the keyboard are frozen by the client, event processing for both devices continues normally. If a device is frozen twice by the client on behalf of two separate grabs, AsyncBoth thaws for both. AsyncBoth has no effect unless both pointer and keyboard are frozen by the client.</p>
<dt><i>XCB_ALLOW_SYNC_BOTH</i></p>
<dd>For SyncBoth, if both pointer and keyboard are frozen by the client, event processing (for both devices) continues normally until the next ButtonPress, ButtonRelease, KeyPress, or KeyRelease event is reported to the client for a grabbed device (button event for the pointer, key event for the keyboard), at which time the devices again appear to freeze. However, if the reported event causes the grab to be released, then the devices do not freeze (but if the other device is still grabbed, then a subsequent event for it will still cause both devices to freeze). SyncBoth has no effect unless both pointer and keyboard are frozen by the client. If the pointer or keyboard is frozen twice by the client on behalf of two separate grabs, SyncBoth thaws for both (but a subsequent freeze for SyncBoth will only freeze each device once).</dl>
</dl>
<dl>
<dd></dl>
<dt><i>time</i></p>
<dd>Timestamp to avoid race conditions when running X over the network. </p>
<p> The special value <i>XCB_CURRENT_TIME</i> will be replaced with the current server time.</dl>
<h2>Description</h2>
<p>Releases queued events if the client has caused a device (pointer/keyboard) to freeze due to grabbing it actively. This request has no effect if <i>time</i> is earlier than the last-grab time of the most recent active grab for this client or if <i>time</i> is later than the current X server time.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_allow_events_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_value_error_t</i></p>
<dd>You specified an invalid <i>mode</i>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
