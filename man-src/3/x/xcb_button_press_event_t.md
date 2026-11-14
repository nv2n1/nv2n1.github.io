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
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_BUTTON_RELEASE</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>detail</i></p>
<dd>The keycode (a number representing a physical key on the keyboard) of the key which was pressed.</p>
<dt><i>time</i></p>
<dd>Time when the event was generated (in milliseconds).</p>
<dt><i>root</i></p>
<dd>The root window of <i>child</i>.</p>
<dt><i>event</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>child</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>root_x</i></p>
<dd>The X coordinate of the pointer relative to the <i>root</i> window at the time of the event.</p>
<dt><i>root_y</i></p>
<dd>The Y coordinate of the pointer relative to the <i>root</i> window at the time of the event.</p>
<dt><i>event_x</i></p>
<dd>If <i>same_screen</i> is true, this is the X coordinate relative to the <i>event</i> window&#8217;s origin. Otherwise, <i>event_x</i> will be set to zero.</p>
<dt><i>event_y</i></p>
<dd>If <i>same_screen</i> is true, this is the Y coordinate relative to the <i>event</i> window&#8217;s origin. Otherwise, <i>event_y</i> will be set to zero.</p>
<dt><i>state</i></p>
<dd>The logical state of the pointer buttons and modifier keys just prior to the event.</p>
<dt><i>same_screen</i></p>
<dd>Whether the <i>event</i> window is on the same screen as the <i>root</i> window.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xcb_generic_event_t/">xcb_generic_event_t</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_button/">xcb_grab_button</a></code>(3), <code><a href="/docs/linux/man/3-xcb_grab_pointer/">xcb_grab_pointer</a></code>(3)</p>
<h2>Author</h2>
<p>Generated from xproto.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
