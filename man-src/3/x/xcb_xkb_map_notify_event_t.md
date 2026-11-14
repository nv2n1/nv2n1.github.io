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
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_XKB_MAP_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>xkbType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>deviceID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>ptrBtnActions</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changed</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>minKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>maxKeyCode</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstKeySym</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeySyms</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstKeyAct</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeyActs</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstKeyBehavior</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeyBehavior</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstKeyExplicit</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeyExplicit</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstModMapKey</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nModMapKeys</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstVModMapKey</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nVModMapKeys</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>virtualMods</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
