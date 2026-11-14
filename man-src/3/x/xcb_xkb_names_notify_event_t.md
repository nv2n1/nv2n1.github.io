---
title: "xcb_xkb_names_notify_event_t(3)"
name: "xcb_xkb_names_notify_event_t"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcb_xkb_names_notify_event_t/"
description: "xcb_xkb_names_notify_event_t –"
---

<p>xcb_xkb_names_notify_event_t &#8211;</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;xcb/xkb.h&gt;</code></pre>
<h3>Event datastructure</h3>
<pre>typedef struct xcb_xkb_names_notify_event_t {
 uint8_t <i>response_type</i>;
 uint8_t <i>xkbType</i>;
 uint16_t <i>sequence</i>;
 xcb_timestamp_t <i>time</i>;
 uint8_t <i>deviceID</i>;
 uint8_t <i>pad0</i>;
 uint16_t <i>changed</i>;
 uint8_t <i>firstType</i>;
 uint8_t <i>nTypes</i>;
 uint8_t <i>firstLevelName</i>;
 uint8_t <i>nLevelNames</i>;
 uint8_t <i>pad1</i>;
 uint8_t <i>nRadioGroups</i>;
 uint8_t <i>nKeyAliases</i>;
 uint8_t <i>changedGroupNames</i>;
 uint16_t <i>changedVirtualMods</i>;
 xcb_keycode_t <i>firstKey</i>;
 uint8_t <i>nKeys</i>;
 uint32_t <i>changedIndicators</i>;
 uint8_t <i>pad2</i>[4];
} <code>xcb_xkb_names_notify_event_t</code>;</pre>
<h2>Event Fields</h2>
<dl>
<dt><i>response_type</i></p>
<dd>The type of this event, in this case <i>XCB_XKB_NAMES_NOTIFY</i>. This field is also present in the <i>xcb_generic_event_t</i> and can be used to tell events apart from each other.</p>
<dt><i>sequence</i></p>
<dd>The sequence number of the last request processed by the X11 server.</p>
<dt><i>xkbType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>time</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>deviceID</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changed</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstType</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nTypes</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstLevelName</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nLevelNames</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nRadioGroups</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeyAliases</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changedGroupNames</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changedVirtualMods</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>firstKey</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>nKeys</i></p>
<dd>NOT YET DOCUMENTED.</p>
<dt><i>changedIndicators</i></p>
<dd>NOT YET DOCUMENTED.</dl>
<h2>Description</h2>
<h2>See Also</h2>
<h2>Author</h2>
<p>Generated from xkb.xml. Contact xcb [at] lists.freedesktop.org for corrections and improvements.</p>
