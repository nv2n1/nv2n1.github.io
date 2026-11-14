---
title: "xcb_xkb_new_keyboard_notify_event_t(3)"
name: "xcb_xkb_new_keyboard_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_new_keyboard_notify_event_t/"
description: "xcb_xkb_new_keyboard_notify_event_t –"
---

<p>xcb_xkb_new_keyboard_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_new_keyboard_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>oldDeviceID</i>;
 xcb_keycode_t <i>minKeyCode</i>;
 xcb_keycode_t <i>maxKeyCode</i>;
 xcb_keycode_t <i>oldMinKeyCode</i>;
 xcb_keycode_t <i>oldMaxKeyCode</i>;
 uint8_t <i>requestMajor</i>;
 uint8_t <i>requestMinor</i>;
 uint16_t <i>changed</i>;
 uint8_t <i>pad0</i>[14];
} <code>xcb_xkb_new_keyboard_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_XKB_NEW_KEYBOARD_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>xkbType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>deviceID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>oldDeviceID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>minKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>maxKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>oldMinKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>oldMaxKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>requestMajor</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>requestMinor</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changed</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
