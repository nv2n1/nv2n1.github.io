---
title: "xcb_button_press_event_t(3)"
name: "xcb_button_press_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_button_press_event_t/"
description: "xcb_button_press_event_t – a mouse button was pressed/released"
---

<p>xcb_button_press_event_t &#8211; a mouse button was pressed/released</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xproto.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_button_press_event_t {
 uint8_t <i>response_type</i>;
 xcb_button_t <i>detail</i>;
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
 uint8_t <i>same_screen</i>;
 uint8_t <i>pad0</i>;
} <code>xcb_button_press_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_BUTTON_RELEASE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>detail</i></dt>
<dd>The keycode (a number representing a physical key on the keyboard) of the key which was pressed.</dd>
<dt><i>time</i></dt>
<dd>Time when the event was generated (in milliseconds).</dd>
<dt><i>root</i></dt>
<dd>The root window of <i>child</i>.</dd>
<dt><i>event</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>child</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>root_x</i></dt>
<dd>The X coordinate of the pointer relative to the <i>root</i> window at the time of the event.</dd>
<dt><i>root_y</i></dt>
<dd>The Y coordinate of the pointer relative to the <i>root</i> window at the time of the event.</dd>
<dt><i>event_x</i></dt>
<dd>If <i>same_screen</i> is true, this is the X coordinate relative to the <i>event</i> window&#8217;s origin. Otherwise, <i>event_x</i> will be set to zero.</dd>
<dt><i>event_y</i></dt>
<dd>If <i>same_screen</i> is true, this is the Y coordinate relative to the <i>event</i> window&#8217;s origin. Otherwise, <i>event_y</i> will be set to zero.</dd>
<dt><i>state</i></dt>
<dd>The logical state of the pointer buttons and modifier keys just prior to the event.</dd>
<dt><i>same_screen</i></dt>
<dd>Whether the <i>event</i> window is on the same screen as the <i>root</i> window.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code>xcb_generic_event_t</code>(3), <code><a href="/docs/linux/man/3-xcb_grab_button/">xcb_grab_button</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_pointer/">xcb_grab_pointer</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
