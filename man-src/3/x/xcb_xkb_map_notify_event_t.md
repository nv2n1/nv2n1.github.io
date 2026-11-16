---
title: "xcb_xkb_map_notify_event_t(3)"
name: "xcb_xkb_map_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_map_notify_event_t/"
description: "xcb_xkb_map_notify_event_t –"
---

<p>xcb_xkb_map_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_map_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>ptrBtnActions</i>;
 uint16_t <i>changed</i>;
 xcb_keycode_t <i>minKeyCode</i>;
 xcb_keycode_t <i>maxKeyCode</i>;
 uint8_t <i>firstType</i>;
 uint8_t <i>nTypes</i>;
 xcb_keycode_t <i>firstKeySym</i>;
 uint8_t <i>nKeySyms</i>;
 xcb_keycode_t <i>firstKeyAct</i>;
 uint8_t <i>nKeyActs</i>;
 xcb_keycode_t <i>firstKeyBehavior</i>;
 uint8_t <i>nKeyBehavior</i>;
 xcb_keycode_t <i>firstKeyExplicit</i>;
 uint8_t <i>nKeyExplicit</i>;
 xcb_keycode_t <i>firstModMapKey</i>;
 uint8_t <i>nModMapKeys</i>;
 xcb_keycode_t <i>firstVModMapKey</i>;
 uint8_t <i>nVModMapKeys</i>;
 uint16_t <i>virtualMods</i>;
 uint8_t <i>pad0</i>[2];
} <code>xcb_xkb_map_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></dt>
<dd>The type of this event, in this case <i>XCB_XKB_MAP_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</dd>
<dt><i>sequence</i></dt>
<dd>The sequence number of the last request processed by the X11 server.</dd>
<dt><i>xkbType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>time</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>deviceID</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>ptrBtnActions</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>changed</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>minKeyCode</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>maxKeyCode</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstType</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nTypes</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstKeySym</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeySyms</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyAct</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeyActs</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyBehavior</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeyBehavior</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstKeyExplicit</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nKeyExplicit</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstModMapKey</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nModMapKeys</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>firstVModMapKey</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>nVModMapKeys</i></dt>
<dd>NOT YET DOCUMENTED.</dd>
<dt><i>virtualMods</i></dt>
<dd>NOT YET DOCUMENTED.</dd></dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
