---
title: "xcb_xkb_state_notify_event_t(3)"
name: "xcb_xkb_state_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_state_notify_event_t/"
description: "xcb_xkb_state_notify_event_t –"
---

<p>xcb_xkb_state_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_state_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>mods</i>;
 uint8_t <i>baseMods</i>;
 uint8_t <i>latchedMods</i>;
 uint8_t <i>lockedMods</i>;
 uint8_t <i>group</i>;
 int16_t <i>baseGroup</i>;
 int16_t <i>latchedGroup</i>;
 uint8_t <i>lockedGroup</i>;
 uint8_t <i>compatState</i>;
 uint8_t <i>grabMods</i>;
 uint8_t <i>compatGrabMods</i>;
 uint8_t <i>lookupMods</i>;
 uint8_t <i>compatLoockupMods</i>;
 uint16_t <i>ptrBtnState</i>;
 uint16_t <i>changed</i>;
 xcb_keycode_t <i>keycode</i>;
 uint8_t <i>eventType</i>;
 uint8_t <i>requestMajor</i>;
 uint8_t <i>requestMinor</i>;
} <code>xcb_xkb_state_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_XKB_STATE_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>xkbType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>deviceID</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>mods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>baseMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>latchedMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>lockedMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>group</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>baseGroup</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>latchedGroup</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>lockedGroup</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>compatState</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>grabMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>compatGrabMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>lookupMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>compatLoockupMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ptrBtnState</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changed</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>keycode</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>eventType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>requestMajor</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>requestMinor</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
