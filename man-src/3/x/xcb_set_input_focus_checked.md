---
title: "xcb_set_input_focus_checked(3)"
name: "xcb_set_input_focus_checked"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_set_input_focus_checked/"
description: "xcb_set_input_focus – Sets input focus"
---

<p>xcb_set_input_focus &#8211; Sets input focus</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;


Request function



xcb_void_cookie_t xcb_set_input_focus(xcb_connection_t *conn, uint8_t revert_to, xcb_window_t focus, xcb_timestamp_t time);</code></pre>
<h2>Request Arguments</h2>
<dl>
<dt><i>conn</i></p>
<dd>The XCB connection to X11.</p>
<dt><i>revert_to</i></p>
<dd>One of the following values:</p>
<dl>
<dd>
<dl>
<dt><i>XCB_INPUT_FOCUS_NONE</i></p>
<dd>The focus reverts to <i>XCB_NONE</i>, so no window will have the input focus.</p>
<dt><i>XCB_INPUT_FOCUS_POINTER_ROOT</i></p>
<dd>The focus reverts to <i>XCB_POINTER_ROOT</i> respectively. When the focus reverts, FocusIn and FocusOut events are generated, but the last-focus-change time is not changed.</p>
<dt><i>XCB_INPUT_FOCUS_PARENT</i></p>
<dd>The focus reverts to the parent (or closest viewable ancestor) and the new revert_to value is <i>XCB_INPUT_FOCUS_NONE</i>.</p>
<dt><i>XCB_INPUT_FOCUS_FOLLOW_KEYBOARD</i></p>
<dd>NOT YET DOCUMENTED. Only relevant for the xinput extension.</dl>
</dl>
<dl>
<dd>Specifies what happens when the <i>focus</i> window becomes unviewable (if <i>focus</i> is neither <i>XCB_NONE</i> nor <i>XCB_POINTER_ROOT</i>).</dl>
<dt><i>focus</i></p>
<dd>The window to focus. All keyboard events will be reported to this window. The window must be viewable (TODO), or a <i>xcb_match_error_t</i> occurs (TODO). </p>
<p> If <i>focus</i> is <i>XCB_NONE</i> (TODO), all keyboard events are discarded until a new focus window is set. </p>
<p> If <i>focus</i> is <i>XCB_POINTER_ROOT</i> (TODO), focus is on the root window of the screen on which the pointer is on currently.</p>
<dt><i>time</i></p>
<dd>Timestamp to avoid race conditions when running X over the network. </p>
<p> The special value <i>XCB_CURRENT_TIME</i> will be replaced with the current server time.</dl>
<h2>Description</h2>
<p>Changes the input focus and the last-focus-change time. If the specified <i>time</i> is earlier than the current last-focus-change time, the request is ignored (to avoid race conditions when running X over the network). </p>
<p> A FocusIn and FocusOut event is generated when focus is changed.</p>
<h2>Return Value</h2>
<p>Returns an <i>xcb_void_cookie_t</i>. Errors (if any) have to be handled in the event loop. </p>
<p> If you want to handle errors directly with <i>xcb_request_check</i> instead, use <i>xcb_set_input_focus_checked</i>. See <code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a>(3)</code> for details.</p>
<h2>Errors</h2>
<dl>
<dt><i>xcb_match_error_t</i></p>
<dd>The specified <i>focus</i> window is not viewable.</p>
<dt><i>xcb_value_error_t</i></p>
<dd>TODO: Reasons?</p>
<dt><i>xcb_window_error_t</i></p>
<dd>The specified <i>focus</i> window does not exist.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb-requests/">xcb-requests</a></code>(3), <code><a href="/docs/linux/man/3-xcb_focus_in_event_t/">xcb_focus_in_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_focus_out_event_t/">xcb_focus_out_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
