---
title: "xcb_leave_notify_event_t(3)"
name: "xcb_leave_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_leave_notify_event_t/"
description: "xcb_leave_notify_event_t – the pointer is in a different window"
---

<p>xcb_leave_notify_event_t &#8211; the pointer is in a different window</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_leave_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>detail</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 xcb_window_t <i>root</i>;
 xcb_window_t <i>event</i>;
 xcb_window_t <i>child</i>;
 int16_t <i>root_x</i>;
 int16_t <i>root_y</i>;
 int16_t <i>event_x</i>;
 int16_t <i>event_y</i>;
 uint16_t <i>state</i>;
 uint8_t <i>mode</i>;
 uint8_t <i>same_screen_focus</i>;
} <code>xcb_leave_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_LEAVE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>detail</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root</i></p>
<dd>The root window for the final cursor position.</p>
<dt><i>event</i></p>
<dd>The window on which the event was generated.</p>
<dt><i>child</i></p>
<dd>If the <i>event</i> window has subwindows and the final pointer position is in one of them, then <i>child</i> is set to that subwindow, <i>XCB_WINDOW_NONE</i> otherwise.</p>
<dt><i>root_x</i></p>
<dd>The pointer X coordinate relative to <i>root</i>&#8216;s origin at the time of the event.</p>
<dt><i>root_y</i></p>
<dd>The pointer Y coordinate relative to <i>root</i>&#8216;s origin at the time of the event.</p>
<dt><i>event_x</i></p>
<dd>If <i>event</i> is on the same screen as <i>root</i>, this is the pointer X coordinate relative to the event window&#8217;s origin.</p>
<dt><i>event_y</i></p>
<dd>If <i>event</i> is on the same screen as <i>root</i>, this is the pointer Y coordinate relative to the event window&#8217;s origin.</p>
<dt><i>state</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>mode</i></p>
<dd>
<dt><i>same_screen_focus</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
